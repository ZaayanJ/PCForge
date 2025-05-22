from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import CPU

class CPUView(TemplateView):
    template_name = "shop/Product_Details_CPU.html"

    def get(self, request):
        cpus = CPU.objects.select_related("prod_id").all()

        # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            cpus = cpus.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                cpus = cpus.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = CPU.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

        context = {
            "cpus": [{
                "id": cpu.prod_id.id,
                "core": cpu.coreCount,
                "coreClock": cpu.baseClockSpeedGHz,
                "boostClock": cpu.boostClockSpeedGHz,
                "microArch": cpu.microArch,
                "productName": cpu.prod_id.name,
                "productPrice": cpu.prod_id.price,
                "productImage": cpu.prod_id.mainImage,
                "manufacturer": cpu.prod_id.manufacturer,
                "inventory": cpu.prod_id.inventory
            } for cpu in cpus],
            "manufacturers": manufacturers
        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))