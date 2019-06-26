from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.


class UserResource(resources.ModelResource):

    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


admin.site.register(User, UserAdmin)

