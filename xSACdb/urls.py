from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'xsd_frontend.views.dashboard', name='dashboard'),
    url(r'^update-request/$', 'xsd_frontend.views.update_request', name='update_request'),

    url(r'^design/$', 'xsd_frontend.views.design', name='design'),

    url(r'^accounts/login/$', 'xsd_frontend.views.login', name='login'),
    url(r'^accounts/register/$', 'xsd_frontend.views.register', name='login'),
    url(r'^accounts/logout/$', 'xsd_frontend.views.logout', name='logout'),
    
    url(r'^facebook/', include('django_facebook.urls')),

    url(r'^profile/$', 'xsd_members.views.view_my_profile', name='my-profile'),

    url(r'^members/', include('xsd_members.urls')),

    url(r'^training/', include('xsd_training.urls')),

    url(r'^sites/', include('xsd_sites.urls')),

    url(r'^trips/', include('xsd_trips.urls')),

    url(r'^kit/', include('xsd_kit.urls')),

    url(r'^about/', include('xsd_about.urls')),

    # Can be enabled for serving static files (dev only)
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': settings.STATIC_DOC_ROOT}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
