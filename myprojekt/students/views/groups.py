def groups_list(request):
	groups = (
		{'id':1,
		'name': u'���-1',
		'leader': {'id':1, 'name': u'����� �������'}},
		{'id':2,
		'name': u'���-22',
		'leader': {'id':2, 'name':u'������ ����������'}},
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