from django.contrib import admin
from .models import Post


# Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = (
        'title', 'content', 'date', 'author'
    )
    list_filter = (
        'author', 'date'
    )


"""
Django Forms
    - forms
    - ModelForms ---

    Model ---> Forms.py ---> views.py
    CRUD - CREATE, READ, UPDATE, DELETE
Template inheritance





"""