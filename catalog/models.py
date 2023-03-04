from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название категории')

    def __str__(self):
        return f"Категория: {self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    price = models.IntegerField(default=0, verbose_name='Цена продукта')
    checkbox = models.BooleanField(verbose_name='Чек бокс')
    date = models.DateField(verbose_name='Поле даты')

    def __str__(self):
        return f"Продукт: {self.id}"
