from django.contrib import admin

from .models import Volunteer, Availability, Opportunity, Assignment, Organization


class VolunteerList(admin.ModelAdmin):
    list_display = ( 'vol_name', 'email', 'phone_number' )
    # list_filter = ( 'vol_name')
    search_fields = ('vol_name', )
    ordering = ['vol_name']


class AvailabilityList(admin.ModelAdmin):
    list_display = ( 'vol_name', 'service_category', 'setup_time')
    list_filter = ( 'vol_name', 'setup_time')
    search_fields = ('vol_name', )
    ordering = ['vol_name']

class OpportunityList(admin.ModelAdmin):
    list_display = ( 'organization', 'date', 'time')
    list_filter = ( 'organization', 'date')
    search_fields = ('organization', )
    ordering = ['organization']
	
class AssignmentList(admin.ModelAdmin):
    list_display = ( 'volunteer', 'opportunity')
    list_filter = ( 'volunteer', 'opportunity')
    search_fields = ('volunteer', )
    ordering = ['volunteer']
	
class OrganizationList(admin.ModelAdmin):
    list_display = ( 'name', 'city', 'phone')
    list_filter = ( 'name', 'phone')
    search_fields = ('name', )
    ordering = ['name']


admin.site.register(Volunteer, VolunteerList)
admin.site.register(Availability, AvailabilityList)
admin.site.register(Opportunity, OpportunityList)
admin.site.register(Assignment, AssignmentList)
admin.site.register(Organization, OrganizationList)