from django.contrib import admin
from . models import Product, SocialMedia, CompanyInfo

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'activity',)   
    
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo',)    