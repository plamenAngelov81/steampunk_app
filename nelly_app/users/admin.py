from django.contrib import admin

from nelly_app.users.models import UserProfile


@admin.register(UserProfile)
class Profile(admin.ModelAdmin):
    pass
