#! /usr/bin/env python
# -*- coding: utf-8 -*-
from celery.task import periodic_task
from datetime import timedelta
# from celery.schedules import crontab

# используя селери записывать какое то значение в celery.log
@periodic_task(run_every = timedelta(seconds = 120))
def test():
    print "is works!"
    # открыть файл на дозапись
    # запускаем командой ./manage.py celeryd -l INFO -B
    f = open("celery.log", "a")
    f.write('celery is works! ' + '\n')
    f.close()