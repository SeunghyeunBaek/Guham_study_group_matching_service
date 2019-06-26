from django.contrib import admin
from .models import Post, HashTag
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        fields = ['id', 'user']


class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource


class HashTagResource(resources.ModelResource):
    class Meta:
        model = HashTag


class HashTagAdmin(ImportExportModelAdmin):
    resource_class = HashTagResource

admin.site.register(Post, PostAdmin)
admin.site.register(HashTag, HashTagAdmin)

# Register your models here.
