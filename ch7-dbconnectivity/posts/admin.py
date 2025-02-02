from django.contrib import admin

# Register your models here.
from .models import Post, Employees

admin.site.register(Post)
admin.site.register(Employees)
