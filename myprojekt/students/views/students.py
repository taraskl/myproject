#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_list(request):
	students = (
		{'id':1,
		'first_name': u'Віталій',
		'last_name': u'Подоба',
		'ticket': 235,
		'image': 'static/img/me.jpeg'},
		{'id':2,
		'first_name': u'Корост',
		'last_name': u'Андрій',
		'ticket': 2123,
		'image': 'static/img/piv.png'},
	)

	return render(request, 'students/students_list.html',
		{'students':students})

def students_add(request):
	return HttpResponse('here we will have a form')
	
def students_edit(request, sid):
	return HttpResponse('student %s edit form' %sid)