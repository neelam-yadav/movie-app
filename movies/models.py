from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=140)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='posters')
    director = models.CharField(max_length=140)
    created_date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=140)

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
