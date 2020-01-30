from django.shortcuts import render
from django.http import HttpResponse
from .models import Shayari, Category

# Create your views here.


def home(request):
    shayari = Shayari.objects.all()
    revShayari = Shayari.objects.all().order_by('-date_created')
    category = Category.objects.all()
    return render(request, 'index.html', {'shayar': shayari, 'category': category, 'revShayari': revShayari})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def shayari(request, id):
    shyri = Shayari.objects.get(pk=id)
    return render(request, 'shayari.html', {'detail': shyri})