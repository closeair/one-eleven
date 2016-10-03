from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from .models import Motion, PublicDocument
from .forms import MembershipApplicationForm, InsuranceSurveyForm, VoteForm


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
      if Group.objects.filter(name=settings.THEBOARD).exists():
        board_emails = map(lambda x: x.email, Group.objects.get(name=settings.THEBOARD).user_set.all())
        send_mail(
          'New Member Application',
          'There is a new member application for %s' % form.cleaned_data.get('name'),
          settings.DONOTREPLY,
		  board_emails,
		  fail_silently=False)
      return HttpResponseRedirect('/thanks/')
  else:
    form = MembershipApplicationForm()
  return render(request, 'club/application.html', {'form': form})

def login(request):
   form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(reverse('panel'))
    return render(request, 'club/login.html', {'form': form })

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
  user = User.objects.get(username='john')
  return render(request, 'club/panel.html', {'user': user})

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
