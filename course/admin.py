from django.contrib import admin
from .models import Person, Course, Membership

admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Membership)
