from django.shortcuts import render

from .models import Title

def index(request):
    """The home page available to anyone."""
    return render(request, 'games/index.html')

def titles(request):
    """Show all games."""
    titles = Title.objects.order_by('date_added')
    context = {'titles': titles}
    
    return render(request, 'games/titles.html', context)

def title(request, title_id):
    """Descriptions and other details per game-entry."""
    title = Title.objects.get(id=title_id)
    entries = title.entry_set.order_by('-date_added')
    context = {'title': title, 'entries': entries}

    return render(request, 'games/title.html', context)
