from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import GPU

class GPUView(TemplateView):
    template_name = "shop/Product_Details_GPU.html"

    def get(self, request):
        gpus = GPU.objects.select_related("prod_id").all()
        context = {
            "gpus": [{
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
                "productImage": gpu.prod_id.mainImage
                } for gpu in gpus]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))