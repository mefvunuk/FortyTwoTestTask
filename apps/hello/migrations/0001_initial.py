# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Info'
        db.create_table(u'hello_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('contacts', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'hello', ['Info'])

    def backwards(self, orm):
        # Deleting model 'Info'
        db.delete_table(u'hello_info')

    models = {
        u'hello.info': {
            'Meta': {'object_name': 'Info'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hello']
