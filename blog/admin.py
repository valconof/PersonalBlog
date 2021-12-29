from django.contrib import admin
from .models import Post, Comment, AdminInformation

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AdminInformation)