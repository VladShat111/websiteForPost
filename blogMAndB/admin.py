from django.contrib import admin
from .models import Feedback, PostForMovies, PostForBooks, Profile
# Register your models here.
admin.site.register(Feedback)
admin.site.register(PostForMovies)
admin.site.register(PostForBooks)
admin.site.register(Profile)


