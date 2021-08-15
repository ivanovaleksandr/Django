from django.shortcuts import render


# HttpRequest
# Create your views here.
# функции = контроллеры = вьюхи

def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
