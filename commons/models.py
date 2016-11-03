from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class Pilot(models.Model):
  user = models.OneToOneField(User)

  def __unicode__(self):
	    return self.user.username


class Document(models.Model):
  uploaded_by = models.ForeignKey(User, null=True)
  name = models.CharField(max_length=100, null=True)
  uploaded_file = models.FileField(blank=False, null=True)

  def __unicode__(self):
	    return self.name


class SecureDocument(Document):
  pass


class SupportingDocument(Document):
  pass


class Aircraft(models.Model):
  avatar = models.ImageField(upload_to='aircraft')
  n_number = models.CharField(max_length=10, null=True)
  model = models.CharField(max_length=255, null=True)
  location_identifier = models.CharField(max_length=5, null=True)
  equipment = models.CharField(max_length=255, null=True)
  color = models.CharField(max_length=25, null=True)
  true_air_speed_knots = models.CharField(max_length=25, null=True)
  hp = models.IntegerField()
  useful_load = models.IntegerField()
  price_per_hour_usd = models.IntegerField()
  misc_info = models.TextField()

  def image_thumb(self):
       return mark_safe('<img src="%s" height="100"/>' % (self.avatar.url))
  image_thumb.short_description = 'Avatar'

  def __str__(self):
    return self.n_number

  class Meta:
    verbose_name_plural = _("Aircraft")

class AirworthinessDirective(models.Model):
  title = models.CharField(max_length=25, null=True)
  next_due_date = models.DateField()
  days_interval = models.IntegerField()
  tach_interval = models.IntegerField()
  aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)


class Scheduling(models.Model):  # Heavily bias towards the calendar json/view
  user = models.ForeignKey(User)
  aircraft = models.ForeignKey(Aircraft)
  name = models.CharField(max_length=25, null=True)  # pilot
  image = models.ImageField()
  color = models.IntegerField() # aircraft have different colors in display
  start_time = models.DateTimeField
  end_time = models.DateTimeField
  description = models.TextField() # destination


class Flight(models.Model):
  user = models.ForeignKey(User)
  aircraft = models.ForeignKey(Aircraft)
  scheduling = models.ForeignKey(Scheduling)
  gallons_at_start = models.IntegerField(null=True)
  ending_tach = models.FloatField(null=True)
  ending_hobbs = models.FloatField(null=True)
