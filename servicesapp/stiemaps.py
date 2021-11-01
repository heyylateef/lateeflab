from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'services_ecommerce', 'services_api', 'contact', 'privacypolicy', 'termsandconditions']

    def location(self, item):
        return reverse(item)