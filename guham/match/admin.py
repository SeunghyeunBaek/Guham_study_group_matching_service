from django.contrib import admin
from .models import MatchPost, HashTag
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class MatchPostResource(resources.ModelResource):

    class Meta:
        model = MatchPost


class MatchPostAdmin(ImportExportModelAdmin):
    resource_class = MatchPostResource


# Register your models here.
admin.site.register(MatchPost, MatchPostAdmin)
admin.site.register(HashTag)
