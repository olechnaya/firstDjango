from django.urls import path
from . import views
from .views import ProductList, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView, login
 
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', ProductList.as_view(), name='products'), 
    path('<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'), 
     
]