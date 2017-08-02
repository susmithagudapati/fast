from django.contrib import admin
from . import models as core_models

class SubjectAdmin(admin.ModelAdmin):

	prepopulated_fields = {'slug': ('name',)}

admin.site.register(core_models.Subject, SubjectAdmin)

