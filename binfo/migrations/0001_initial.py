# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 09:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(db_index=True, default='', max_length=200, verbose_name='Категория товара')),
                ('name_en', models.CharField(db_index=True, default='', max_length=200, verbose_name='Product category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='binfo.Category')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=200, verbose_name='Город')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('favorite', models.BooleanField(default=False, verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(db_index=True, default='', max_length=100, unique=True, verbose_name='Страна')),
                ('name_en', models.CharField(db_index=True, default='', max_length=100, unique=True, verbose_name='Country')),
                ('iso', models.CharField(db_index=True, default='', max_length=3, unique=True, verbose_name='ISO')),
                ('favorite', models.BooleanField(default=False, verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Наименование производителя')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=200, verbose_name='Наименование тороговой точки')),
                ('address', models.TextField(default='', max_length=500, verbose_name='Адрес')),
                ('latitude', models.FloatField(default=0, verbose_name='Широта')),
                ('longitude', models.FloatField(default=0, verbose_name='Долгота')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.City')),
            ],
            options={
                'verbose_name': 'Тороговая точка',
                'verbose_name_plural': 'Тороговые точки',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_address', models.TextField(default='', max_length=500, verbose_name='Юридический адрес')),
                ('actual_address', models.TextField(default='', max_length=500, verbose_name='Фактический адрес')),
                ('tax_number', models.BigIntegerField(db_index=True, verbose_name='ИНН')),
                ('name', models.CharField(db_index=True, default='', max_length=200, verbose_name='Наименование тороговой точки')),
                ('director', models.CharField(default='', max_length=200, verbose_name='ФИО руководителя или владельца')),
                ('email', models.EmailField(default='', max_length=100, verbose_name='Email')),
                ('work_phone', models.CharField(default='', max_length=100, verbose_name='Рабочий телефон')),
                ('mobile_phone', models.TextField(default='', max_length=100, verbose_name='Мобильный телефон')),
                ('fax', models.CharField(default='', max_length=100, verbose_name='Факс')),
                ('site', models.URLField(default='', max_length=1000, verbose_name='Сайт')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.City')),
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Владелец тогровой точки',
                'verbose_name_plural': 'Владельцы торговых точек',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('editdate', models.DateField(default=datetime.date.today)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.Market')),
            ],
            options={
                'verbose_name': 'Цена за единицу товара',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.BigIntegerField(verbose_name='Штрихкод')),
                ('name_ru', models.CharField(db_index=True, default='', max_length=200, verbose_name='Наименование товара')),
                ('name_en', models.CharField(db_index=True, default='', max_length=200, verbose_name='Product name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.Category')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.Country', verbose_name='Страна производитель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_ru', models.TextField(default='', max_length=4000, verbose_name='Описание')),
                ('description_en', models.TextField(default='', max_length=4000, verbose_name='Description')),
                ('manufacturer', models.CharField(default='', max_length=200, verbose_name='Производитель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.Product')),
            ],
            options={
                'verbose_name': 'Описание товара',
                'verbose_name_plural': 'Описания товаров',
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FavoriteProduct', models.ManyToManyField(to='binfo.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.Product'),
        ),
        migrations.AddField(
            model_name='market',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='binfo.Owner'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='binfo.Country'),
        ),
    ]
