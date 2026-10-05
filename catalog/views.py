from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
# Create your views here.



def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})


def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        price = request.POST.get('price', '').strip()
        if name and price:
            Product.objects.create(name=name, price=price)
            messages.success(request, f'Товар «{name}» додано')
            return redirect('product_list')
        messages.error(request, 'Заповніть усі поля')
    return render(request, 'catalog/product_form.html')