from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from shop.models import Product
from shop.models import Customer
from shop.models import OrderObject
from shop.models import OrderListing

class ProfilePageView(TemplateView):
    template_name = "shop/profile_page.html"

    def get(self, request):

        context = {
            "products": [
                {"name": p.name,
                 "price": p.price,
                 "image_url": p.mainImage or "missing.png"}
                for p in Product.objects.order_by("-price")
            ]
            ,

            # "user": Customer.objects.all()

            # "orderObjects": [
            #     {"orderId": o.id,
            #      "timestamp": o.timestamp,
            #      "totalPrice": o.totalPrice,
            #      "status": o.status}
            #      for o in OrderObject.objects.filter(user=request.user.id)
            # ]

        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))