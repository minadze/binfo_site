import datetime
from django.contrib.auth.models import User
from django.db import models
from django import forms
# Create your models here.

''' *******************************************************
    Города и страны
    ******************************************************* '''
class Country(models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering=['-favorite', 'iso',]

    name_ru = models.CharField(verbose_name='Страна', max_length=100, db_index=True, default='', unique=True)
    name_en = models.CharField(verbose_name='Country', max_length=100, db_index=True, default='', unique=True)
    iso = models.CharField(verbose_name='ISO', max_length=3, db_index=True, default='', unique=True)
    favorite = models.BooleanField(verbose_name='Избранное', default=False)



    def __str__(self):
        return self.name_ru

class City(models.Model):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ['-favorite', 'name_ru', ]

    country = models.ForeignKey(Country)
    name_ru= models.CharField(verbose_name='Город', max_length=200, db_index=True, default='')
    name_en = models.CharField(verbose_name='City', max_length=200, db_index=True, default='')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    favorite = models.BooleanField(verbose_name='Избранное', default=False)

    def __str__(self):
        return self.name_ru


''' *******************************************************
    Категории и продукты
    ******************************************************* '''
class Category(models.Model):
    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    parent = models.ForeignKey('self', blank=True, null=True)
    name_ru = models.CharField(verbose_name='Категория товара', max_length=200, db_index=True, default='')
    name_en = models.CharField(verbose_name='Product category', max_length=200, db_index=True, default='')

    def __str__(self):
        return self.name_ru


class Manufacturer(models.Model):
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    name = models.CharField(verbose_name='Наименование производителя', max_length=200, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    category = models.ForeignKey(Category)
    country = models.ForeignKey(Country, verbose_name='Страна производитель')
    barcode = models.BigIntegerField(verbose_name='Штрихкод')
    name_ru = models.CharField(verbose_name='Наименование товара', max_length=200, db_index=True, default='')
    name_en = models.CharField(verbose_name='Product name', max_length=200, db_index=True, default='')

    def __str__(self):
        return self.name_ru


class ProductDescription(models.Model):
    class Meta:
        verbose_name = "Описание товара"
        verbose_name_plural = "Описания товаров"

    product = models.ForeignKey(Product)
    description_ru = models.TextField(verbose_name='Описание', max_length=4000,default='')
    description_en = models.TextField(verbose_name='Description', max_length=4000, default='')
    manufacturer = models.CharField(verbose_name='Производитель', max_length=200, default='')


''' *******************************************************
    Владельцы
    ******************************************************* '''
class Owner(models.Model):
    class Meta:
        verbose_name = "Владелец тогровой точки"
        verbose_name_plural = "Владельцы торговых точек"

    city = models.ForeignKey(City)
    legal_address = models.TextField(verbose_name='Юридический адрес', max_length=500, default='')
    actual_address = models.TextField(verbose_name='Фактический адрес', max_length=500, default='')
    tax_number = models.BigIntegerField(verbose_name='ИНН', db_index=True)
    name = models.CharField(verbose_name='Наименование тороговой точки', max_length=200, db_index=True, default='')
    director = models.CharField(verbose_name='ФИО руководителя или владельца', max_length=200, default='')
    email = models.EmailField(verbose_name='Email', max_length=100, default='')
    work_phone = models.CharField(verbose_name='Рабочий телефон', max_length=100, default='')
    mobile_phone = models.TextField(verbose_name='Мобильный телефон', max_length=100, default='')
    fax = models.CharField(verbose_name='Факс', max_length=100, default='')
    site = models.URLField(verbose_name='Сайт', max_length=1000, default='')
    userid = models.OneToOneField(User)

    def __str__(self):
        return self.name


''' *******************************************************
    Тогровые точки и цены
    ******************************************************* '''
class Market(models.Model):
    class Meta:
        verbose_name = "Тороговая точка"
        verbose_name_plural = "Тороговые точки"

    owner = models.ForeignKey(Owner, blank=True, null=True)
    city = models.ForeignKey(City)
    name = models.CharField(verbose_name='Наименование тороговой точки', max_length=200, db_index=True, default='')
    address = models.TextField(verbose_name='Адрес', max_length=500, default='')
    worktime = models.TextField(verbose_name='Рабочее время', max_length=500, default='')
    latitude = models.FloatField(verbose_name='Широта', default=0)
    longitude = models.FloatField(verbose_name='Долгота', default=0)

    def save(self, *args, **kwargs):
        if self.latitude == 0:
            self.latitude = self.city.latitude
        if self.longitude == 0:
            self.longitude = self.city.longitude
        super(Market, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

''' *******************************************************
    Цены
    ******************************************************* '''
class Price(models.Model):
    class Meta:
        verbose_name = "Цена за единицу товара"

    market = models.ForeignKey(Market)
    product = models.ForeignKey(Product)
    price = models.FloatField(verbose_name='Стоимость')
    editdate = models.DateField(default=datetime.date.today)

''' *******************************************************
    Настройки пользователя
    ******************************************************* '''
class UserSettings(models.Model):
    user = models.OneToOneField(User)
    FavoriteProduct = models.ManyToManyField(Product)