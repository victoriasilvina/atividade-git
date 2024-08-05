from django.urls import path
from alunas.views import index, vivian, victoria

urlpatterns = [
    path('', index, name='index'),
    path('vivian', vivian, name='vivian'),
    path('victoria', victoria, name="victoria")
]
