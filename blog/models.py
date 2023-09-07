from django.db import models
import uuid


# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class PostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("UserModel", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    created = models.DateTimeField()
    updated = models.DateTimeField()


class PostLikesModel(models.Model):
    post = models.OneToOneField("PostModel", on_delete=models.CASCADE)
    who_likes = models.ManyToManyField("UserModel")


class CommentModel(models.Model):
    author = models.ManyToManyField("UserModel")
    post = models.OneToOneField("PostModel", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    created = models.DateTimeField()
    updated = models.DateTimeField()
