from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum



now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

# def rolemanagercheck(user):
	# if user.groups == ('Manager'):
		# return True
	# else:
		# return False

def rolemanagercheck(user):
	return user.groups.filter(name__in=['Managers'])
	
def rolevolunteercheck(user):
	return user.groups.filter(name__in=['Volunteer'])

# def rolevolunteercheck(self):
	# if self.groups == ('Volunteer'):
		# return True
	# else:
		# return False
		

@login_required
# @user_passes_test(rolecheck)
def assignment_list(request):
    assignments = Assignment.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/assignment_list.html',
                 {'assignments': assignments})

@login_required
# @user_passes_test(rolevolunteercheck)
def assignment_new(request):
   if request.method == "POST":
       form = AssignmentForm(request.POST)
       if form.is_valid():
           assignment = form.save(commit=False)
           assignment.created_date = timezone.now()
           assignment.save()
           assignments = Assignment.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/assignment_list.html',
                         {'assignments': assignments})
   else:
       form = AssignmentForm()
       # print("Else")
   return render(request, 'crm/assignment_new.html', {'form': form})

@login_required
@user_passes_test(rolevolunteercheck)
def assignment_edit(request, pk):
   assignment = get_object_or_404(Assignment, pk=pk)
   if request.method == "POST":
       # update
       form = AssignmentForm(request.POST, instance=assignment)
       if form.is_valid():
           assignment = form.save(commit=False)
           assignment.updated_date = timezone.now()
           assignment.save()
           assignments = Assignment.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/assignment_list.html',
                         {'assignments': assignments})
   else:
        # edit
       form = AssignmentForm(instance=assignment)
   return render(request, 'crm/assignment_edit.html', {'form': form})
   
@login_required
@user_passes_test(rolevolunteercheck)
def assignment_delete(request, pk):
   assignment = get_object_or_404(Assignment, pk=pk)
   assignment.delete()
   return redirect('crm:assignment_list')
   
@login_required
def organization_list(request):
    organization = Organization.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/organization_list.html',
                 {'organizations': organization})

@login_required
@user_passes_test(rolemanagercheck)
def organization_new(request):
   if request.method == "POST":
       form = OrganizationForm(request.POST)
       if form.is_valid():
           organization = form.save(commit=False)
           organization.created_date = timezone.now()
           organization.save()
           organizations = Organization.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/organization_list.html',
                         {'organizations': organizations})
   else:
       form = OrganizationForm()
       # print("Else")
   return render(request, 'crm/organization_new.html', {'form': form})

@login_required
@user_passes_test(rolemanagercheck)
def organization_edit(request, pk):
   organization = get_object_or_404(Organization, pk=pk)
   if request.method == "POST":
       # update
       form = OrganizationForm(request.POST, instance=organization)
       if form.is_valid():
           organization = form.save(commit=False)
           organization.updated_date = timezone.now()
           organization.save()
           organizations = Organization.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/organization_list.html',
                         {'organizations': organizations})
   else:
        # edit
       form = OrganizationForm(instance=organization)
   return render(request, 'crm/organization_edit.html', {'form': form})
   
@login_required
@user_passes_test(rolemanagercheck)
def organization_delete(request, pk):
   organization = get_object_or_404(Organization, pk=pk)
   organization.delete()
   return redirect('crm:organization_list')

@login_required
@user_passes_test(rolemanagercheck)
def volunteer_list(request):
    volunteer = Volunteer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/volunteer_list.html',
                 {'volunteers': volunteer})

@login_required
def volunteer_edit(request, pk):
   volunteer = get_object_or_404(Volunteer, pk=pk)
   if request.method == "POST":
       # update
       form = VolunteerForm(request.POST, instance=volunteer)
       if form.is_valid():
           volunteer = form.save(commit=False)
           volunteer.updated_date = timezone.now()
           volunteer.save()
           volunteers = Volunteer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/volunteer_list.html',
                         {'volunteers': volunteers})
   else:
        # edit
       form = VolunteerForm(instance=volunteer)
   return render(request, 'crm/volunteer_edit.html', {'form': form})

@login_required
def volunteer_delete(request, pk):
   volunteer = get_object_or_404(Volunteer, pk=pk)
   volunteer.delete()
   return redirect('crm:volunteer_list')

@login_required
def availability_list(request):
   availabilitys = Availability.objects.filter(created_date__lte=timezone.now())
   return render(request, 'crm/availability_list.html', {'availabilitys': availabilitys})

@login_required
@user_passes_test(rolevolunteercheck)
def availability_new(request):
   if request.method == "POST":
       form = AvailabilityForm(request.POST)
       if form.is_valid():
           availability = form.save(commit=False)
           availability.created_date = timezone.now()
           availability.vol_name = request.user.username
           availability.save()
           availabilitys = Availability.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/availability_list.html',
                         {'availabilitys': availabilitys})
   else:
       form = AvailabilityForm()
       # print("Else")
   return render(request, 'crm/availability_new.html', {'form': form})

@login_required
@user_passes_test(rolevolunteercheck)
def availability_edit(request, pk):
   availability = get_object_or_404(Availability, pk=pk)
   if request.method == "POST":
       form = AvailabilityForm(request.POST, instance=availability)
       if form.is_valid():
           availability = form.save()
           # service.customer = service.id
           availability.updated_date = timezone.now()
           availability.save()
           availabilitys = Availability.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/availability_list.html', {'availabilitys': availabilitys})
   else:
       # print("else")
       form = AvailabilityForm(instance=availability)
   return render(request, 'crm/availability_edit.html', {'form': form})

@login_required
@user_passes_test(rolevolunteercheck)
def availability_delete(request, pk):
   availability = get_object_or_404(Availability, pk=pk)
   availability.delete()
   return redirect('crm:volunteer_list')

@login_required
def opportunity_list(request):
   opportunitys = Opportunity.objects.filter(created_date__lte=timezone.now())
   return render(request, 'crm/opportunity_list.html', {'opportunitys': opportunitys})

@login_required
@user_passes_test(rolemanagercheck)
def opportunity_new(request):
   if request.method == "POST":
       form = OpportunityForm(request.POST)
       if form.is_valid():
           opportunity = form.save(commit=False)
           opportunity.created_date = timezone.now()
           opportunity.save()
           opportunitys = Opportunity.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/opportunity_list.html', {'opportunitys': opportunitys})
   else:
       form = OpportunityForm()
       # print("Else")
   return render(request, 'crm/opportunity_new.html', {'form': form})

@login_required
@user_passes_test(rolemanagercheck)
def opportunity_edit(request, pk):
   opportunity = get_object_or_404(Opportunity, pk=pk)
   if request.method == "POST":
       form = OpportunityForm(request.POST, instance=opportunity)
       if form.is_valid():
           opportunity = form.save()
           # service.customer = service.id
           opportunity.updated_date = timezone.now()
           opportunity.save()
           opportunitys = Opportunity.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/opportunity_list.html', {'opportunitys': opportunitys})
   else:
       # print("else")
       form = OpportunityForm(instance=opportunity)
   return render(request, 'crm/opportunity_edit.html', {'form': form})

@login_required
@user_passes_test(rolemanagercheck)
def opportunity_delete(request, pk):
   opportunity = get_object_or_404(Opportunity, pk=pk)
   opportunity.delete()
   return redirect('crm:opportunity_list')

# @login_required
# def summary(request, pk):
    # customer = get_object_or_404(Volunteer, pk=pk)
    # customers = Volunteer.objects.filter(created_date__lte=timezone.now())
    # services = Service.objects.filter(cust_name=pk)
    # products = Product.objects.filter(cust_name=pk)
    # sum_service_charge = Service.objects.filter(cust_name=pk).aggregate(Sum('service_charge'))
    # sum_product_charge = Product.objects.filter(cust_name=pk).aggregate(Sum('charge'))
    # return render(request, 'crm/summary.html', {'customers': customers,
                                                    # 'products': products,
                                                    # 'services': services,
                                                    # 'sum_service_charge': sum_service_charge,
                                                    # 'sum_product_charge': sum_product_charge,})

