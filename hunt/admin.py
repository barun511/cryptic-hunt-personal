from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Level, Submission, AppVariable


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(Level)
admin.site.register(User, UserAdmin)
admin.site.register(Submission)
admin.site.register(AppVariable)
