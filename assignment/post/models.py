from django.db import models
from django.urls import reverse


class Account(models.Model):
    name = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('post:detailAcc',kwargs={'pk':self.pk})

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.call, self.address)


class Stock(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField(blank=True)
    price = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return '{}/ 가격: {}/ 남은 수량: {}'.format(self.title, self.price, self.amount)
