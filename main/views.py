from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from notes.models import Notes

@login_required
def home(request):
    if request.user.is_authenticated():
        notes = Notes.objects.all()
        return render(request, 'main/home.html', {'notes': notes})
    else:
        return render(request, 'main/home.html')
