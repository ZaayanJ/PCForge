from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import CPUCooler

class CPUCoolersView(TemplateView):
    template_name = "shop/Product_Details_CPUCoolers.html"

    def get(self, request):
        cpucoolers = CPUCooler.objects.select_related("prod_id").all()

            # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            cpucoolers = cpucoolers.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                cpucoolers = cpucoolers.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = CPUCooler.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

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
                "productImage": cpucooler.prod_id.mainImage,
                "inventory": cpucooler.prod_id.inventory
                } for cpucooler in cpucoolers],
                "manufacturers": manufacturers
                }
        
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))