from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Storage

class StorageView(TemplateView):
    template_name = "shop/Product_Details_Storage.html"

    def get(self, request):
        storages = Storage.objects.select_related("prod_id").all()

                # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            storages = storages.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                storages = storages.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = Storage.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

        context = {
            "storages": [{
                "id":storage.prod_id.id,
                "storageType": storage.storageType,
                "capacityGB": storage.capacityGB,
                "interface": storage.interface,
                "formFactor": storage.formFactor,
                "nandType": storage.nandType,
                "productName": storage.prod_id.name, 
                "productPrice": storage.prod_id.price, 
                "productImage": storage.prod_id.mainImage,
                "inventory": storage.prod_id.inventory
                } for storage in storages],
                "manufacturers":manufacturers}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))