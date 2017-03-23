from django.views.generic.base import TemplateView


class Home_view(TemplateView):
    """View"""

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(Home_view, self).get_context_data(**kwargs)
        context['name'] = 'Oleg'
        context['surname'] = 'Vunuk'
        context['email'] = 'mefvunuk@gmail.com'
        return context
