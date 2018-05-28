from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from neighbourhoods.models import Neighbourhood
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Business(models.Model):
    user = models.ForeignKey(User, related_name="businesses")
    created_at = models.DateTimeField(auto_now=True)
    business_name = models.CharField(max_length=140, blank=True, null=True)
    business_email = models.EmailField(max_length=70, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='businesses', null=True, blank=True)

    def __str__(self):
        return self.business_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'business_name']
