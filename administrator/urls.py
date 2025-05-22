from django.urls import path
from . import views
# from administrator_dashboard_view import IndexView


urlpatterns = [
    path('', views.administrator_dashboard_view, name="administrator_dashboard"),
    # path('orders_dashboard/', views.orders_dashboard_view, name="orders_dashboard"),
    path('product_management/', views.product_management_view, name="product_management"),
    path('user_management/', views.user_management_view, name="user_management"),
    path('create_user', views.create_user, name="create_user"),
    path('delete_user', views.delete_user, name="delete_user"),
    path('products/<slug:slug>/', views.product_information, name='product_information'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<slug:slug>/', views.edit_product, name='edit_product'),
    path('delete/<slug:slug>/', views.delete_product, name='delete_product'),
    path('analytics/', views.admin_analytics_view, name="analytics"),
    path('contact-messages/', views.admin_contact_messages_view, name='contact_messages'),
    path('contact-messages-detail/<int:message_id>/', views.view_contact_message, name="view_contact_message")


]