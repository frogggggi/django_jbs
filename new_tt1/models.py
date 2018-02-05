#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, date, time
#from django.utils.image import Image


class Presentation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthdate = models.DateTimeField(null=True, default=datetime.now, blank=True, verbose_name='Дата рождения')
    bio = models.TextField(null=True, verbose_name='Биография')
    phone = models.CharField(max_length=50, null=True, verbose_name='Телефон')
    skype = models.CharField(max_length=50, null=True, verbose_name='Скайп')
    photo = models.ImageField(null=True, blank=True, upload_to='photos', verbose_name='Фото')


class RequestContent(models.Model):
    method = models.CharField(max_length=7)
    path = models.TextField('Путь', max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField('Статус code', max_length=3)


class AuditLogEntry(models.Model):
    """
    Stores CRUD actions related to model instance
    """
    class Meta:
        verbose_name = "AuditLog Entry"
        verbose_name_plural = "AuditLog Entries"

    ACTION_UNKNOWN = 0
    ACTION_CREATE = 1
    ACTION_UPDATE = 2
    ACTION_DELETE = 3

    ACTION_CHOICES = (
        (ACTION_UNKNOWN, 'Unknown'),
        (ACTION_CREATE, 'Create'),
        (ACTION_UPDATE, 'Update'),
        (ACTION_DELETE, 'Delete')
    )

    date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=40)
    instance = models.CharField(max_length=40)
    action = models.SmallIntegerField(max_length=1, choices=ACTION_CHOICES, default=0)

    def __unicode__(self):
        return u'%s [%s] <%s: %s>' % \
            (self.date, self.get_action_display(), self.model, self.instance)
