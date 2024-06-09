from django.contrib import admin

from .models import FAQ,Course,Enrollment
admin.site.register(FAQ)
admin.site.register(Course)
admin.site.register(Enrollment)