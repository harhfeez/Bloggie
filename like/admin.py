from django.contrib import admin
from .models import Like

# Register your models here.


class LikeAdmin(admin.ModelAdmin):

    list_display = ("id",)


admin.site.register(Like, LikeAdmin)