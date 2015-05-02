#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student

# Create your views here.
def student_list(request):
	page = request.GET.get('page')
	# try to order studenys list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()
		
	# paginate students
	students = Student.objects.all()
	paginator = Paginator(students, 2) # Show 3 student per pag
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		students = paginator.page(paginator.num_pages)
	
	return render(request, 'students/students_list.html',
		{'students':students})

def students_add(request):
	return HttpResponse('here we will have a form')
	
def students_edit(request, sid):
	return HttpResponse('student %s edit form' %sid)
	
def groups_list(request):
	groups = (
		{'id':1,
		'name': u'Мтм-1',
		'leader': {'id':1, 'name': u'Тарас Мельник'}},
		{'id':2,
		'name': u'Мтм-22',
		'leader': {'id':2, 'name':u'Микола Садовський'}},
	)
	return render(request, 'students/groups_list.html',
		{'groups':groups})
def groups_add(request):
	return HttpResponse('here we will have a form')
	
def groups_edit(request, sid):
	return HttpResponse('group %s edit form' %sid)
	
def groups_delete(request, sid):
	return HttpResponse('group %s delete form' %sid)
	
def journal(request):
	return HttpResponse('journal')