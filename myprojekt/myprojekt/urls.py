from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.student_list', name='home'),
	url(r'^students/add/$', 'students.views.students_add', name='students_add'),
	url(r'^students/(?P<sid>[0-9]+)/edit/$', 'students.views.students_edit', name='students_edit'),
	
	#Groups urls
	url(r'^groups/$', 'students.views.groups_list', name='groups_list'),
	url(r'^groups/add/$', 'students.views.groups_add', name='groups_add'),
	url(r'^groups/(?P<sid>[0-9]+)/edit/$', 'students.views.groups_edit', name='groups_edit'),
	url(r'^groups/(?P<sid>[0-9]+)/delete/$', 'students.views.groups_delete', name='groups_delete'),
	#Journal urls
	url(r'^journal/$', 'students.views.journal', name='journal'),
	
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
)  

if DEBUG:
	# serve files from media folder
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)