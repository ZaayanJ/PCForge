from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from django.contrib import messages
from shop.models import *
from django.http import JsonResponse

# Create your views here.

def process_order(request):
    if request.POST:

        cart = Cart(request)
        cart_products = cart.get_prods
        totals = cart.total()

        user = request.user

        #create an order
        create_order = Order(userId=user,totalPrice = totals,status="processing")
        create_order.save()

        #add order items
        #get orderID
        order_id = create_order
        #get prod info
        for product in cart_products():
            product_id = product
            price = product.price

            create_order_item = OrderItem(orderId=order_id, productId=product_id,user=user,price=price)

            create_order_item.save()


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
    cart_products = cart.get_prods
    totals = cart.total()

    return render(request, "ShoppingCart.html", {"cart_products": cart_products, "totals":totals})

def cart_add(request):
    #get cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #get item added
        product_id = int(request.POST.get('product_id'))

        #get product in database
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product)

        cart_quantity = cart.__len__()

        #return response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    totals = cart.total()

    return render(request, "checkout.html", {"cart_products": cart_products, "totals":totals})

# def cart_delete(request):
#     return render(request, "cart_summary.html")

# def cart_update(request):
#     return render(request, "cart_summary.html")