# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maja_newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='unsubscribers',
            field=models.ManyToManyField(blank=True, related_name='mailinglist_unsubscriber', to='maja_newsletter.Contact', verbose_name='unsubscribers'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='test_contacts',
            field=models.ManyToManyField(blank=True, to='maja_newsletter.Contact', verbose_name='test contacts'),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='contacts',
            field=models.ManyToManyField(blank=True, to='maja_newsletter.Contact', verbose_name='contacts'),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='mailinglists',
            field=models.ManyToManyField(blank=True, to='maja_newsletter.MailingList', verbose_name='mailing lists'),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='newsletters',
            field=models.ManyToManyField(blank=True, to='maja_newsletter.Newsletter', verbose_name='newsletters'),
        ),
    ]