from django.shortcuts import render, redirect
from .forms import SalesOrderForm, SalesItemFormSet,SignUpForm
from .models import SalesOrder, SalesItem, Customer
from django.contrib import messages
from django.db.models import Sum, Q, Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.http import HttpResponseForbidden
from .util import render_to_pdf
from django.views import View


def dashboard(request):
    total_orders = SalesOrder.objects.count()
    total_revenue = sum(item.quantity * item.product.price for item in SalesItem.objects.select_related('product'))
    total_customers = Customer.objects.count()

    best_selling = (
        SalesItem.objects.values('product__name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')[:5]
    )

    context = {
        'total_orders': total_orders,
        'tota_revenue': total_revenue,
        'total_customers': total_customers,
        'best_selling': best_selling,
    }

    return render(request, 'dashboard.html', context)


class InvoicePDFView(View):
    def get(self, request, pk):
        order = SalesOrder.objects.get(pk=pk)
        context = {'order': order}
        return render_to_pdf('invoice.html', context)
    

class SalesOrderListView(ListView):
    model = SalesOrder
    template_name = 'order_list.html'
    context_object_name = 'orders'
    # paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related('items__product', 'customer')

        if not self.request.user.is_superuser:
           qs = qs.filter(user=self.request.user)
           print('user is:', self.request.user)

        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(customer__name__icontains=query) |
                Q(items__product__name__icontains=query)
            ).distinct()
        return qs


@login_required
def create_sales_order(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    if request.method == 'POST':
        order_form = SalesOrderForm(request.POST)
        formset = SalesItemFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            formset.instance = order
            formset.save()
            # items = formset.save(commit=False)
            # for item in items:
            #     item.order = order  # link item to the saved order
            #     item.save()
            return redirect('order_success')  # redirect to a success page or order detail
    else:
        order_form = SalesOrderForm()
        formset = SalesItemFormSet()

    return render(request, 'create_order.html', {
        'order_form': order_form,
        'formset': formset,
    })


def order_success(request):
    return render(request, 'order_success.html',{})

# @login_required
# def order_list(request):
#     print('user is:' , request.user)
#     if request.user.is_superuser:
#         orders = SalesOrder.objects.all()#.select_related('customer')#.prefetch_related('items__product')
#     else:
#        orders = SalesOrder.objects.filter(user=request.user)
       
#     return render(request, 'order_list1.html', {'orders': orders})


def order_detail(request, pk):
    order = SalesOrder.objects.get(pk=pk)
    return render (request, 'order_detail.html', {'order': order})


def home(request):
    # check to see if loggin in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authinticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In')
            return redirect ('home')
        else:
            messages.success(request, 'There Was An Error Logging In, Please Try Again!')
            return redirect ('home')
    else:
        return render (request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return redirect ('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})
