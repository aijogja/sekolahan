# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class MataPelajaran(models.Model):
    nama = models.CharField(max_length=100, null=True)
    jurusan = models.ForeignKey('sekolahapp.Jurusan', blank=True, null=True)

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Mata Pelajaran'


class Jurusan(models.Model):
    kode = models.CharField(max_length=4, null=True)
    nama = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return '%s-%s' % (self.kode, self.nama)

    class Meta:
        verbose_name_plural = 'Jurusan'
