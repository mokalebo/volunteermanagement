from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('volunteer_list', views.volunteer_list, name='volunteer_list'),
    path('volunteer/<int:pk>/edit/', views.volunteer_edit, name='volunteer_edit'),
    path('volunteer/<int:pk>/delete/', views.volunteer_delete, name='volunteer_delete'),
    path('availability_list', views.availability_list, name='availability_list'),
    path('availability/create/', views.availability_new, name='availability_new'),
    path('availability/<int:pk>/edit/', views.availability_edit, name='availability_edit'),
    path('availability/<int:pk>/delete/', views.availability_delete, name='availability_delete'),
    path('opportunity_list', views.opportunity_list, name='opportunity_list'),
    path('opportunity/create/', views.opportunity_new, name='opportunity_new'),
    path('opportunity/<int:pk>/edit/', views.opportunity_edit, name='opportunity_edit'),
    path('opportunity/<int:pk>/delete/', views.opportunity_delete, name='opportunity_delete'),
    path('assignment_list', views.assignment_list, name='assignment_list'),
    path('assignment/create/', views.assignment_new, name='assignment_new'),
    path('assignment/<int:pk>/edit/', views.assignment_edit, name='assignment_edit'),
    path('assignment/<int:pk>/delete/', views.assignment_delete, name='assignment_delete'),
    path('organization_list', views.organization_list, name='organization_list'),
    path('organization/create/', views.organization_new, name='organization_new'),
    path('organization/<int:pk>/edit/', views.organization_edit, name='organization_edit'),
    path('organization/<int:pk>/delete/', views.organization_delete, name='organization_delete'),
    # path('volunteer/<int:pk>/summary/', views.summary, name='summary'),
]