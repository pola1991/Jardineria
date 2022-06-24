from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/app/index.html')

def productos(request):
    return render(request,'core/app/productos.html')

def addproducto(request):
    return render(request,'core/app/addproducto.html')