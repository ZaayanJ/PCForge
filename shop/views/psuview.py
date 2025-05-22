from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import PSU

class PSUView(TemplateView):
    template_name = "shop/Product_Details_PSU.html"

    def get(self, request):
        psus = PSU.objects.select_related("prod_id").all()

                # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            psus = psus.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                psus = psus.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = PSU.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

        context = {
            "psus": [{
                "id":psu.prod_id.id,
                "wattage": psu.wattage,
                "efficiencyRating": psu.efficiencyRating,
                "formFactor": psu.formFactor,
                "modularity": psu.modularity,
                "fanSizeMM": psu.fanSizeMM,
                "protections": psu.protections,
                "productName": psu.prod_id.name, 
                "productPrice": psu.prod_id.price, 
                "productImage": psu.prod_id.mainImage,
                "inventory": psu.prod_id.inventory
                } for psu in psus],
                "manufacturers":manufacturers}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))