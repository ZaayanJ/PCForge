from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Motherboard

class MotherboardView(TemplateView):
    template_name = "shop/Product_Details_Motherboard.html"

    def get(self, request):
        motherboards = Motherboard.objects.select_related("prod_id").all()

                # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            motherboards = motherboards.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                motherboards = motherboards.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = Motherboard.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

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
                "productImage": motherboard.prod_id.mainImage,
                "inventory": motherboard.prod_id.inventory
                } for motherboard in motherboards],
                "manufacturers":manufacturers}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))