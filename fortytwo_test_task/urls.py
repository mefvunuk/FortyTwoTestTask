from django.conf.urls import patterns, include, url
from apps.hello.views import Home_view
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
    url(r'^request_history$', TemplateView.as_view(template_name="base.html"), name='request_history'),
)
