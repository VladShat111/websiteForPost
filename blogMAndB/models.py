from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    pub_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class PostForMovies(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    pub_date = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_movies', kwargs={'pk': self.pk})


class PostForBooks(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    pub_date = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_books', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='images_profile', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)

