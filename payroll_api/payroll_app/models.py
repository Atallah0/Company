from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employees')
    manager = models.ForeignKey('Manager', null=True, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return str(self.user)


class Manager(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='managers')

    def __str__(self):
        return str(self.employee)


class Department(models.Model):
    dep_name = models.CharField(max_length=20)
    dep_place = models.CharField(max_length=20)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return str(self.dep_name)


class Payroll(models.Model):
    title = models.CharField(max_length=50, default='payroll')
    date = models.DateField(null=True)
    basic_salary = models.PositiveIntegerField(default=0)
    extra_work_hours = models.PositiveIntegerField(default=0)
    extra_paid = models.PositiveIntegerField(default=0)
    bonus = models.PositiveIntegerField(default=0)
    income_tax = models.PositiveIntegerField(default=0)
    percent = models.PositiveIntegerField(default=100)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='payrolls')

    def __str__(self):
        return str(self.title)
