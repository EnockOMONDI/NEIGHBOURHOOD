from django.contrib import admin
from . import models

# Register your models here.


class NeighbourhoodMember(admin.TabularInline):
    model = models.NeighbourhoodMember


admin.site.register(models.Neighbourhood)
