from django.db import models

# Create your models here.
User = get_user_model()
reigster = template.Library


class Neighbourhood(models.Model):
    name = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(allow_unicode=True,  unique=True)
    location = models.CharField(max_length=140, blank=True, default='')
    occupants = models.ManyToManyField(User, through='NeighbourhoodMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('neighbourhoods:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

class NeighbourhoodMember(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_neighbourhoods')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('neighbourhood', 'user')
