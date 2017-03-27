from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import MyRequest
import json


class RequestHistory(TemplateView):

    template_name = 'request_template.html'

    def get_context_data(self, **kwargs):
        context = super(RequestHistory, self).get_context_data(**kwargs)
        context['request_set'] = MyRequest.objects.all()
        return context


def my_request_number(request):
    unread_number = 0
    request_set = MyRequest.objects.all()
    for c in request_set:
        if c.request_status == 0:
            unread_number += 1
    return HttpResponse(json.dumps({'request_number': unread_number}), content_type="application/json")
