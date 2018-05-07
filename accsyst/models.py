from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Bill(models.Model):
    salary = models.IntegerField(null=True)
    hours = models.IntegerField(null=True)


class Card(models.Model):
    date = models.DateField(default=timezone.now())
    working_hours = models.IntegerField(null=True)
    extra_hours = models.IntegerField(null=True)
    day_hours = 8

    rate = models.IntegerField(null=True)
    extra_coeff = 1.5
    fix_salary = models.IntegerField(null=True)

    PAYMENT_CHOICE = (
        ('Csh', 'Cash'),
        ('Crd', 'Card')
    )
    payment = models.CharField(max_length=4, choices=PAYMENT_CHOICE, null=True)

    def save(self, *args, **kwargs):
        if self.working_hours > self.day_hours:
            self.extra_hours = self.working_hours - self.day_hours
        super(Card, self).save(*args, **kwargs)


class UserInfo(models.Model):
    surname = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    picture = models.ImageField(upload_to='profile_images', null=True)


class Report(models.Model):
    workers = models.ManyToManyField('Worker')
    accountants = models.ManyToManyField('Accountant')
    bills = models.ForeignKey(Bill)
    info = models.CharField(max_length=100, null=True)
    comments = models.CharField(max_length=500, null=True)


class AdminReport(Report):
    admin = models.ManyToManyField('Admin')


#  User profiles


class UserProfile(User):
    card = models.OneToOneField(Card)
    user_info = models.OneToOneField(UserInfo)


class Worker(UserProfile):
    accountant_ptr = models.ForeignKey('Accountant', null=True)


class Accountant(UserProfile):
    admin_ptr = models.ForeignKey('Admin', null=True)


class Admin(UserProfile):
    pass
