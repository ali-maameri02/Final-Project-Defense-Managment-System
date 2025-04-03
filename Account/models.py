from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    USER_ROLE = (
        ('Student', 'Student'),
        ('Professor', 'Professor'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    role = models.CharField(max_length=20, choices=USER_ROLE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    picture = models.ImageField(upload_to='Profiles/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.password.startswith('pbkdf2_sha256$'):  # Avoid double hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Student(models.Model):
    TEAM_TYPE_CHOICES = (
        ('Binome', 'Binome'),
        ('Monome', 'Monome'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    team_type = models.CharField(max_length=50, choices=TEAM_TYPE_CHOICES)

    def __str__(self):
        return self.user.username


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    supervisor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(models.Model):
    student1 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='team_student1')
    student2 = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='team_student2')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Team: {self.student1.user.username} & {self.student2.user.username if self.student2 else 'Solo'}"
