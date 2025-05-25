from django.shortcuts import render, redirect
from .forms import SalesOrderForm, SalesItemFormSet,SignUpForm
from .models import SalesOrder
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def create_sales_order(request):
    if request.method == 'POST':
        order_form = SalesOrderForm(request.POST)
        formset = SalesItemFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
            order_user = request.user
            items = formset.save(commit=False)
            for item in items:
                item.order = order  # link item to the saved order
                item.save()
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

@login_required
def order_list(request):
    orders = SalesOrder.objects.all()#.select_related('customer')#.prefetch_related('items__product')
    return render(request, 'order_list.html', {'orders': orders})


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


def logout_uset(request):
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
