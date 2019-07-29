import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Employer, Professional
from jobs.models import Job


class CompetencyType(models.Model):
    COMPETENCY_TIER_CHOICES = (
        ('Personal', 'Personal'),
        ('Academic', 'Academic'),
        ('Workplace', 'Workplace'),
        ('Sector', 'Sector'),
    )

    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    tier = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)


class Competency(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    required = models.BooleanField(default=False, blank=True)
    skill = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey(
        CompetencyType, on_delete=models.CASCADE, related_name="competencies", blank=True)
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="competencies", null=True, blank=True)

    class Meta:
        verbose_name = _('competency')
        verbose_name_plural = _('competencies')

    def __str__(self):
        return self.skill


class ProfessionalCompetency(models.Model):
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name='competencies', blank=True)
    competency = models.ForeignKey(
        Competency, on_delete=models.CASCADE, related_name='professional', blank=True)
    proficiency_level = models.CharField(max_length=10, null=True, blank=True)
    experience = models.CharField(max_length=10, null=True, blank=True)


class JobQualification(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                            related_name='qualifictions', blank=True)
    competency = models.ForeignKey(
        Competency, on_delete=models.CASCADE, related_name='jobs', blank=True)
    proficiency_level = models.CharField(max_length=10, null=True, blank=True)
    experience = models.CharField(max_length=10, null=True, blank=True)
    is_required = models.BooleanField(default=False, blank=True)
