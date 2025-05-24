from django.shortcuts import render, redirect
from .forms import SalesOrderForm, SalesItemFormSet
from .models import SalesOrder
from django.db.models import Sum

# Create your views here.

def create_sales_order(request):
    if request.method == 'POST':
        order_form = SalesOrderForm(request.POST)
        formset = SalesItemFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
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




def order_list(request):
    orders = SalesOrder.objects.all().select_related('customer').prefetch_related('item_product')
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = SalesOrder.objects.get(pk=pk)
    return render (request, 'orderdetail.html', {'order': order})

def home(request):
    return render (request, 'home.html', {})
