from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import GPU

class GPUView(TemplateView):
    template_name = "shop/Product_Details_GPU.html"

    def get(self, request):
        gpus = GPU.objects.select_related("prod_id").all()

        # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            gpus = gpus.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                gpus = gpus.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = GPU.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

        context = {
            "gpus": [{
                "id": gpu.prod_id.id,
                "chipset": gpu.chipset, 
                "memoryType": gpu.memoryType, 
                "memoryGB": gpu.memoryGB, 
                "baseClockSpeedGHz": gpu.baseClockSpeedGHz, 
                "boostClockSpeedGHz": gpu.boostClockSpeedGHz, 
                "lengthMM": gpu.lengthMM, 
                "widthMM": gpu.widthMM,
                "gpuChip": gpu.gpuChip,
                "vramType": gpu.vramType,
                "vramGB": gpu.vramGB,
                "productName": gpu.prod_id.name, 
                "productPrice": gpu.prod_id.price, 
                "productImage": gpu.prod_id.mainImage,
                "inventory": gpu.prod_id.inventory
                } for gpu in gpus],
                "manufacturers":manufacturers}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))