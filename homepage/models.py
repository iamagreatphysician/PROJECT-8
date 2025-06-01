from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title
    
#comment ,post ,content,created_by,updated_by
class Comment(BaseTimestampModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updater', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment on {self.post.title} by {self.created_at}'