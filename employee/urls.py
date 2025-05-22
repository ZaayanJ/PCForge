from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_dashboard, name="employee_dashboard"),
    path('employee_profile', views.employee_profile, name="employee_profile"),
    path('claim_order/', views.claim_order, name="claim_order"),
    path('manage_order_status', views.manage_order_status, name="manage_order_status")
    # path('checkout/', views.checkout, name="checkout"),
]