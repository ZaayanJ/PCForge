from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import CPU

class CatalogDetailsView(TemplateView):
    template_name = "shop/Product_Details_CPU.html"

    def get(self, request):
        products = CPU.objects.all()
        context = {"products": [{"cores": p.coreCount, "base": p.baseClockSpeedGHz} for p in products]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
