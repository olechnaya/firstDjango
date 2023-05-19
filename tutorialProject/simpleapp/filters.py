import django_filters as filters # импортируем filterset, чем-то напоминающий знакомые дженерики
from django import forms
from .models import Product, Category
 
 
# создаём фильтр
class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(label='Название', lookup_expr='icontains')
    price = filters.CharFilter(label='цена', lookup_expr='lt')
    quantity = filters.CharFilter(label='количество', lookup_expr='gt')
    category = filters.ModelChoiceFilter(
        label = 'Категории',
        queryset = Category.objects.all()
    )
    category = forms.ModelChoiceField(queryset=Category.objects.values())
   
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
      model = Product
      fields = ('name', 'price', 'quantity', 'category') # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)
      # fields = {
      #           'name': ['icontains'], # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то, что запросил пользователь
      #           'quantity': ['gt'], # количество товаров должно быть больше или равно тому, что указал пользователь
      #           'price': ['lt'], # цена должна быть меньше или равна тому, что указал пользователь
      #           'category': ['exact'],
      # }