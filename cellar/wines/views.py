from django.shortcuts import render

def home(request):
    """Returns the home index.html page."""
    return render(request, 'index.html', {})
