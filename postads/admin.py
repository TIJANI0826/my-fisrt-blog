from django.contrib import admin

# Register your models here.
from .models import PostAd


class PostAdAdmin(admin.ModelAdmin):
    list_display = ("name","email","gist","category","location","description","expire")
    list_filter = ['email']
    search_fields = ['name']
    ordering = ["email","name","gist","category","location","description","expire"]



admin.site.register(PostAd,PostAdAdmin)

