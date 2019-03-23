from django.contrib import admin
from .models import Feedback, PostForMovies, PostForBooks, Profile
# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


class PostForMandBAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(PostForMovies, PostForMandBAdmin)
admin.site.register(PostForBooks, PostForMandBAdmin)
admin.site.register(Profile, ProfileAdmin)


