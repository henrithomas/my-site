from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """
    The model responsible for representing blog post data.
    """
    title = models.CharField(max_length=250)
    content = models.TextField()
    content_display = models.TextField(max_length=125)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)


    def get_absolute_url(self):
        return reverse('single-post', kwargs={'pk': str(self.id), 'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title[:(self._meta.get_field('slug').max_length)])
        super(Post, self).save(*args, **kwargs)
        # 50
        # slug_max_len =
        # # 45 || 30 || 100
        # title_len = len(self.title)
        # # dif = 50 - 45 = 5 || dif = 50 - 30 = 20 || dif = -50
        # dif = slug_max_len - title_len
        # # true || true || false
        # if title_len < slug_max_len:
        #     if dif < 10:
        #         # dif = 5, len(self.slug) = 50
        #         self.slug = slugify(self.title) + '-' + get_random_string((dif - 1))
        #     else:
        #         # dif = 20, len(self.slug) = 40
        #         self.slug = slugify(self.title) + '-' + get_random_string(9)
        # else:
        #     # dif = -50, len(self.slug) = 50
        #     self.slug = slugify(self.title[:(slug_max_len - 10)]) + '-' + get_random_string(9)


    def __str__(self):
        return self.title
