<<<<<<< HEAD
from django.conf.urls import patterns, url
from django.conf import settings
=======
from django.conf.urls import patterns, url #import two functions
>>>>>>> Yang

import dashboard.views

urlpatterns = patterns('',
    url(r'^$', dashboard.views.DashboardView.as_view(), name='dashboard-index'),
)

<<<<<<< HEAD
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
=======
#class based view
>>>>>>> Yang
