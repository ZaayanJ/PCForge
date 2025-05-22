from django.urls import path
from . import views
# from administrator_dashboard_view import IndexView


urlpatterns = [
    path('', views.pcbuilder_view, name="pcbuilder"),
]