from django.views.generic.base import TemplateView
from .models import MyRequest


class RequestHistory(TemplateView):

    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(RequestHistory, self).get_context_data(**kwargs)
        context['request_set'] = MyRequest.objects.all()
        return context
