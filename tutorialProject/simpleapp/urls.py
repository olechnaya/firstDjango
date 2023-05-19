from django.urls import path
from .views import ProductList,ProductDetail # импортируем наше представление
 
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', ProductList.as_view()), 
    path('<int:pk>', ProductDetail.as_view()), 
]