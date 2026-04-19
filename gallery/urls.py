from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('achievements/',views.achievements),
    path('gallery/',views.gallery_view,name='gallery'),
    path('like/<int:id>/', views.like_artwork, name='like_artwork'),
    path('commission/',views.commission, name='commission'),
    path('contact/',views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('add-review/', views.add_testimonial, name='add_testimonial'),

]