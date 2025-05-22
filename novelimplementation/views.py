from django.shortcuts import render
from shop.models import Product
from shop.models import CPU, Memory, GPU, Motherboard, CPUCooler, Storage, PCCase, PSU, Monitor
from django.core.serializers import serialize
from django.http import JsonResponse
import json

# Create your views here.

def pcbuilder_view(request):

    cpus = CPU.objects.select_related("prod_id").all()
    memory = Memory.objects.select_related("prod_id").all()
    gpus = GPU.objects.select_related("prod_id").all()
    motherboards = Motherboard.objects.select_related("prod_id").all()
    cpucoolers = CPUCooler.objects.select_related("prod_id").all()
    psus = PSU.objects.select_related("prod_id").all()
    storage = Storage.objects.select_related("prod_id").all()
    pccases = PCCase.objects.select_related("prod_id").all()
    monitor = Monitor.objects.select_related("prod_id").all()

    # Build incompatibility map: { product_id: [list_of_incompatible_ids] }
    incompat_map = {}
    name_map = {}
    for product in Product.objects.prefetch_related('incompatibilities').all():
        incompat_map[product.id] = list(product.incompatibilities.values_list('id', flat=True))
        name_map[product.id] = product.name


    return render(request, 'pcbuilder.html', {'cpus': cpus,
                                                'memory': memory,
                                                'gpus': gpus,
                                                'motherboards': motherboards,
                                                'cpucoolers': cpucoolers,
                                                'psus': psus,
                                                'storage': storage,
                                                'pccases': pccases,
                                                'monitors': monitor,
                                                'incompatibilities_json': json.dumps(incompat_map),
                                                'name_map_json': json.dumps(name_map)})
