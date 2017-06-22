from django.contrib.auth.models import User
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    obs = models.CharField(null=True, blank=True, max_length=255)

    dh_create = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    user_create = models.ForeignKey(User, editable=False, blank=False, related_name="%(app_label)s_%(class)s_create_related")
    dh_update = models.DateTimeField(auto_now=True, editable=False, blank=True)
    user_update = models.ForeignKey(User, editable=False, blank=False, related_name="%(app_label)s_%(class)s_update_related")
    
    class Meta:
        abstract = True