#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from .models import Presentation, RequestContent, AuditLogEntry
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.conf import settings
from .forms import PresentationForm
from django.contrib import auth
from django.db.models import get_model
from django.http import Http404
#from django.db.models import get_model
from django.views.generic import ListView
from django.test.client import RequestFactory
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
'''
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=RequestContent)
def my_handler(sender, **kwargs):
    print("Request post_save!")

'''

IGNORELIST = (
    'AuditLogEntry',
    'RequestContentMiddleware',
    'LogEntry', #django admin app
)


@receiver(post_save, sender=Presentation)
#@receiver(post_save, sender=RequestContent)
def AuditLogger(sender, **kwargs):
    '''
    Logger Stores CRUD actions related to model instances
    depending on ENABLE_AUDIT setting
    '''

    if not getattr(settings, 'ENABLE_AUDIT', False):
        print("ENABLE_AUDIT False")
        return

    if sender._meta.object_name in IGNORELIST:
        print("IGNORELIST")
        return

    print("Request post_save signals.py!")
    print(kwargs)
    print(kwargs.get('instance'))

    action = AuditLogEntry.ACTION_DELETE

    if kwargs.has_key('created'):
        #created is True if a new record was created https://docs.djangoproject.com/en/dev/ref/signals/#post-save
        action = kwargs.get('created') and AuditLogEntry.ACTION_CREATE or AuditLogEntry.ACTION_UPDATE
        print("created is True")

    '''
    AuditLogEntry.objects.get_or_create(name=kwargs.get('instance'))
    AuditLogEntry.objects.create(
        model=sender._meta.object_name,
        instance=unicode(kwargs.get('instance')),
        action=sender)
    '''
    AuditLogEntry1 = get_model('new_tt1', 'AuditLogEntry')

    request_log1 = AuditLogEntry1(
        model=sender._meta.object_name,
        instance=unicode(kwargs.get('instance')),
        action=action
    )
    request_log1.save()


def requestContetnView(ListView):
    querysets = RequestContent.objects.all().order_by('-date')[:10]
    return render_to_response('request.html', {'querysets': querysets})


def home(request):
    # Работаем с объектом
    queryset = Presentation.objects.all()
    for item in queryset:
        name = item.name  # выводим адрес
        surname = item.surname  # выводим город
        birthdate = item.birthdate  # выводим дату рождения
        bio = item.bio  # выводим инфо
        phone = item.phone  # выводим телефон
        skype = item.skype  # выводим skype
        photo = item.photo  # выводим фото

    # TEMPLATE_CONTEXT_PROCESSORS
    val1 = settings.MY_EMAIL
    val2 = settings.MY_NAME
    response_dict = RequestContext(request)
    # добавляем новое значение
    response_dict['some_var_only_in_this_view'] = 42

    tmp_dict = RequestContext(request)
    tmp_dict.update(response_dict)

    return render_to_response('index.html',
                              {'MY_EMAIL': val1, 'MY_NAME': val2, 'queryset': queryset, 'response_dict': response_dict,
                               'name': name, 'surname': surname, 'birthdate': birthdate, 'bio': bio, 'phone': phone,
                               'skype': skype, 'photo': photo, 'username': auth.get_user(request).username, })


def post_edit(request):
    instance = get_object_or_404(Presentation.objects.all())
    if request.method == "POST":
        form = PresentationForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            #message.success()
            return HttpResponseRedirect('/')
    else:
        form = PresentationForm(instance=instance)
    return render(request, 'edit.html', {'form': form})







