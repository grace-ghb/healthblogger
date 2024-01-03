from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# Post inherit from Model.
# Title is an attribute


class Post(models.Model):
    title_post = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt_post = models.CharField(max_length=300, null=True, blank=True)
    blog_content = models.TextField(null=True, blank=True)
    # Print everytimes updated.
    updated = models.DateTimeField(auto_now=True)
    # Only print once initial time.
    created = models.DateTimeField(auto_now_add=True)
    # Refer to STATUS at above.
    status = models.IntegerField(choices=STATUS, default=0)
    # Blank=True allowed 'likes' field to be left blank
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
    )

    class Meta:
        ordering = ["-created", "-updated"]

    # '__str__' method defined to return the title_post
    # when its string representation is requested.
    def __str__(self):
        return self.title_post

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body_content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body_content} by {self.name}"