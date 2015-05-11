#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Group

def groups_list(request):
	groups = Group.objects.all()
#	groups = (
#		{'id':1,
#		'name': u'���-1',
#		'leader': {'id':1, 'name': u'����� �������'}},
#		{'id':2,
#		'name': u'���-22',
#		'leader': {'id':2, 'name':u'������ ����������'}},
#	)
	return render(request, 'students/groups_list.html',
		{'groups':groups})
def groups_add(request):
	return HttpResponse('here we will have a form')
	
def groups_edit(request, sid):
	return HttpResponse('group %s edit form' %sid)
	
def groups_delete(request, sid):
	return HttpResponse('group %s delete form' %sid)