from django.urls import path
from .views import home, galeria, somos, api, conta, mostrar, eliminar, crear, modificar

urlpatterns=[
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('somos/', somos, name="somos"),
    path('conta/', conta, name="conta"),
    path('api/', api, name="api"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crear/', crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
]