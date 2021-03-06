from django.conf.urls import patterns, include, url
from apps.hello.views import Home_view
from apps.request_history.views import RequestHistory
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home_view.as_view(), name='home'),
    url(r'^request_history$', RequestHistory.as_view(), name='request_history'),
    url(r'^request_number$', 'apps.request_history.views.my_request_number', name='request_number'),
    url(r'^request_upload$', 'apps.request_history.views.request_upload', name='request_template'),
    url(r'^add_data$', TemplateView.as_view(template_name='add_data.html'), name='add_data'),
)
