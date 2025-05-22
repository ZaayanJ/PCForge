from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import ContactInformation

@login_required
def contact_us(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.user.email  # Get user's email
        user = request.user

        if subject and message:
            ContactInformation.objects.create(
                user=user,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')  # Redirect to avoid form resubmission
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'shop/contact-us-page.html')  # Adjust path if needed
