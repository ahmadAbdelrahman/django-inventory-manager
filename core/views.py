from django.shortcuts import render, redirect
from .forms import SalesOrderForm, SalesItemFormSet
from .models import SalesOrder

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


def home(request):
    return render (request, 'home.html', {})
