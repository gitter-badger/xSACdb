from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.contrib.auth.models import User, Group

from xSACdb.roles.mixins import RequireAdministrator, RequireVerified
from xSACdb.version import *

class AboutView(RequireVerified, TemplateView):
	template_name='about_about.html'
	def get_context_data(self, **kwargs):
	    context = super(AboutView, self).get_context_data(**kwargs)
	    context['version'] = VERSION
	    return context

class DatabaseOfficersView(RequireVerified, TemplateView):
	template_name='about_database_officers.html'
	def get_users_in_role(self, role):
		return Group.objects.get(pk=role).user_set.all()
	def get_context_data(self, **kwargs):
	    context = super(DatabaseOfficersView, self).get_context_data(**kwargs)
	    context['admins'] = self.get_users_in_role(2)
	    context['dos'] = self.get_users_in_role(7)
	    context['mos'] = self.get_users_in_role(6)
	    context['tos'] = self.get_users_in_role(3)
	    context['instructors'] = None
	    context['tas'] = self.get_users_in_role(4)
	    context['sas'] = self.get_users_in_role(5)
	    return context

