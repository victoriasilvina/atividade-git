from django.urls import path
from alunas.views import index, vivian

urlpatterns = [
    path('', index, name='index'),
    path('vivian', vivian, name='vivian')
]
