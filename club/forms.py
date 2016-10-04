from django.contrib.admin.widgets import AdminFileWidget
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from django.forms import extras
from django.core.exceptions import ValidationError
from .models import MembershipApplication, InsuranceSurvey, Vote

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class MembershipApplicationForm(forms.ModelForm):
  error_css_class = 'error'
  drivers_license_report = forms.FileField(widget=AdminFileWidget)
  class Meta:
    model = MembershipApplication
    widgets = {
      'birth_date': extras.SelectDateWidget(years=range(1920, 2010)),
      'bfr_expiration': extras.SelectDateWidget(years=range(1920, 2020)),
      'medical_expiration': extras.SelectDateWidget(years=range(1920, 2020)),
    }
    labels = {
      'bfr_expiration': 'BFR Expiration',
      'faa_certificate_number': 'FAA Certificate Number',
      'cfi': 'CFI/CFII',
      'atp': 'ATP',
      'if_no_where': 'If NO, where?',
      'united_states_citizen': 'US Citizen?',
      'birth_date': 'Birth Date',
    }
    error_messages = {
      'name': {
        'required': 'Please enter your full name',
      },
      'email': {
        'required': 'Please enter your email address',
      },
      'phone': {
        'required': 'Please enter your phone number',
      },
      'drivers_license_report': {
        'required': "Please attach your driver's license report",
      },
      'address': {
        'required': 'Please enter your full address',
      },
      'city': {
        'required': 'Please enter your city',
      },
      'state_abbreviation': {
        'required': 'Please enter the abbreviation for your state',
      },
      'zipcode': {
        'required': 'Please enter your zipcode',
      },
      'total_flight_hours': {
        'required': 'Please enter your total hours or N/A if you are a student and have zero hours',
      },
      'faa_certificate_number': {
        'required': 'Please enter your FAA certificate number or N/A if you are a student',
      },
      'reference_name': {
        'required': 'Please your the name of your reference',
      },
      'reference_relation': {
        'required': 'Please enter how you know your reference',
      },
      'reference_phone': {
        'required': 'Please enter the phone number of your reference',
      },
    }
    fields = ['name', 'email', 'phone', 'drivers_license_report', 'birth_date', 'address', 'city', 'state_abbreviation', 'zipcode', 'phone', 'criminal_convictions', 'united_states_citizen', 'if_no_where', 'student', 'private', 'commercial', 'atp', 'cfi', 'other', 'faa_certificate_number', 'total_flight_hours', 'bfr_expiration', 'medical_expiration', 'reference_name', 'reference_relation', 'reference_phone',]


class VoteForm(forms.ModelForm):
  yay = forms.ChoiceField(widget=forms.RadioSelect,
    choices=BOOL_CHOICES, label='Vote Yes or No')
  class Meta:
    model = Vote
    fields = ['yay',]


class LoginForm(forms.Form):
  username = forms.CharField(max_length=255, required=True)
  password = forms.CharField(widget=forms.PasswordInput, required=True)

  def __init__(self, login={}, *args, **kwargs):
    if 'username' not in login or 'password' not in login:
        return super(LoginForm, self).__init__(*args, **kwargs)

    super(LoginForm, self).__init__(login, *args, **kwargs)

    if not self.is_valid():
        return

    username = login['username']
    password = login['password']

    if not User.objects.filter(username=username).exists():
      self.add_error('username', 'Username is incorrect.')

    self.user = authenticate( username=username, password=password)
    if not self.user:
      self.add_error('password', 'Password is incorrect.')


class InsuranceSurveyForm(forms.ModelForm):
  truthful = forms.BooleanField(required=True, label="The information I have supplied to Richmond Pilots on this form is true and correct and no material information has been withheld.")
  class Meta:
    model = InsuranceSurvey
    widgets = {
      'medical_expiration': extras.SelectDateWidget(years=range(2015, 2020)),
      'medical': forms.RadioSelect,
      'bfr_expiration': extras.SelectDateWidget(years=range(2015, 2020)),
      'bfr': forms.RadioSelect,
      'claims': forms.RadioSelect,
      'drivers_license': forms.RadioSelect,
      'felonies_misdemeanors': forms.RadioSelect,
      'insurance_history': forms.RadioSelect,
    }
    labels = {
      'medical': "Do have a current medical certificate?",
      'medical_expiration': "If so, when does it expire?",
      'bfr': "Do have a current BFR?",
      'bfr_expiration': "If so, when does it expire?",
      'claims': "In the past 36 months, have you had an aircraft accident, incident or insurance claim?",
      'drivers_license': "In the past 36 months, have you had your pilot's or driver's license surrendered, suspended or revoked, or been arrested for, or charged with, operating an aircraft or motor vehicle under the influence of drugs or alcohol?",
      'felonies_misdemeanors': "In the past 36 months, have you been convicted of, or pleaded guilty or no contest to, any felony or misdemeanor other than for parking?",
      'insurance_history': "In the past 36 months, have you had an aircraft policy canceled or been refused a renewal on an aircraft policy?",
      'truthful': "The information I have supplied to Richmond Pilots on this form is true and correct and no material information has been withheld.",
      'printed_name': "Print your full name for the record:",
    }
    fields = ['medical', 'medical_expiration', 'bfr', 'bfr_expiration', 'claims', 'drivers_license', 'felonies_misdemeanors', 'insurance_history', 'truthful', 'printed_name',]
