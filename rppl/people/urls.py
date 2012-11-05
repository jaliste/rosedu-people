from django.conf.urls.defaults import patterns, include, url

from views import Overview, Profile, Projects, ProjectDetail

urlpatterns = patterns('',
    url(r'^$', Overview.as_view(), name='overview'),
    url(r'^profile/(?P<pk>\d+)/$', Profile.as_view(), name='profile'),
    url(r'^project/$', Projects.as_view(), name='project-list'),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project-detail'),
)
