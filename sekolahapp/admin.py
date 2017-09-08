# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MataPelajaran, Jurusan
from userapp.models import Guru

# Register your models here.


class MataPelajaranInline(admin.TabularInline):
    model = MataPelajaran


class JurusanAdmin(admin.ModelAdmin):
    model = Jurusan
    inlines = [
        MataPelajaranInline,
    ]


class GuruInline(admin.TabularInline):
    model = Guru


class MapelAdmin(admin.ModelAdmin):
    model = MataPelajaran
    inlines = [
        GuruInline,
    ]

admin.site.register(MataPelajaran, MapelAdmin)
admin.site.register(Jurusan, JurusanAdmin)
