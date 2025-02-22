from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

class IndexView(TemplateView):
    template_name = "shop/index.html"

    def get(self, request):
        products = Product.objects.order_by("name")
        context = {"products": [{"name": products[0].name, "price": products[0].price, "description": products[0].description}]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))