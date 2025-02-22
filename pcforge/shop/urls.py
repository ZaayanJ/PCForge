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

urlpatterns = [
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