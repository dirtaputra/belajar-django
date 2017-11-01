# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pembeli(models.Model):
	name = models.CharField(max_length=200)
	address = models.TextField()
	notlp = models.CharField(max_length=12)

	def __unicode__(self):
		return self.name