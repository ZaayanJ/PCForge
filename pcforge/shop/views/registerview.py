# from django.views.generic import TemplateView
# from django.http import HttpResponse
# from django.template import loader
# from shop.models import Product

# class RegisterView(TemplateView):
#     template_name = "shop/registration.html"

#     def get(self, request):
#         context = {}
#         template = loader.get_template(self.template_name)
#         return HttpResponse(template.render(context, request))

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib import messages

User = get_user_model()  # This ensures you use the CustomUser model if you've extended it

class RegisterView(TemplateView):
    template_name = "shop/registration.html"

    def get(self, request):
        context = {}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))

    def post(self, request):
        """Handles user input from the registration form."""
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")  # Redirect back to the registration page

        # Create and save the user
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # Hash the password before saving
        )
        user.save()

        messages.success(request, "User registered successfully! You can now log in.")
        return redirect("login")