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
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_author = models.ForeignKey(
        'Author', on_delete='CASCADE', related_name="Books"
    )


class Author(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book_rated = models.ForeignKey(
        'Book', on_delete='CASCADE', related_name="rated_book"
    )
    book_reviewd = models.ForeignKey(
        'Book', on_delete='CASCADE', related_name="reviewed_book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
