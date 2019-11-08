from django.contrib import admin
from .models import Feedback, PostForMovies, PostForBooks, Profile, CommentForBook, CommentForMovie
# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


@admin.register(PostForMovies, PostForBooks)
class PostForMandBAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')


@admin.register(CommentForBook, CommentForMovie)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'pub_date')


