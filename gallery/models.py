from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    image=models.ImageField(upload_to='artworks/')
    category=models.CharField(max_length=50,default='General 1')
    likes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Achievement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='achievements/')
    description = models.TextField()

    def __str__(self):
        return self.title  

  
class Commission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    art_type = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    details = models.TextField()
    reference_image = models.ImageField(upload_to='commissions/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.first_name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    
