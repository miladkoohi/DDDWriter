from django.contrib import admin
from blog.infrastructure.database.models import BlogPostModel

@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
