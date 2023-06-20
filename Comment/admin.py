from django.contrib import admin

# Register your models here.
from Comment.models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ( 'post',)
    
   