from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import CPU

class CPUView(TemplateView):
    template_name = "shop/Product_Details_CPU.html"

    def get(self, request):
        cpus = CPU.objects.select_related("prod_id").all()
        context = {"cpus": [{
            "core": cpu.coreCount, 
            "coreClock": cpu.baseClockSpeedGHz, 
            "boostClock": cpu.boostClockSpeedGHz, 
            "microArch": cpu.microArch, 
            "productName": cpu.prod_id.name, 
            "productPrice": cpu.prod_id.price, 
            "productImage": cpu.prod_id.mainImage
            } for cpu in cpus]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))