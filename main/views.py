from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from notes.models import Notes
from notes.views import notes_list

@login_required
def home(request):
    if request.user.is_authenticated():
        return notes_list(request)
    else:
        return render(request, 'main/home.html')
