from django.contrib import admin
from .models import course,topic,subtopics,subtopics_info

# Register your models here.
#for admin access database(AKA super user access)
admin.site.register(course)
admin.site.register(topic)
admin.site.register(subtopics)
admin.site.register(subtopics_info)
