from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите адресс доставки'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Ваши комментарии по желанию"}))
    class Meta:
        model = Order
        fields = ['address', 'comment']

