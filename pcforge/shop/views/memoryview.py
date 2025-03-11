from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Memory

class MemoryView(TemplateView):
    template_name = "shop/Product_Details_Memory.html"

    def get(self, request):
        memory_items = Memory.objects.select_related("prod_id").all()
        
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
                "productImage": memory.prod_id.mainImage
            })
        
        context = {
            "memory": memory_list
        }
        
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))