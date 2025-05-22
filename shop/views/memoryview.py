from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Memory

class MemoryView(TemplateView):
    template_name = "shop/Product_Details_Memory.html"

    def get(self, request):
        memory_items = Memory.objects.select_related("prod_id").all()

                # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            memory_items = memory_items.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                memory_items = memory_items.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = Memory.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()
        
        # Create a list of memory dictionaries
        memory_list = []
        for memory in memory_items:
            memory_list.append({
                "id":memory.prod_id.id,
                "memoryType": memory.memoryType, 
                "speedMHz": memory.speedMHz,
                # Remove this line - memoryGB is not in your model
                # "memoryGB": memory.memoryGB,
                "capacityGB": memory.capacityGB,
                "casLatency": memory.casLatency,
                "modules": memory.modules,
                "printedCircuitBoard": memory.printedCircuitBoard,
                "chips": memory.chips,
                "heatsink": memory.heatsink,
                "productName": memory.prod_id.name, 
                "productPrice": memory.prod_id.price, 
                "productImage": memory.prod_id.mainImage,
                "inventory": memory.prod_id.inventory
            })
        
        context = {
            "memory": memory_list,
            "manufacturers":manufacturers
        }
        
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))