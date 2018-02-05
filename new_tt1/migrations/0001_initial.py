# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presentation'
        db.create_table(u'new_tt1_presentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthdate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'new_tt1', ['Presentation'])

        # Adding model 'RequestContent'
        db.create_table(u'new_tt1_requestcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('path', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status_code', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal(u'new_tt1', ['RequestContent'])

        # Adding model 'AuditLogEntry'
        db.create_table(u'new_tt1_auditlogentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('instance', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('action', self.gf('django.db.models.fields.SmallIntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal(u'new_tt1', ['AuditLogEntry'])


    def backwards(self, orm):
        # Deleting model 'Presentation'
        db.delete_table(u'new_tt1_presentation')

        # Deleting model 'RequestContent'
        db.delete_table(u'new_tt1_requestcontent')

        # Deleting model 'AuditLogEntry'
        db.delete_table(u'new_tt1_auditlogentry')


    models = {
        u'new_tt1.auditlogentry': {
            'Meta': {'object_name': 'AuditLogEntry'},
            'action': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'new_tt1.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'new_tt1.requestcontent': {
            'Meta': {'object_name': 'RequestContent'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'path': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['new_tt1']