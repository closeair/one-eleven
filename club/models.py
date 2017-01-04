from datetime import datetime
from django.db import models
from django_markdown.models import MarkdownField
from django.contrib.auth.models import User
from commons.models import SecureDocument

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Minutes(models.Model):
  minutes_text = models.TextField(blank=False)
  minutes_file = models.FileField(blank=False)
  minutes_date = models.DateTimeField(blank=False, unique=True)

  def __unicode__(self):
    return self.minutes_date.strftime('%B, %Y')

  class Meta:
      verbose_name_plural = 'Minutes'


class Meeting(models.Model):
  occured_at = models.DateField(blank=True)
  minutes = models.ForeignKey(Minutes)

  def __unicode__(self):
    return self.occured_at.strftime('%B, %Y')


class Attendence(models.Model):
  meeting = models.ForeignKey(Meeting)
  member = models.ForeignKey(User, null=True)

  def __unicode__(self):
    return self.member.username


class Motion(models.Model):
  made_by = models.ForeignKey(User, null=True, related_name="motions_made")
  seconded_by = models.ForeignKey(User, null=True, blank=True, related_name="motions_seconded")
  body = models.TextField(null=True)
  @property
  def in_favor(self):
    return Vote.objects.filter(motion_id=self.pk, yay=True).count()
  @property
  def against(self):
    return Vote.objects.filter(motion_id=self.pk, yay=False).count()
  def __unicode__(self):
    return self.body[:150]+'..'


class Vote(models.Model):
  motion = models.ForeignKey(Motion, related_name="votes_made")
  yay = models.BooleanField(default=False)
  member = models.ForeignKey(User, null=True)


class PublicDocument(models.Model):
  name = models.CharField(max_length=100, null=True)
  uploaded_file = models.FileField(blank=False, null=True)

  def __unicode__(self):
	    return self.name


class MembershipApplication(models.Model):
  name = models.CharField(max_length=100, blank=False, null=True)
  email = models.CharField(max_length=100, blank=False, null=True)
  phone = models.CharField(max_length=20, blank=False, null=True)
  drivers_license_report = models.FileField(upload_to='documents/%Y/%m/%d/', blank=False, null=True)
  birth_date = models.DateField(blank=False, null=True)
  address = models.CharField(max_length=255, blank=False, null=True)
  city = models.CharField(max_length=20, blank=False, null=True)
  state_abbreviation = models.CharField(max_length=2, blank=False, null=True)
  zipcode = models.CharField(max_length=9, blank=False, null=True)
  criminal_convictions = models.TextField(blank=True, null=True)
  united_states_citizen = models.BooleanField(blank=False, default=False)
  if_no_where = models.CharField(max_length=100, blank=True, null=True)
  student = models.BooleanField(blank=True, default=False)
  private = models.BooleanField(blank=True, default=False)
  commercial = models.BooleanField(blank=True, default=False)
  atp = models.BooleanField(blank=True, default=False)
  cfi = models.BooleanField(blank=True, default=False)
  other = models.CharField(max_length=100, blank=True, null=True)
  faa_certificate_number = models.CharField(max_length=10, blank=False, null=True)
  total_flight_hours = models.CharField(max_length=4, blank=False, null=True)
  bfr_expiration = models.DateField(blank=False, null=True)
  medical_expiration = models.DateField(blank=False, null=True)
  reference_name = models.CharField(max_length=100, blank=False, null=True)
  reference_relation = models.CharField(max_length=30, blank=False, null=True)
  reference_phone = models.CharField(max_length=11, blank=False, null=True)
  information_verified_by = models.CharField(max_length=30, blank=False, null=True)
  inconsistencies = models.TextField(null=True)
  notes = models.TextField(null=True)
  approved = models.BooleanField(blank=True, default=False)
  submitted_at = models.DateField(default=datetime.now, blank=True)

  def __unicode__(self):
    return self.name


class InsuranceSurvey(models.Model):
  medical = models.BooleanField(default=False, choices=BOOL_CHOICES)
  medical_expiration = models.DateField(blank=False, null=True)
  bfr = models.BooleanField(default=False, choices=BOOL_CHOICES)
  bfr_expiration = models.DateField(blank=False, null=True)
  claims = models.BooleanField(default=False, choices=BOOL_CHOICES)
  drivers_license = models.BooleanField(default=False, choices=BOOL_CHOICES)
  felonies_misdemeanors = models.BooleanField(default=False, choices=BOOL_CHOICES)
  insurance_history = models.BooleanField(default=False, choices=BOOL_CHOICES)
  truthful = models.BooleanField(default=False)
  printed_name = models.CharField(max_length=100, blank=False, null=True)
  submitted_at = models.DateField(default=datetime.now, blank=True)
  submitted_by = models.ForeignKey(User, null=True)
  def __unicode__(self):
    return "%s %s" % (self.submitted_by.first_name, self.submitted_by.last_name)


class Survey(models.Model):
  made_by = models.ForeignKey(User, null=True)
  def __unicode__(self):
    return "%s" % (self.question)


class SurveyResponse(models.Model):
  survey = models.ForeignKey(Survey)
  member = models.ForeignKey(User, null=True)
  detail = models.CharField(max_length=2000, blank=True, default=False)
