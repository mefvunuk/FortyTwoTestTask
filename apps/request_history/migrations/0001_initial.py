# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyRequest'
        db.create_table(u'request_history_myrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('request_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('request_link', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('request_status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'request_history', ['MyRequest'])

    def backwards(self, orm):
        # Deleting model 'MyRequest'
        db.delete_table(u'request_history_myrequest')

    models = {
        u'request_history.myrequest': {
            'Meta': {'object_name': 'MyRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'request_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['request_history']
