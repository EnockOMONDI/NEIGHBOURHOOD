from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


class BusinessList(SelectRelatedMixin, generic.ListView):
    model = models.Business
    select_related = ('user', 'neighbourhood')


class UserBusinesses(generic.ListView):
    model = models.Business
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.business_user = User.objects.prefetch_related('businesses').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.business_user.businesses.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business_user'] = self.business_user
        return context


class BusinessDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Business
    select_related = ('user', 'neighbourhood')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user___username__iexact=self.kwargs.get('username'))


class CreateBusiness(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('business_name', 'business_email', 'neighbourhood')
    model = models.Business

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteBusiness(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Business
    select_related = ('user', 'neighbourhood')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Business Deleted')
        return super().delete(*args, **kwargs)
