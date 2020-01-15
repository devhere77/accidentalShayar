from django.db import models

# Create your models here.


class Shayari(models.Model):
    SHAYARI_CATEGORY = (
        ('MOTIVATIONAL', 'Motivational'),
        ('INSPIRATIONAL', 'Inspirational'),
        ('SAD', 'Sad'),
        ('ROMANTIC', 'Romantic'),
        ('LIFE', 'Life'),
        ('COMEDY', 'Comedy'),
    )
    name = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.CharField(max_length=20, choices=SHAYARI_CATEGORY, default='MOTIVATIONAL')
    img = models.ImageField(upload_to="uploads")
    date_created = models.DateField(auto_now=True)
    is_active = models.IntegerField(default=1)


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1)