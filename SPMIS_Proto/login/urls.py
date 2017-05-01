from django.conf.urls import url,  include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import login
from login.views import register1, registration_complete, results, savedPapers
admin.autodiscover()

app_name= 'login'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    #url(r'^results/$',  TemplateView.as_view(template_name='results.html'), name='results'),
    #sadasasdsad
    url(r'^register/$', register1, name='register'),
    url(r'^register/registration_complete/$', registration_complete, name='complete'),
    url(r'^results/$', results, name='results'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/$', savedPapers, name='account'),
]
