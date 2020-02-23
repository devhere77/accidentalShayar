from django.shortcuts import render
from django.http import HttpResponse
from .models import Shayari, Category
import random

# Create your views here.


def home(request):
    shayari = Shayari.objects.all().order_by('-id')
    revShayari = Shayari.objects.all().order_by('-date_created')[:4]
    popPost = random.sample(list(shayari), 4)
    category = Category.objects.all()
    return render(request, 'index.html', {'shayar': shayari, 'category': category, 'revShayari': revShayari, 'popPost': popPost})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def shayari(request, id):
    shyri = Shayari.objects.get(pk=id)
    return render(request, 'shayari.html', {'detail': shyri})


def privacyPolicy(request):
    return render(request, 'privacypolicy.html')


def categoryShayari(request, slug):
    slugs = format(slug.upper())
    shayaris = Shayari.objects.filter(category=slugs)
    return render(request, 'categoryShayari.html', {'shayariByCategory': shayaris})