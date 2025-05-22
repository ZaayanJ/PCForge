from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Monitor

class MonitorsView(TemplateView):
    template_name = "shop/Product_Details_Monitors.html"

    def get(self, request):
        monitors = Monitor.objects.select_related("prod_id").all()

                # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            monitors = monitors.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                monitors = monitors.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = Monitor.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

        context = {
            "monitors": [{
                "id": monitor.prod_id.id,
                "screenSizeInches": monitor.screenSizeInches, 
                "resolution": monitor.resolution, 
                "refreshRateHz": monitor.refreshRateHz,
                "responseTimeMS": monitor.responseTimeMS,
                "panelType": monitor.panelType,
                "aspectRatio": monitor.aspectRatio,
                "ports": monitor.ports,
                "productName": monitor.prod_id.name, 
                "productPrice": monitor.prod_id.price, 
                "productImage": monitor.prod_id.mainImage,
                "inventory": monitor.prod_id.inventory
                } for monitor in monitors],
                "manufacturers":manufacturers}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))