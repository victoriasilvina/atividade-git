from django.urls import path
from alunas.views import index, victoria

urlpatterns = [
    path('', index, name='index'),
    path('victoria', victoria, name="victoria")
]
