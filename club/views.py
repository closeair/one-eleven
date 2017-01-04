from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.shortcuts import redirect
from .models import Motion, PublicDocument, Survey
from .forms import MembershipApplicationForm, InsuranceSurveyForm, VoteForm, LoginForm, SurveyResponseForm


def index(request):
  return render(request, 'club/index.html')

def thanks(request):
  return render(request, 'club/thanks.html')

def public(request):
  public_documents = PublicDocument.objects.all()
  return render(request, 'club/public.html', {'public_documents': public_documents})

def application(request):
  if request.method == 'POST':
    form = MembershipApplicationForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/thanks/')
  else:
    form = MembershipApplicationForm()
  return render(request, 'club/application.html', {'form': form})

def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      import pdb;pdb.set_trace()
      auth_login(request, form.user)
      return redirect(reverse('panel'))
  else:
    form = LoginForm()
    return render(request, 'club/login.html', {'form': form})

@login_required(login_url='/login/')
def insurance(request):
  if request.method == 'POST':
    form = InsuranceSurveyForm(request.POST)
    if form.is_valid():
      document = form.save(commit=False)
      document.submitted_by = request.user
      document.save()
      return HttpResponseRedirect('/complete/')
  else:
    form = InsuranceSurveyForm()
  return render(request, 'club/insurance.html', {'form': form})

@login_required(login_url='/login/')
def panel(request):
  return render(request, 'club/panel.html', {'user': request.user})

@login_required(login_url='/login/')
def vote(request, motion):
  motion = get_object_or_404(Motion, pk=motion)
  if request.method == 'POST':
    form = VoteForm(request.POST, initial={'motion': motion})
    if form.is_valid():
      document = form.save(commit=False)
      document.submitted_by = request.user
      document.motion = motion
      document.save()
      return HttpResponseRedirect('/complete/')
  else:
    form = VoteForm()
  return render(request, 'club/vote.html', {'form': form, 'motion': motion})

def complete(request):
  return render(request, 'club/complete.html')

@login_required(login_url='/admin/login/')
def survey(request, survey):
  survey = get_object_or_404(Survey, pk=survey)
  if request.method == 'POST':
    form = SurveyResponseForm(request.POST, initial={'survey': survey})
    if form.is_valid():
      document = form.save(commit=False)
      document.member = request.user
      document.survey = survey
      document.save()
      return HttpResponseRedirect('/complete/')
  else:
    form = SurveyResponseForm(initial={'detail': ''})
  return render(request, 'club/survey.html', {'form': form, 'survey': survey})
