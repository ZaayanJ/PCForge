from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product,UserAnalytics
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

class LoginView(TemplateView):
    template_name = "shop/login.html"

    def get(self, request):
        context = {}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
    def post(self, request):
        """Handles user authentication and login"""
        username = request.POST.get("username")
        # email = request.POST.get("email")  # Note: Django's authenticate() does not use email
        password = request.POST.get("password")

        # Authenticate using username & password (Django's default behavior)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "You have been logged in")

            analytics, created = UserAnalytics.objects.get_or_create(user=user)
            analytics.login_count += 1
            analytics.save()

            if user.is_superuser:
                #this is where it should go when implemented
                return redirect("administrator_dashboard")
                # return redirect("employee_profile")
            elif user.is_staff:
                return redirect("employee_dashboard")
            else:
                return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")