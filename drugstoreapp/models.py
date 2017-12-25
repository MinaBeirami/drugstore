# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User as U
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Person(U):
    tel = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

@python_2_unicode_compatible
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
        return self.Generic_name

class AddressOfDrugstore(models.Model):
    block_number = models.CharField(max_length=5)
    alley = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    tel = models.IntegerField()
    postal_code = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.block_number


class OrderModel(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)


class StorageModel(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    stock = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.drug


class DrugStore(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    drug_code = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    address_list = models.ManyToManyField(AddressOfDrugstore)
    storage_list = models.ManyToManyField(StorageModel)
    def __str__(self):
         return self.name


class Order(models.Model):
    #USERNAME_FIELD = 'email'
    #prescription = models.ManyToManyField(OrderModel)
    date = models.DateField(default=now)
    drug_store = models.ForeignKey(DrugStore, on_delete=models.DO_NOTHING)
