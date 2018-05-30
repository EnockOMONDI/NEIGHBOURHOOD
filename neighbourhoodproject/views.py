from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
'''
this is the view responsible for the welcome page
'''

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
