from django.contrib import admin
from xsd_members.models import *

class MemberAdmin(admin.ModelAdmin):
    pass
class MembershipTypeAdmin(admin.ModelAdmin):
    pass
class MailingAdmin(admin.ModelAdmin):
    pass

admin.site.register(MemberProfile, MemberAdmin)
admin.site.register(MembershipType, MembershipTypeAdmin)
# admin.site.register(Mailing, MailingAdmin)
