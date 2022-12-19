from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'employee/index.html')

def addItem(request):
  return render(request, 'employee/add-item.html')