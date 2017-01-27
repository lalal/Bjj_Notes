from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Notes, NotesForm

class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        return Notes.objects.all()

class DetailView(generic.DetailView):
    model = Notes
    template_name = 'notes/detail.html'

def detail(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    return render(request, 'notes/detail.html', {'notes': note})

def create_note(request):
    form = NotesForm()
    return render(request, 'notes/create_note.html', {'form': form})

def edit_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    form = NotesForm(instance=note)
    return render(request, 'notes/create_note.html', {'form': form})
    
def delete_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    note.delete()
    notes = Notes.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})
    
