from django.contrib import admin

# Register your models here.
from todo.models import Todo, Tag

admin.site.register(Todo)
admin.site.register(Tag)
