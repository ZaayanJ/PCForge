# from django.views.generic import TemplateView
# from django.http import HttpResponse
# from django.template import loader

# from shop.models import Product
# # from shop.models import Customer
# # from shop.models import User
# from shop.models import Order
# from shop.models import OrderItem

# class EmployeeProfilePageView(TemplateView):
#     template_name = "shop/employee_profile.html"

#     def get(self, request):

#         current_user = request.user

#         employee_orders = Order.objects.filter(employeeId=current_user).prefetch_related("orderitem_set")


#         # user_order_items = OrderItem.objects.filter(orderId__in=user_orders)

#         context = {
#             "user": current_user,

#             "orders": employee_orders,
#         }

#         template = loader.get_template(self.template_name)
#         return HttpResponse(template.render(context, request))