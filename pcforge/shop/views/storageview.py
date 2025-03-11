from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Storage

class StorageView(TemplateView):
    template_name = "shop/Product_Details_Storage.html"

    def get(self, request):
        storages = Storage.objects.select_related("prod_id").all()
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
                "productImage": storage.prod_id.mainImage
                } for storage in storages]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))