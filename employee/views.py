from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Order,OrderItem,UserAnalytics
from django.contrib.auth import get_user_model

# Create your views here.

def employee_dashboard(request):

    orders = Order.objects.filter(status='placed').prefetch_related("orderitem_set")

    return render(request, 'employee/employee_dashboard.html',{"orders":orders})

def employee_profile(request):

    current_user = request.user

    employee_orders = Order.objects.filter(employeeId=current_user).prefetch_related("orderitem_set")

    context = {
            "user": current_user,

            "orders": employee_orders,
        }

    return render(request, 'employee/employee_profile.html',context)

def claim_order(request):
    if request.POST:
        employee = request.user

        order_id = request.POST.get("order_id")
        order = get_object_or_404(Order, orderId=order_id)

        if order.status == Order.Status.PLACED:
            order.employeeId = employee
            order.status = Order.Status.CLAIMED
            order.save()

    return redirect('employee_dashboard')


def manage_order_status(request):

    if request.POST:
        employee = request.user

        order_id = request.POST.get("order_id")
        order = get_object_or_404(Order, orderId=order_id)

        new_status = request.POST.get("order_status_change")

        # Assign employee and change status
        if new_status and new_status not in ["finished", "removed"]:
            order.employeeId = employee
            order.status = new_status
            order.save()

            # Increment orders_worked_on
            analytics, created = UserAnalytics.objects.get_or_create(user=employee)
            analytics.orders_worked_on += 1
            analytics.save()

        elif new_status == "removed":
            order.employeeId = None
            order.status = Order.Status.PLACED
            order.save()

            return redirect('employee_dashboard')

        else:
            # "finished" case
            previous_employee = order.employeeId  # Might be the current user or another employee

            order.employeeId = None
            order.status = new_status
            order.save()

            if previous_employee:
                analytics, created = UserAnalytics.objects.get_or_create(user=previous_employee)
                analytics.orders_finished += 1
                analytics.save()

            return redirect('employee_dashboard')


    return redirect('employee_profile')

