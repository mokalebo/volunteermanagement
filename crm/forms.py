from django import forms
from .models import Volunteer
from .models import Volunteer, Availability, Opportunity, Assignment, Organization

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('user', 'email', 'address', 'city', 'state', 'zipcode', 'phone_number')

class AvailabilityForm(forms.ModelForm):
   class Meta:
       model = Availability
       fields = ('service_category', 'description', 'location', 'setup_time', 'cleanup_time' )
       exclude = ('vol_name',)

class OpportunityForm(forms.ModelForm):
   class Meta:
       model = Opportunity
       fields = ('organization', 'date', 'time')

class AssignmentForm(forms.ModelForm):
   class Meta:
       model = Assignment
       fields = ('volunteer', 'opportunity') 

class OrganizationForm(forms.ModelForm):
   class Meta:
       model = Organization
       fields = ('name', 'street', 'city', 'state', 'zip', 'phone')