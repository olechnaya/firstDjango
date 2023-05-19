from django.shortcuts import render
from django.views import View # импортируем простую вьюшку
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView # импоритируем необходимые дженерики
#from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from django.core.paginator import Paginator

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm

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
    form_class = ProductForm # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        
        # ОБЯЗАТЕЛЬНО ДОБАВИТЬ ЧТОБЫ НАПЕЧАТАЛИСЬ КАТЕГОРИИ В ФОРМЕ ДОБАВЛЕНИЯ ТОВАРА
        # context['categories'] = Category.objects.all()
        # context['form'] = ProductForm()
        return context
    
    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST) # создаём новую форму, забиваем в неё данные из POST-запроса 
 
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()
 
        return super().get(request, *args, **kwargs)
        # # берём значения для нового товара из POST-запроса отправленного на сервер
        # name = request.POST['name']
        # quantity = request.POST['quantity']
        # category_id = request.POST['category']
        # price = request.POST['price']

        # product = Product(
        #     name=name,
        #     quantity=quantity,
        #     category_id=category_id,
        #     price=price
        # )

        # product.save()
        # return super().get(request,*args, **kwargs)

# создаём представление, в котором будут детали конкретного отдельного товара
# class ProductDetail(DetailView):
class ProductDetailView(DetailView):
    # model = Product 
    template_name = 'product.html'
    queryset = Product.objects.all()
    # context_object_name = 'product'

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm

# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['isUpdateView'] = True # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context
 
 
# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
 