from django.contrib import admin
from shop.models import Product
from shop.models import Image
from shop.models import CPU
from shop.models import Memory
from shop.models import GPU
from shop.models import Motherboard
from shop.models import CPUCooler
from shop.models import Storage
from shop.models import PCCase
from shop.models import PSU
from shop.models import Monitor
from shop.models import Customer
from shop.models import OrderObject
from shop.models import OrderListing

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(CPU)
admin.site.register(Memory)
admin.site.register(GPU)
admin.site.register(Motherboard)
admin.site.register(CPUCooler)
admin.site.register(Storage)
admin.site.register(PCCase)
admin.site.register(PSU)
admin.site.register(Monitor)
admin.site.register(Customer)
admin.site.register(OrderObject)
admin.site.register(OrderListing)