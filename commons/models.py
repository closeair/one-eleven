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

