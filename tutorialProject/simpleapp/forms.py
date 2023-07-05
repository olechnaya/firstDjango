from django import forms
from django.forms import ModelForm, Select, TextInput, BooleanField
from .models import Product, Category
from django.utils.translation import gettext_lazy as _

class NewDtInput(forms.DateTimeInput):
    class Media:
        css = {
            "all": ["css/theme.css"],
            }
        js = ["js/jquery-3.7.0.min.js","js/calendar.min.js"]

class ProductForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'   
    checkbox = BooleanField(label='Ало, Галочка!') # добавляем галочку или же true-false поле
    #dt = DateField(label="Датапикер")
   
    name = forms.CharField(
        label = _('first name'),
        widget=forms.TextInput(attrs={
            'placeholder': 'Например, молоко...', 
            'class':'form-control',
            'id': 'adding-item-name' 
        }))
    
    price = forms.CharField(
        label = _('price'),
        widget=forms.TextInput(attrs={            
            'class':'form-control',
            'id': 'adding-item-price'
        }))
    quantity = forms.CharField(
        label = _('qwantity'),
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': 'adding-item-quantity'
        }))
    category = forms.ModelChoiceField(
        label = 'Категория',
        queryset = Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select', 
            'size': 3,
            'id': 'adding-item-category'
        }))    

    class Meta:
        model = Product
        fields = ['checkbox', 'name', 'price', 'category', 'quantity',]   
        # fields = ['checkbox', 'dt', 'name', 'price', 'category', 'quantity',]   
        # widgets = {
        #     'dt': NewDtInput()
        # }

        # fields = ['name', 'price', 'category', 'quantity',  'check_box']
        # widgets = {
        #     'name': TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Название'
        #     }),
        #     'price': TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Цена'
        #     }),
        #     'quantity': TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Количество'
        #     }),
        #     'category': Select(attrs={'class': 'form-select', 'size': 3})
        # }
        # labels = {
        #     'name': 'Название',
        #     'price': 'Цена',
        #     'category': 'Категория',
        #     'quantity': 'Количество',
        # }