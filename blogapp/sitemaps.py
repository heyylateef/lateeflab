from django.contrib.sitemaps import Sitemap
from blogapp.models import Blogpost

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Blogpost.objects.filter(status="PUBLISH")
        # return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.updated_on