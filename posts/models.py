from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class BaseModel(models.Model):
    uid = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blogsimg')

    def __str__(self):
        return self.title
