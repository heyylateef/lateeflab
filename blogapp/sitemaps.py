from django.contrib.sitemaps import Sitemap
from blogapp.models import Blogpost

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blogpost.objects.filter(status="PUBLISH")
        # return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.created_on