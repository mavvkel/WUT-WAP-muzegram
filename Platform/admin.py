from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Profile, Post, Song, Radio


class ProfileInline(admin.StackedInline):
    model = Profile


class AdminUser(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, AdminUser)
admin.site.unregister(Group)

admin.site.register(Post)
admin.site.register(Song)
admin.site.register(Radio)
