from django.db import models
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['first_name']) < 2:
            errors['first_name'] = "Name is too short"
        if len(data['last_name']) < 2:
            errors['last_name'] = "Name is too short"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email is invalid"
        if len(data['password']) < 8:
            errors['password'] = "Password needs to be 8 characters or longer"
        if data['password'] != data['cpassword']:
            errors['password'] = "Passwords do not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField("Message", related_name="Liked_messages")
    objects = UserManager()
    objects = UserManager()


class MessageManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['message']) < 2:
            errors['message'] = "Message needs 2 charaters or more"
        return errors


class Message(models.Model):
    author = models.CharField(max_length=50)
    message = models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_related = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name="user_messaged")
    objects = MessageManager()
