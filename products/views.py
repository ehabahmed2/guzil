from django.shortcuts import render, redirect
from products.forms import CreateProductForm
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})




@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم اضافه المنتج')
            return redirect('admin_dashboard')
        else: 
            messages.error(request, 'حدث خطا')
    else: 
        form = CreateProductForm()
    return render(request, 'admin/create_product.html', {'form': form})