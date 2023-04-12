from django.contrib import admin
from .models import Language


class LanguageAdmin(admin.ModelAdmin):
    list = ('name', 'paradigm', 'author')

    admin.site.register(Language)
