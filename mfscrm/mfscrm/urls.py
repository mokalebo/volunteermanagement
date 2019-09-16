"""mfscrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('accounts/password_change/',
        PasswordChangeView.as_view(template_name='registration/passwordchangeform.html'),
        name='passwordchangeform'),
    path('accounts/password_change/done',
        PasswordChangeDoneView.as_view(template_name='registration/passwordchangedone.html'),
        name='password_change_done'),
    path('accounts/password_reset/',
        PasswordResetView.as_view(template_name='registration/passwordresetform.html'),
        name='passwordresetform'),
    path('accounts/password_reset/done',
        PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'),
        name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='registration/passwordresetconfirm.html'),
        name='password_reset_confirm'),
    path('accounts/password_reset/complete',
        PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'),
        name='password_reset_complete'),
    re_path(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    re_path(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),

]