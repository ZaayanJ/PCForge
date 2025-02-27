from django.urls import path
from shop.views.indexview import IndexView
from shop.views.aboutusview import AboutUsView
from shop.views.catalogview import CatalogView
from shop.views.catalogdetails import CatalogDetailsView
from shop.views.shoppingcartview import ShoppingCartView
from shop.views.zaayanview import ZaayanView
from shop.views.josueview import JosueView
from shop.views.evanview import EvanView
from shop.views.ethanview import EthanView
from shop.views.bobbyview import BobbyView
from shop.views.cpuview import CPUView
from shop.views.cpucoolersview import CPUCoolersView
from shop.views.motherboardview import MotherboardView
from shop.views.memoryview import MemoryView
from shop.views.storageview import StorageView
from shop.views.gpuview import GPUView
from shop.views.pccasesview import PCCasesView
from shop.views.psuview import PSUView
from shop.views.monitorsview import MonitorsView

urlpatterns = [
    path("monitors", MonitorsView.as_view(), name='monitors'),
    path("psu", PSUView.as_view(), name='psu'),
    path("pccases", PCCasesView.as_view(), name='pccases'),
    path("gpu", GPUView.as_view(), name='gpu'),
    path("storage", StorageView.as_view(), name='storage'),
    path("memory", MemoryView.as_view(), name='memory'),
    path("motherboard", MotherboardView.as_view(), name='motherboard'),
    path("cpucoolers", CPUCoolersView.as_view(), name='cpucoolers'),
    path("cpu", CPUView.as_view(), name='cpu'),
    path("bobby", BobbyView.as_view(), name='bobby'),
    path("ethan", EthanView.as_view(), name='ethan'),
    path("evan", EvanView.as_view(), name='evan'),
    path("josue", JosueView.as_view(), name='josue'),
    path("zaayan", ZaayanView.as_view(), name='zaayan'),
    path("shoppingcart", ShoppingCartView.as_view(), name='shoppingcart'),
    path("catalog", CatalogView.as_view(), name='catalog'),
    path("about-us", AboutUsView.as_view(), name='about-us'),
    path("", IndexView.as_view(), name="index"),
    path("catalog-details", CatalogDetailsView.as_view(), name="catalog-details")
]