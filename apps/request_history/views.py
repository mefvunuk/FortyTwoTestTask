from django.views.generic.base import TemplateView
from datetime import datetime


class RequestHistory(TemplateView):

    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(RequestHistory, self).get_context_data(**kwargs)
        context.update({'request_method': 'POST', 'request_link': 'http://127.0.0.1:8000/', 'request_date': datetime.now()})
        return context
