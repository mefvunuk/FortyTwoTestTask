from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import MyRequest
import json
from django.utils.formats import date_format
from django.db.models import F


class RequestHistory(TemplateView):

    template_name = 'request_template.html'


def my_request_number(request):
    unread_number = 0
    request_set = MyRequest.objects.all()
    for c in request_set:
        if c.request_status == 0:
            unread_number += 1
    return HttpResponse(json.dumps({'request_number': unread_number}), content_type="application/json")


def request_upload(request):
    request_set = MyRequest.objects.order_by('-request_time')
    json_data = []
    for c in request_set:
        if c.request_status == 0:
            c.request_status = F('request_status')+1
            c.save(update_fields=['request_status'])
        json_data.append({
                          'request_method': c.request_method,
                          'request_link': c.request_link,
                          'request_time': date_format(c.request_time, 'DATETIME_FORMAT'),
                        })
    return HttpResponse(json.dumps(json_data), content_type="application/json")
