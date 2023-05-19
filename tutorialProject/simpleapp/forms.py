from django import forms
from django.forms import ModelForm, Select, TextInput, BooleanField
from .models import Product, Category

class ProductForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'   

    name = forms.CharField(
        label = 'Название',
        widget=forms.TextInput(attrs={
            'placeholder': 'Например, молоко...', 
            'class':'form-control',
            'id': 'adding-item-name' 
        }))
    
    price = forms.CharField(
        label = 'Цена',
        widget=forms.TextInput(attrs={            
            'class':'form-control',
            'id': 'adding-item-price'
        }))
    quantity = forms.CharField(
        label = 'Количество',
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
    
    #check_box = BooleanField(label='Ало, Галочка!')

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity']
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