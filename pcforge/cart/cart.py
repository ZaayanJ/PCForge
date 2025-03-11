from shop.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #get key if exists
        cart = self.session.get('session_key')

        #if no key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make cart available on all pages
        self.cart = cart
    
    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True


    def total(self):
        #get product ids
        product_ids = self.cart.keys()
        #lookup keysin model
        products = Product.objects.filter(id__in=product_ids)
        #start total
        total = 0
        for product in products:
            total = total + float(product.price)

        return f"{total:.2f}"


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #use ids to loopup products in database model
        products = Product.objects.filter(id__in=product_ids)

        return products
