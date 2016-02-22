"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from models import Queries
import scripts

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

'''
Looks up news items based on the keywords stored in the database
'''

def search(request):
    
    # get all relevent data from database and add search terms to list
    searches = Queries.objects.filter(username=request.user)
    keywords = []
    for key in searches:
        keywords.append(str(key.query))

    # extract relevant titles from the internet
    results = scripts.extractLinksTitles(keywords)
    links, titles = results[0], results[1]
    results = zip(links, titles)
    return render(request, 'app/search.html', 
                  {'results': results})