from django.shortcuts import  render,get_object_or_404, redirect
from .models import Artwork
from .models import Achievement
from django.core.mail import EmailMessage
from .models import Contact
from django.core.mail import send_mail
from .models import Testimonial

def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'home.html', {'artworks': artworks})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def achievements(request):
    data = Achievement.objects.all()
    return render(request, 'achievements.html', {'data': data})

def gallery_view(request):
    artworks = Artwork.objects.all()
     # 🔍 SEARCH
    query = request.GET.get('q')
    if query:
        artworks = artworks.filter(title__icontains=query)

    # 🎨 CATEGORY FILTER
    category = request.GET.get('category')
    if category:
        artworks = artworks.filter(category=category)
    categories = Artwork.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'gallery.html', {
        'artworks': artworks,
        'categories': categories
    })
    
    


def like_artwork(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    artwork.likes += 1
    artwork.save()
    return redirect('gallery')  



def commission(request):
    if request.method == "POST":
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        art = request.POST.get('art_type')
        size = request.POST.get('size')
        details = request.POST.get('details')
        reference_image = request.FILES.get('reference_image')

        # 🔥 SAVE TO DATABASE
        commission.objects.create(
            first_name=first,
            last_name=last,
            phone=phone,
            email=email,
            art_type=art,
            size=size,
            details=details,
            reference_image=reference_image
        )


        # -------- EMAIL TO YOU --------
        message = f"""
New Commission Order:

Name: {first} {last}
Phone: {phone}
Email: {email}
Artwork Type: {art}
Size: {size}
Details: {details}
"""

        admin_email = EmailMessage(
            'New Commission Order',
            message,
            'YOUR_GMAIL@gmail.com',   # 👈 yaha apna email daalo
            ['YOUR_GMAIL@gmail.com'],
        )

        if reference_image:
            admin_email.attach(
                reference_image.name,
                reference_image.read(),
                reference_image.content_type
            )

        admin_email.send()

        # -------- AUTO REPLY TO USER --------
        reply_message = f"""
Hi {first},

Thank you for your commission request 🎨

I’ve received your order and will contact you soon to discuss pricing and details.

For faster response, you can also reach me here:
👉 Instagram: https://instagram.com/artofshree9
👉 WhatsApp: (your number)

Regards,
Shrishti Pal
ArtOfShree
"""

        user_email = EmailMessage(
            'Your Commission Request Received',
            reply_message,
            'YOUR_GMAIL@gmail.com',   # 👈 same email
            [email],                  # 👈 user ka email
        )

        user_email.send()

        return render(request, 'success.html')

    return render(request, 'commission.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # ✅ Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # ✅ Send email
        send_mail(
            "New Contact Message",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            "your_email@gmail.com",
            ["your_email@gmail.com"],
            fail_silently=False,
        )

        return render(request, 'success.html')

    return render(request, 'contact.html')

from .models import Testimonial

def testimonials(request):
    data = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'testimonials.html', {'data': data})


def add_testimonial(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        Testimonial.objects.create(
            name=name,
            message=message,
            rating=rating
        )

        return redirect('testimonials')

    return render(request, 'add_testimonial.html')