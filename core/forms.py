from django import forms
from django.forms import inlineformset_factory
from .models import SalesOrder, SalesItem

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer']

SalesItemFormSet = inlineformset_factory(
    SalesOrder, SalesItem,
    fields=('product', 'quantity'),
    extra=1,
    can_delete=True
)