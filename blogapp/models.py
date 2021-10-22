from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
from django.urls import reverse

class Blogpost(models.Model):
    DRAFT = 'DRAFT'
    PUBLISH ='PUBLISH'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subheading = models.CharField(max_length=100, default="")
    cover_image = models.ImageField(upload_to='uploads/coverimages', default="uploads/blog1.jpg")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title

    def get_absolute_url(self): #Required to use sitemaps framework (good for SEO)
        return reverse("post_detail", kwargs={"slug": self.slug})
    