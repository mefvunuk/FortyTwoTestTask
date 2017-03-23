from django.views.generic.base import TemplateView
from .models import Info


class Home_view(TemplateView):
    """View"""

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(Home_view, self).get_context_data(**kwargs)
        context['info'] = Info.objects.all()
        return context
