from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):

    model = Product

    ordering = '-name'
    # queryset = Product.objects.filter (price__lt=300)

    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
