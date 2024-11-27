from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #the same name as the model
    readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Book,BookAdmin)