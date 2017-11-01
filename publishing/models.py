# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	the_year = models.PositiveIntegerField(null=True, blank=True)
	synopsis = models.TextField(null=True, blank=True)
	author = models.ForeignKey('Author')
	publisher = models.ForeignKey('Publisher')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=200)
	address = models.TextField()

	def __unicode__(self):
		return self.name

class Coba(models.Model):
	coba_tabel = models.CharField(max_length=200)

	def __unicode__(self):
		return self.coba_tabel

