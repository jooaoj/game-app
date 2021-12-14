from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Title, Entry
from .forms import TitleForm, EntryForm

def index(request):
    """The home page available to anyone."""
    return render(request, 'games/index.html')

@login_required
def titles(request):
    """Show all games."""
    titles = Title.objects.order_by('date_added')
    context = {'titles': titles}
    
    return render(request, 'games/titles.html', context)
@login_required
def title(request, title_id):
    """Descriptions and other details per game-entry."""
    title = Title.objects.get(id=title_id)
    entries = title.entry_set.order_by('-date_added')
    context = {'title': title, 'entries': entries}

    return render(request, 'games/title.html', context)
@login_required
def new_title(request):
    """Add a new title."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TitleForm()
    else:
          # POST data submitted; process data.
          form = TitleForm(data=request.POST)
          if form.is_valid():
              form.save()
              return redirect('games:titles')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'games/new_title.html', context)
@login_required
def new_entry(request, title_id):
    """Add a new entry for a particular title"""
    title = Title.objects.get(id=title_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.title = title
            new_entry.save()
            return redirect('games:title', title_id=title_id)

    # Display a blank or invalid form.
    context = {'title': title, 'form': form} 
    return render(request, 'games/new_entry.html', context)       
@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    title = entry.title

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('games:title', title_id=title.id)  

    # Display a blank or invalid form.
    context = {'entry': entry, 'title': title, 'form': form} 
    return render(request, 'games/edit_entry.html', context)       

