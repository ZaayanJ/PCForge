from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import CPUCooler

class CPUCoolersView(TemplateView):
    template_name = "shop/Product_Details_CPUCoolers.html"

    def get(self, request):
        cpucoolers = CPUCooler.objects.select_related("prod_id").all()
        context = {
            "cpucoolers": [{
                "id": cpucooler.prod_id.id,
                "coolerType": cpucooler.coolerType, 
                "fanSizeMM": cpucooler.fanSizeMM, 
                "rpm": cpucooler.rpm,
                "noiseLeveldBA": cpucooler.noiseLeveldBA,
                "tdpWatts": cpucooler.tdpWatts,
                "material": cpucooler.material,
                "socketCompatibility": cpucooler.socketCompatibility,
                "productName": cpucooler.prod_id.name, 
                "productPrice": cpucooler.prod_id.price, 
                "productImage": cpucooler.prod_id.mainImage
                } for cpucooler in cpucoolers]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))