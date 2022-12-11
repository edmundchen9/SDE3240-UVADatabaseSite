from django.contrib import admin
from .models import myUser, course, department
# Register your models here.

admin.site.register(myUser)
admin.site.register(course)
admin.site.register(department)