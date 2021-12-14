from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Title
from .forms import TitleForm

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

