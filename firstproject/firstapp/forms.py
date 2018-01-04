from django import forms
from firstapp.models import Order
from firstapp.models import Pizza

class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')
