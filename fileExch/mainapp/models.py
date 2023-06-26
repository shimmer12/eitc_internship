from django.db import models
from django.contrib.auth.models import AbstractUser

class AccessLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    CHOICESLEVEL = [
        ('Dispatch', 'Dispatch'),
        ('SectionOffice', 'Section Office'),
        ('HOD', 'Head of Department'),
    ]

    access_levels = models.ManyToManyField(AccessLevel, choices=CHOICESLEVEL, default='Dispatch')

    def __str__(self):
        return self.username

import uuid
from django.db import models
from django.contrib.auth import get_user_model

class Image(models.Model):
    CHOICES = [
        ('Dispatch', 'Dispatch'),
        ('SectionOffice', 'Section Office'),
        ('HOD', 'Head of Department'),
    ]
    User = get_user_model()
    users = User.objects.all()
    title = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=CHOICES)
    photo = models.FileField(upload_to='pics')
    approver = models.CharField(max_length=36)  # Store UUID as a string
    history = models.TextField()

    def __str__(self):
        user = self.users.filter(id=self.approver).first()
        if user:
            return f"Image: {self.title}, Status: {self.status}, Approver: {user.username}"
        return f"Image: {self.title}, Status: {self.status}"
