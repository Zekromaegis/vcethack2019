from . import views
from django.conf.urls import url

app_name = 'IndustryFinder'

urlpatterns = [

    #/signup/
    url(r'^signup/$', views.UserFormView.as_view(), name = 'signup'),

    # /profile/<pk>/
    url(r'^profile/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /profile/update/
    url(r'^profile/update/$', views.StudentUpdate, name='student-update'),

    # /profile/
    url(r'^profile/$', views.saveStudentData, name='save-student-data'),

    #/home/
    url(r'^home/$', views.Home.as_view(), name='home'),
]