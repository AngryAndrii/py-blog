from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from blog.models import Commentary, Post

admin.site.unregister(Group)

admin.site.register(get_user_model())
admin.site.register(Commentary)
admin.site.register(Post)