from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from shop.models import Product
# from shop.models import Customer
# from shop.models import User
from shop.models import Order
from shop.models import OrderItem

class ProfilePageView(TemplateView):
    template_name = "shop/profile.html"

    def get(self, request):

        current_user = request.user

        user_orders = Order.objects.filter(userId=current_user).prefetch_related("orderitem_set")


        # user_order_items = OrderItem.objects.filter(orderId__in=user_orders)

        context = {
            # "products": [
            #     {"name": p.name,
            #      "price": p.price,
            #      "image_url": p.mainImage or "missing.png"}
            #     for p in Product.objects.order_by("-price")
            # ]
            # ,

            "user": current_user,

            "orders": user_orders,

            # "order_items": user_order_items,

        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))