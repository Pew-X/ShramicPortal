from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'

class Skill(models.Model):
    name = models.CharField(max_length=50)

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class Employer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary_range = models.CharField(max_length=50)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    locations = models.ManyToManyField(Location)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
