from django.contrib import admin
from shop.models import Product
from shop.models import Image
from shop.models import CPU
from shop.models import Memory
from shop.models import GPU
from shop.models import Motherboard

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(CPU)
admin.site.register(Memory)
admin.site.register(GPU)
admin.site.register(Motherboard)