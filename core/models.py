from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Custom User Modeli
class User(AbstractUser):
    ROLE_CHOICES = (
        ('donor', 'E\'lon beruvchi'),
        ('beneficiary', 'Qabul qiluvchi'),
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# 2. Kategoriya Modeli
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# 3. E'lon Modeli
class Announcement(models.Model):
    STATUS_CHOICES = (
        ('active', 'Faol'),
        ('claimed', 'Band qilingan'),
        ('completed', 'Topshirildi'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='announcements')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='announcements/', blank=True, null=True)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 4. Band qilish (So'rov) Modeli
class Claim(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Kutilmoqda'),
        ('approved', 'Qabul qilindi'),
        ('rejected', 'Rad etildi'),
    )

    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='claims')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claims')
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim by {self.applicant.username} for {self.announcement.title}"