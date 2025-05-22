from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from django.contrib import messages
from shop.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import traceback

# Create your views here.

def process_order(request):
    if request.POST:

        cart = Cart(request)
        cart_products = cart.get_prods()

        totals = cart.total()

        user = request.user
        employee_id = None

        #create an order
        create_order = Order(userId=user, employeeId =employee_id, totalPrice = totals,status="placed")
        create_order.save()

        #add order items
        #get orderID
        order_id = create_order
        #get prod info
        # for product in cart_products():
        #     product_id = product
        #     price = product.price

        #     create_order_item = OrderItem(orderId=order_id, productId=product_id,user=user,price=price)

        #     create_order_item.save()
        for item in cart_products:
            product = item['product']
            quantity = item['quantity']
            price = item['total_price']

            create_order_item = OrderItem(
                orderId=order_id,
                productId=product,
                user=user,
                price=price,
                quantity=quantity
            )
            create_order_item.save()

            product.timesOrdered += quantity
            product.inventory -= quantity

            product.save()



        for key in list(request.session.keys()):
            if key == "session_key":

                del request.session[key]

        messages.success(request, "Order Placed!")



        return redirect('index')
    else:
        messages.error(request, "oops")
        return redirect('index')


def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_prods()
    totals = cart.total()

    return render(request, "ShoppingCart.html", {"cart_products": cart_products, "totals":totals})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        try:
            raw_id = request.POST.get('product_id')
            if not raw_id:
                raise ValueError("No product_id provided")

            product_id = int(raw_id)
            quantity = int(request.POST.get('quantity', 1))

            print(f"🧪 Received add-to-cart for product ID {product_id}, quantity {quantity}")

            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product, quantity=quantity)

            print(f"✅ Added to cart: {product.name}")
            print(f"🛒 Cart now contains: {cart.cart}")

            cart_quantity = cart.__len__()
            return JsonResponse({'qty': cart_quantity})

        except Exception as e:
            print("❌ Error in cart_add view:")
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    totals = cart.total()

    if cart.__len__() == 0:
        return redirect('catalog')

    return render(request, "checkout.html", {"cart_products": cart_products, "totals":totals})

def cart_add_bulk(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        try:
            product_ids = json.loads(request.POST.get('product_ids', '[]'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid product list'}, status=400)

        for product_id in product_ids:
            product = get_object_or_404(Product, id=int(product_id))
            cart.add(product=product, quantity=1)

        return JsonResponse({'qty': cart.__len__()})

# def cart_delete(request):
#     return render(request, "cart_summary.html")

# def cart_update(request):
#     return render(request, "cart_summary.html")