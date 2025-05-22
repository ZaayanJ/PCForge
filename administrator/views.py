from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.utils.text import slugify
from django.db.models import Max
import shop.models 

# Create your views here.

def administrator_dashboard_view(request):

    user_class= get_user_model()

    current_user = request.user

    three_most_recent_users = user_class.objects.exclude(id=request.user.id).order_by('-date_joined')[:3]
    two_most_active_employees = shop.models.UserAnalytics.objects.filter(user__is_staff=True).select_related('user').order_by('-orders_finished')[:2]
    five_last_orders = shop.models.Order.objects.order_by("-orderId")[:5]
    employee_orders = shop.models.Order.objects.filter(employeeId=current_user).prefetch_related("orderitem_set")

    new_messages_count = shop.models.ContactInformation.objects.filter(status='new').count()

    return render(request, 'administrator_dashboard.html',{'user':current_user,'recent_orders':five_last_orders,'recent_employees':two_most_active_employees,'recent_users':three_most_recent_users,'claimed_orders':employee_orders, 'unread_messages':new_messages_count})



#
#
#

def user_management_view(request):

    user_class = get_user_model()

    if request.method == "POST":
        user_type = request.POST.get("user_classification")

        if user_type == "Customer":
            current_users = user_class.objects.filter(
                is_staff=False,
                is_superuser=False
            ).exclude(id=request.user.id).order_by('-date_joined')

        elif user_type == "Employee":
            current_users = user_class.objects.filter(
                is_staff=True,
                is_superuser=False
            ).exclude(id=request.user.id).order_by('-date_joined')

        elif user_type == "Admin":
            current_users = user_class.objects.filter(
                is_superuser=True
            ).exclude(id=request.user.id).order_by('-date_joined')

        elif user_type == "All":
            current_users = user_class.objects.all().exclude(id=request.user.id).order_by('-date_joined')

        else:
            current_users = user_class.objects.none()

        return render(request, 'user_management.html', {"current_users": current_users})

    # Default GET - show all except self
    current_users = user_class.objects.exclude(id=request.user.id).order_by('-date_joined')
    return render(request, 'user_management.html', {"current_users": current_users})

@csrf_protect
def create_user(request):
    if request.method == "POST":
        user_class = request.POST.get("user_classification")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_class_model = get_user_model()
        
        # Check user class to set appropriate flags
        is_staff = (user_class == "Employee" or user_class == "Admin")
        is_superuser = (user_class == "Admin")

        # Create the user
        user_class_model.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # hashes the password!
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        return redirect('user_management')  # or your actual view name

    return redirect('user_management')

@csrf_protect
def delete_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user_class = get_user_model()

        try:
            user = user_class.objects.get(id=user_id)
            user.delete()
        except user_class.DoesNotExist:
            pass  # silently fail or log

        return redirect('user_management')

    return redirect('user_management')

#
#
#

def product_management_view(request):

    all_products = shop.models.Product.objects.all()

    return render(request, 'product_management.html', {'products':all_products})

def product_information(request, slug):
    product = get_object_or_404(shop.models.Product, slug=slug)
    return render(request, 'product_information.html', {'product': product})

def add_product(request):
    if request.method == "POST":

        category_prefix = int(request.POST['category_prefix'])  # 1–9

        # Define min and max range for this category
        lower_bound = category_prefix * 10**7
        upper_bound = (category_prefix + 1) * 10**7 - 1

        # Get the current max ID in that range
        max_id = shop.models.Product.objects.filter(id__gte=lower_bound, id__lte=upper_bound).aggregate(Max('id'))['id__max']

        if max_id:
            new_id = max_id + 1
        else:
            new_id = lower_bound  # start fresh in this category


        name = request.POST['name']
        product = shop.models.Product.objects.create(
            id=new_id,
            name=name,
            slug=slugify(name),
            price=request.POST['price'],
            description=request.POST['description'],
            mainImage=request.POST['mainImage'],
            inventory=request.POST['inventory']
        )
    return redirect('product_management')

def edit_product(request, slug):
    product = get_object_or_404(shop.models.Product, slug=slug)
    if request.method == "POST":
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.mainImage = request.POST['mainImage']
        product.inventory = request.POST['inventory']
        product.save()
    return redirect('product_management')

def delete_product(request, slug):
    product = get_object_or_404(shop.models.Product, slug=slug)
    if request.method == "POST":
        product.delete()
    return redirect('product_management')

#
#
#

def admin_analytics_view(request):
    user_class = get_user_model()

    # 3 Most Active Users
    active_users = (
        shop.models.UserAnalytics.objects
        .filter(user__is_superuser=False)
        .select_related('user')
        .order_by('-login_count')[:3]
    )

    # 3 Most Productive Employees
    productive_employees = (
        shop.models.UserAnalytics.objects
        .filter(user__is_staff=True, user__is_superuser=False)
        .select_related('user')
        .order_by('-orders_worked_on')[:3]
    )

    # 5 Most Popular Products (timesOrdered already accounts for discontinued products too!)
    popular_products = (
        shop.models.Product.objects
        .order_by('-timesOrdered')[:5]
    )

    context = {
        'active_users': active_users,
        'productive_employees': productive_employees,
        'popular_products': popular_products
    }

    return render(request, 'admin_analytics.html', context)

#
#
#
#

def admin_contact_messages_view(request):
    if not request.user.is_superuser:
        return redirect('index')

    messages = shop.models.ContactInformation.objects.all().order_by('-created_at')  # assuming you have a timestamp field

    return render(request, 'contact_messages.html', {'messages': messages})


def view_contact_message(request, message_id):
    if not request.user.is_superuser:
        return redirect('index')

    message = get_object_or_404(shop.models.ContactInformation, id=message_id)

    # Mark as read if not already
    if message.status == 'new':
        message.status = 'read'
        message.save()

    return render(request, 'contact_messages_information.html', {'message': message})
