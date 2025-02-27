from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import PSU

class PSUView(TemplateView):
    template_name = "shop/Product_Details_PSU.html"

    def get(self, request):
        psus = PSU.objects.select_related("prod_id").all()
        context = {
            "psus": [{
                "wattage": psu.wattage,
                "efficiencyRating": psu.efficiencyRating,
                "formFactor": psu.formFactor,
                "modularity": psu.modularity,
                "fanSizeMM": psu.fanSizeMM,
                "protections": psu.protections,
                "productName": psu.prod_id.name, 
                "productPrice": psu.prod_id.price, 
                "productImage": psu.prod_id.mainImage
                } for psu in psus]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))