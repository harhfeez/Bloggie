from django.contrib import admin
from Post.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','create_on','status',]
    list_filter = ['status']
    search_Field = ['title', 'content']

admin.site.register(Post, PostAdmin)