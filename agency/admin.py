from django.contrib import admin

from agency.models import SpyCat, Mission, Target

# Register your models here.

admin.site.register(SpyCat)
admin.site.register(Mission)
admin.site.register(Target)