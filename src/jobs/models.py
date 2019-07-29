import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Employer

class Job(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.CharField(max_length=255, null=True, blank=True)
    employment_type = models.CharField(max_length=255, null=True, blank=True)
    pay_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    published = models.BooleanField(default=False, blank=True)
    is_featured = models.BooleanField(default=False, blank=True)
    is_expired = models.BooleanField(default=False, blank=True)
    apply_here = models.BooleanField(default=False, blank=True)
    apply_instructions = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    positions_to_fill = models.PositiveIntegerField(blank=True)
    creator = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs', blank=True)

    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    def __str__(self):
        return self.name

