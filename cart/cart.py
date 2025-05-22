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
    
    # def add(self, product):
    #     product_id = str(product.id)

    #     if product_id in self.cart:
    #         pass
    #     else:
    #         self.cart[product_id] = {'price': str(product.price)}

    #     self.session.modified = True

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': quantity
            }

        self.session.modified = True



    def total(self):
        #get product ids
        product_ids = self.cart.keys()
        #lookup keysin model
        products = Product.objects.filter(id__in=product_ids)
        #start total
        total = 0
        for product in products:
            item = self.cart[str(product.id)]
            total += float(product.price) * item['quantity']


        return total


    # def __len__(self):
    #     return len(self.cart)

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    
    def get_prods(self):
        # Convert string keys to int before querying
        product_ids = [int(pid) for pid in self.cart.keys()]
        products = Product.objects.filter(id__in=product_ids)

        cart_items = []
        for product in products:
            key = str(product.id)  # use str key to get from session
            item = self.cart.get(key)
            if item:
                cart_items.append({
                    'product': product,
                    'quantity': item['quantity'],
                    'total_price': float(product.price) * item['quantity']
                })

        return cart_items


