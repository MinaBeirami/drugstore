from django.contrib import admin
from drugstoreapp.models import *

admin.site.register(Person)
admin.site.register(Drug)
admin.site.register(AddressOfDrugstore)
admin.site.register(OrderModel)
admin.site.register(StorageModel)
admin.site.register(DrugStore)
admin.site.register(Order)