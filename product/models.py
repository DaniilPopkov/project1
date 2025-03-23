from django.db import models

class Categorie(models.Model):
    name=models.CharField(max_length=150,verbose_name='Название')
    slug=models.SlugField(max_length=200,verbose_name='URL')

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=150,verbose_name='Название')
    slug=models.SlugField(max_length=200,verbose_name='URL')
    description=models.TextField(verbose_name='Описание')
    price=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Цена')
    discount=models.DecimalField(default=0.00,max_digits=4,decimal_places=2,verbose_name='Скидка в %')
    porcia=models.CharField(max_length=150,default=0,verbose_name='Порция')
    category=models.ForeignKey('Categorie',on_delete=models.CASCADE,verbose_name='Категория')

    def __str__(self):
        return self.name

