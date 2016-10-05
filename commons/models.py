from django.db import models
from django.contrib.auth.models import User


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
  avatar = ImageField(upload_to='aircraft')
  n_number = models.CharField(max_length=10, null=True)
  model = models.CharField(max_length=255, null=True)
  location_identifier = models.CharField(max_length=5, null=True)
  equipment = models.CharField(max_length=255, null=True)
  color = models.CharField(max_length=25, null=True)
  true_air_speed_knots = models.CharField(max_length=25, null=True)
  hp = models.IntegerField()
  useful_load = models.IntegerField()
  price_per_hour_usd = models.FloatField()
  misc_info = models.TextField()


class AirworthnessDirective(models.Model):
    pass



class Scheduling(models.Model):
    # pilot
    # aircraft
    # start
    # end
    # destination
    # notes
    pass


class Flight(models.Model):
    # fuel at start
    # tach (or hobbs)
    # pilot
    # aircraft
    # scheduling
    pass






class
