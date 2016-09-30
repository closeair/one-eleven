from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm

@login_required(login_url='/admin/login/')
def upload(request):
  if request.method == 'POST':
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
      document = form.save(commit=False)
      document.uploaded_by = request.user
      document.save()
      return HttpResponseRedirect('/uploaded/')
  else:
    form = DocumentForm()
  return render(request, 'commons/upload.html', {'form': form})

def uploaded(request):
  return render(request, 'commons/uploaded.html')
	
