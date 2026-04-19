from django.contrib import admin
from .models import Artwork,Achievement,Commission
from .models import Contact
from .models import Testimonial

admin.site.register(Artwork)
admin.site.register(Achievement)
admin.site.register(Commission)

admin.site.register(Contact)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','rating','created_at')
    search_fields = ('name',)



