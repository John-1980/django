from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    status = (
        ('drafts', 'Drafts'),
        ('publish', 'Publish'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status, default='drafts')

    # ordena relacão de posts na ordem crescente
    # ordem decrescente seria ('-publish',)
    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title
