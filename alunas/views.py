from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'alunas/index.html')

def victoria(request):
    return render(request, 'alunas/victoria.html')