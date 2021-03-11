from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField('phone', max_length=20, blank=True, null=True)
    company = models.CharField('company', max_length=200, blank=True, null=True)
    dept = models.CharField('department', max_length=100, blank=True, null=True)
    job = models.CharField('job', max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField('last update', auto_now=True, blank=True)

    class Meta:
        db_table = 'auth_user'
        ordering = ['updated_at']
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __unicode__(self):
        return self.username
