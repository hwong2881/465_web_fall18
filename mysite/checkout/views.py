from django.shortcuts import render
# from django.conf import settings
from django.views.generic.base import TemplateView


class check_out(TemplateView):
    template_name = 'checkout/checkout.html'

    # def get_context_data(self, **kwargs): # new
    #     context = super().get_context_data(**kwargs)
    #     context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    #     return context
