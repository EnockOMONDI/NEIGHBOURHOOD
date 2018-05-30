from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from neighbourhoodapp.models import Neighbourhood, NeighbourhoodMember

# Create your views here.


class CreateNeighbourhood(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'location')
    model = Neighbourhood


class SingleNeighbourhood(generic.DetailView):
    model = Neighbourhood


class ListNeighbourhoods(generic.ListView):
    model = Neighbourhood

'''
    This view function will enable new users join a given neighbourhood
'''
class JoinNeighbourhood(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('neighbourhoodapp:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        neighbourhood = get_object_or_404(Neighbourhood, slug=self.kwargs.get('slug'))

        try:
            NeighbourhoodMember.objects.create(user=self.request.user, neighbourhood=neighbourhood)
        except IntegrityError:
            messages.warning(self.request, ' already a member!')
        else:
            messages.success(self.request, 'welcome to the community!')

        return super().get(request, *args, **kwargs)

'''
    This view function will eneble users to exit a neighborhood
'''
class LeaveNeighbourhood(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('neighbourhoodapp:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = NeighbourhoodMember.objects.filter(user=self.request.user, neighbourhood__slug=self.kwargs.get('slug')).get()
        except NeighbourhoodMember.DoesNotExist:
            messages.warning(self.request, ' bummer looks like your are not a resident here!')
        else:
            membership.delete()
            messages.success(self.request, 'bummer looks like you are not a member!')

        return super().get(request, *args, **kwargs)
        
