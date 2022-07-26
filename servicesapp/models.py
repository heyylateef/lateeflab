# from django.db import models
# from PIL import Image
# from django.conf import settings
# from django.urls import reverse
# from lateeflab.storage_backends import PrivateMediaStorage

# class Templatepackage(models.Model):
#     HTML = 'HTML'
#     PYTHON = 'PYTHON'
#     REACT = 'REACT'
#     JAVASCRIPT = 'JAVASCRIPT'
#     PLUGIN= 'PLUGIN'
#     WEBAPP = 'WEBAPP'

#     FILTER_TAG_CHOICES = [
#         (HTML, 'HTML'),
#         (PYTHON, 'Python'),
#         (REACT, 'React'),
#         (JAVASCRIPT, 'JavaScript'),
#         (PLUGIN, 'Plugin'),
#     ]

#     FILTER_TYPE_CHOICES = [
#         (WEBAPP, 'Web App'),
#         (PLUGIN, 'Plugin'),
#     ]

#     title = models.CharField(max_length=200, unique=True)
#     subheading = models.CharField(max_length=100, default="")
#     preview_image = models.ImageField(upload_to='uploads/previewimages', storage=PrivateMediaStorage(), default="")
#     package_files = models.FileField()
#     filter_tags = models.CharField(max_length=7, choices=FILTER_TAG_CHOICES, default=HTML)
#     filter_type = models.CharField(max_length=7, choices=FILTER_TYPE_CHOICES, default=WEBAPP)
#     description = models.TextField()
#     demo_url = models.URLField()
#     updated_on = models.DateTimeField(auto_now_add=True)
#     created_on = models.DateTimeField(auto_now_add=True)