from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from .models import Notes, NotesForm
from django.contrib.auth.decorators import login_required



def get_notes_and_categories(my_user):
    notes = Notes.objects.filter(note_user=my_user).order_by('note_date')
    categories = Notes.objects.filter(note_user=my_user).distinct('note_category')
    return notes, categories

@login_required
def notes_list(request):
    print "got here"
    categories = {}
    if request.method == 'POST':
       cat_filter = request.POST.get('cat') 
       if cat_filter is None or cat_filter == 'None':
           notes, categories = get_notes_and_categories(request.user)
       else:
           notes = Notes.objects.filter(note_user=request.user).filter(note_category=cat_filter).order_by('note_date')
    else:   
       notes, categories = get_notes_and_categories(request.user)
    print notes, categories
    return render(request, 'notes/notes_list.html', {'notes': notes, 'categories': categories})

@login_required
def notes_create(request):
    form = NotesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('notes:list')
    return render(request, 'notes/notes_create.html', {'form': form})

@login_required
def notes_update(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    form = NotesForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('notes:list')
    return render(request, 'notes/notes_create.html', {'form': form})

@login_required
def notes_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')
    return render(request, 'notes/notes_confirm_delete.html', {'object': note})

@login_required
def notes_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'notes/notes_detail.html', {'notes': note})
