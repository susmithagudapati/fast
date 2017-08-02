from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _



@python_2_unicode_compatible
class Subject(models.Model):

	name = models.CharField(_('name'), max_length=128)
	description = models.CharField(_('description'), max_length=2048, blank=True)
	slug = models.SlugField(unique=True)
	instructor = models.ForeignKey(User, null=True)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.name;



@python_2_unicode_compatible
class Topic(models.Model):

	name = models.CharField(_('name'),max_length=128)
	subject = models.ForeignKey(Subject)
	description = models.CharField(_('description'), max_length=2048, blank=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return "{0}, ({1})".format(self.name, self.subject)



@python_2_unicode_compatible
class Session(models.Model):

	name = models.CharField(_('name'), max_length=128)
	description = models.CharField(_('description'), max_length=2048, blank=True)
	session_id = models.IntegerField(_('session id'))
	topics = models.ManyToManyField(Topic)

	def __str__(self):
		return "{0}, ({1})".format(self.name, self.session_id)



@python_2_unicode_compatible
class SubSessionCategory(models.Model):

	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name



@python_2_unicode_compatible
class SubSession(models.Model):

	session = models.ForeignKey(Session)
	topic = models.ForeignKey(Topic)
	duration = models.PositiveIntegerField()
	category = models.ManyToManyField(SubSessionCategory)

	def __str__(self):
		return self.name



@python_2_unicode_compatible
class Objective(models.Model):

	name = models.CharField(max_length=128)
	session = models.ForeignKey(Session)

	def __str__(self):
		return "{0} ({1})".format(self.name, self.session)




