from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Motherboard

class MotherboardView(TemplateView):
    template_name = "shop/Product_Details_Motherboard.html"

    def get(self, request):
        motherboards = Motherboard.objects.select_related("prod_id").all()
        context = {
            "motherboards": [{
                "id": motherboard.prod_id.id,
                "socket": motherboard.socket, 
                "chipset": motherboard.chipset,
                "formFactor": motherboard.formFactor,
                "maxMemoryGB": motherboard.maxMemoryGB,
                "maxMemorySlots": motherboard.maxMemorySlots,
                "printedCircuitBoard": motherboard.printedCircuitBoard,
                "voltageRegulator": motherboard.voltageRegulator,
                "productName": motherboard.prod_id.name, 
                "productPrice": motherboard.prod_id.price, 
                "productImage": motherboard.prod_id.mainImage
                } for motherboard in motherboards]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))