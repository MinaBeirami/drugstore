# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User as U


# Create your models here.
class Person(U):
    tel = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Drug(models.Model):
    Commercial_name = models.CharField(max_length=20, primary_key=True)
    Generic_name = models.CharField(max_length=20)
    Dose = models.IntegerField()
    Side_effects = models.CharField(max_length=100)
    How_to_use = models.CharField(max_length=100)
    Drug_interactions = models.CharField(max_length=100)
    Compositions = models.CharField(max_length=100)
    Price = models.IntegerField()
    Necessity_of_prescription = models.IntegerField()
    Drug_code = models.IntegerField()

    def __str__(self):
        cn=self.Commercial_name
        gn=self.Generic_name
        d=self.Dose
        se=self.How_to_use
        arg={'cn':cn,'gn':gn,'d':d,'se':se}
        return arg

class AddressOfDrugstore(models.Model):
    block_number = models.CharField(max_length=5)
    alley = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    tel = models.IntegerField()
    postal_code = models.CharField(max_length=10, primary_key=True)


class OrderModel(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)


class StorageModel(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    stock = models.IntegerField(default=0)


class DrugStore(models.Model):
    name = models.CharField(max_length=20)
    drug_code = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    address_list = models.ManyToManyField(AddressOfDrugstore)
    storage_list = models.ManyToManyField(StorageModel)


class Order(models.Model):
    patiant = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    prescription = models.ManyToManyField(OrderModel)
    date = models.DateField(default=now)
    drug_store = models.ForeignKey(DrugStore, on_delete=models.DO_NOTHING)
