from django.urls import path
from alunas.views import index

urlpatterns = [
    path('', index, name='index')
]
