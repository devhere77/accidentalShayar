from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('privacy-policy', views.privacyPolicy, name="privacy-policy"),
    path('shayari/<int:id>', views.shayari, name="shayari"),
    path('category/<slug:slug>', views.categoryShayari, name="categoryShayari"),
]
