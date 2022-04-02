from django.contrib import admin
from .models import Blogpost
from django_summernote.admin import SummernoteModelAdmin

# class BlogpostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status','created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
class BlogpostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'updated_on', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blogpost, BlogpostAdmin)
