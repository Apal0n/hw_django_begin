from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f"Название товара: {self.name}, цена товара: {self.price}"


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"ФИО клиента: {self.name}, возраст клиента: {self.age}, купил товар: {self.item_id}"
