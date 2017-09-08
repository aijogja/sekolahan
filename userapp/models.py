# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

KELAS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

# Create your models here.


class Guru(models.Model):
    nip = models.CharField(max_length=10, unique=True, db_index=True)
    nama = models.CharField(max_length=100, null=True)
    mapel = models.ForeignKey(
        'sekolahapp.MataPelajaran', blank=True, null=True)

    def __unicode__(self):
        return '%s-%s' % (self.nip, self.nama)

    class Meta:
        verbose_name_plural = 'Guru'


class Siswa(models.Model):
    nis = models.CharField(max_length=10, unique=True, db_index=True)
    nama = models.CharField(max_length=100, null=True)
    kelas = models.CharField(
        max_length=1,
        choices=KELAS_CHOICES,
        default='1'
    )
    jurusan = models.ForeignKey('sekolahapp.Jurusan', null=True)
    mapel = models.ManyToManyField('sekolahapp.MataPelajaran')

    def __unicode__(self):
        return '%s-%s' % (self.nis, self.nama)

    class Meta:
        verbose_name_plural = 'Siswa'
