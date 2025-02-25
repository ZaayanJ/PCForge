from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

class DatabaseTestingView(TemplateView):
    template_name = "shop/database_testing.html"

    def get(self, request):

        context = {
            "products": [
                {"name": p.name, "price": p.price, "image_url": p.mainImage or "missing.png"}
                for p in Product.objects.order_by("-price")
            ]
        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
