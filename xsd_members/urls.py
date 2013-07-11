from django.conf.urls import patterns, include, url
from django.conf import settings

from views import *

urlpatterns = patterns('',
	    url(r'^profile/$', 'xsd_members.views.view_my_profile', name='my-profile'),
	    url(r'^profile/edit/$', MyProfileEdit.as_view(), name='MyProfileEdit'),
	    url(r'^$', 'xsd_members.views.admin', name='members_admin'),
	    url(r'^search/$', MemberSearch.as_view(), name='MemberSearch'),
	    url(r'^member/(?P<pk>\d+)$', MemberDetail.as_view(), name='MemberDetail'),
	    url(r'^list/$', MemberList.as_view(), name='MemberList'),
)