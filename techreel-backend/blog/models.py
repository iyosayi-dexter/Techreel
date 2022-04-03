from django.db import models
from authors.models import Author
from django.contrib.postgres.fields import ArrayField
from django.template.defaultfilters import slugify
from django.urls import reverse


class TagChoices(models.TextChoices):
    TECH = 'tech'
    COMPUTERS = 'computers'
    PHONES = 'phones'
    EARNING = 'earning'
    PROGRAMMING = 'programming'
    REVIEWS = 'reviews'
    DEV = 'dev'
    Gadgets = 'gadgets'

# Create your models here.


class BlogPost (models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='author')
    title = models.CharField(max_length=200)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField()
    tags = ArrayField(models.CharField(
        max_length=30, choices=TagChoices.choices, default=TagChoices.TECH))
    thumbnail = models.ImageField(
        upload_to='thumbnails', null=True, blank=True)
    exert = models.TextField()
    content = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # unique slugs for each post
        slug = slugify(self.title)
        self.slug = slug

        # featured post max 3
        if self.featured:
            queryset = BlogPost.objects.filter(
                featured=True).order_by('date_created')
            if self in queryset or len(queryset) < 3:
                pass
            elif len(queryset) >= 3:
                queryset[0].featured = False
                queryset[0].save()

        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'

    def __str__(self):
        return self.title
