from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id

            # Check if user has made inquiry already
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted.exists():
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)
        else:
            user_id = 0

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #     'traversy.brad@gmail.com',
        #     [realtor_email, 'techguyinfo@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)
    else:
        # Handle GET or other methods - redirect to listings page or show error
        messages.error(request, 'Invalid request method.')
        return redirect('listings')

