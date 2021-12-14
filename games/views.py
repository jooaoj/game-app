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
