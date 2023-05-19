from django.shortcuts import render
#from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.views import View # импортируем простую вьюшку
from django.views.generic import ListView
#from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод


from .models import Product
from .filters import ProductFilter
# from datetime import datetime 
 
 
# class ProductsList(ListView):
    # model = Product  
    # template_name = 'products.html'
    # context_object_name = 'products'
    # queryset = Product.objects.order_by('-id')

    # # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
    #     context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
    #     context['value2'] = ""
    #     return context

# class ProductPaging(ListView):
    
#     def get(self, request):
#         products = Product.objects.all()
#         p = Paginator(products, 1)
#         products = p.get_page(request.GET.get('page', 1))
#         data = {
#             'products': products,
#         }
#         return render(request, 'products.html', data)

class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1 # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context

# создаём представление, в котором будут детали конкретного отдельного товара
# class ProductDetail(DetailView):
class ProductDetail(View):
    model = Product 
    template_name = 'product.html'
    context_object_name = 'product'