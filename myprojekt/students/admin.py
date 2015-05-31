# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Student, Group
from .models import MonthJournal

# Register your models here.
admin.site.register(MonthJournal)
admin.site.register(Student)
admin.site.register(Group)
