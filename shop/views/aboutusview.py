from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

class AboutUsView(TemplateView):
    template_name = "shop/about-us.html"

    def get(self, request):
        products = Product.objects.order_by("name")
        context = {"products": [{"name": p.name, "price": p.price} for p in products]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))