from django.shortcuts import render

# Create your views here.
from django.template.backends import django
from django.views.generic import TemplateView
from . import models


class chartsView(TemplateView):
    template_name = 'charts/charts.html'
    Users = django.apps.get_model('charts.Users')

    def get_context_data(self, **kwargs):
        context = super(chartsView, self).get_context_data(**kwargs)
        context['users'] = self.Users.objects.order_by('userid')
        print(context['users'][0].name)
        return context
