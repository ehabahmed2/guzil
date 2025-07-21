from django.urls import path
from . import views
urlpatterns = [
    path('', views.products, name='products'),
    path('add-product', views.create_product, name='add_product'),

]


