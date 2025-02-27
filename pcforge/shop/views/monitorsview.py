from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Monitor

class MonitorsView(TemplateView):
    template_name = "shop/Product_Details_Monitors.html"

    def get(self, request):
        monitors = Monitor.objects.select_related("prod_id").all()
        context = {
            "monitors": [{
                "screenSizeInches": monitor.screenSizeInches, 
                "resolution": monitor.resolution, 
                "refreshRateHz": monitor.refreshRateHz,
                "responseTimeMS": monitor.responseTimeMS,
                "panelType": monitor.panelType,
                "aspectRatio": monitor.aspectRatio,
                "ports": monitor.ports,
                "productName": monitor.prod_id.name, 
                "productPrice": monitor.prod_id.price, 
                "productImage": monitor.prod_id.mainImage
                } for monitor in monitors]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))