# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Guru, Siswa

# Register your models here.


class SiswaAdmin(admin.ModelAdmin):
    model = Siswa
    list_display = ('nis', 'nama', 'kelas', 'jurusan')


class GuruAdmin(admin.ModelAdmin):
    model = Guru
    list_display = ('nip', 'nama', 'mapel')
    fieldsets = (
        (None, {
            'fields': ('nip', 'nama')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('mapel',),
        }),
    )

admin.site.register(Guru, GuruAdmin)
admin.site.register(Siswa, SiswaAdmin)
