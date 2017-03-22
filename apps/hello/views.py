from django.views.generic.base import TemplateView


class Home_view(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(Home_view, self).get_context_data(**kwargs)
        context.update({'name': 'Oleg', 'surname': 'Vunuk', 'email': 'mefvunuk@gmail.com',
                        'date': '02.09.1989', 'bio': 'Live in Lviv', 'jabber': 'mefvunuk@42cc.co',
                        'skype': 'None', 'contacts': 'None'})
        return context
