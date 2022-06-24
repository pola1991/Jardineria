from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name = "index"),
    path('productos',productos, name = "productos"),
    path('addproducto',addproducto, name = "addproducto"),
]