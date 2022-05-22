from email.headerregistry import Group
from django.contrib import admin
from MagazineApp.models import *
from django.contrib.auth.models import Group

from django.utils.html import format_html

admin.site.site_header = 'MFAH Admin'
admin.site.unregister(Group)

# Register your models here.
class MagazineCategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryName', 'image_tag', 'color_tag', )
    readonly_fields = ['image_tag', 'color_tag']
    

    
admin.site.register(MagazineCategory, MagazineCategoryAdmin)
admin.site.register(MagazineDetails)
admin.site.register(MegazinePages)
