from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from .models import Notes, NotesForm


def notes_list(request):
    notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes})

def notes_create(request):
    form = NotesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('notes:list')
    return render(request, 'notes/notes_create.html', {'form': form})

def notes_update(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    form = NotesForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('notes:list')
    return render(request, 'notes/notes_create.html', {'form': form})

def notes_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')
    return render(request, 'notes/notes_confirm_delete.html', {'object': note})

def notes_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'notes/notes_detail.html', {'notes': note})
