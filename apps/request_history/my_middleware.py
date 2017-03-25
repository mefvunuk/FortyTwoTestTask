from .models import MyRequest


class RequestHistoryMiddleware():
    def process_request(self, request):
        instance = MyRequest.objects.create(request_method=request.method, request_link=request.META.get('HTTP_REFERER', ''))
        instance = MyRequest.objects.order_by('-request_time')
        for c in range(len(instance)):
            if c >= 10:
                instance[c].delete()
        return None
