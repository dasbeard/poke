from __future__ import unicode_literals

from django.db import models

# Create your models here.
#

class Poke(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    poker = models.ForeignKey('loginReg.Users', related_name='thepokerpoke')
    poked = models.ForeignKey('loginReg.Users', related_name='thepokedpoke')


class Thepoke(models.Model):
    poker = models.ManyToManyField('loginReg.Users', related_name='thepoker')
    poker = models.ManyToManyField('loginReg.Users', related_name='thepoked')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
