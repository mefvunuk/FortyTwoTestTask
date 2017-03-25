from .models import MyRequest


class RequestHistoryMiddleware():
    def process_request(self, request):
        instance = MyRequest.objects.create(request_method=request.method, request_link=request.META.get('HTTP_REFERER', ''))
        if instance:
            pass
        return None
