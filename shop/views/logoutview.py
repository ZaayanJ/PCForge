from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages

class LogoutView(View):
    """Handles user logout and redirects to the index page"""

    def get(self, request):
        logout(request)  # Logs the user out
        messages.success(request, "You have been logged out")
        return redirect("index")  # Redirect to home page
