from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from collections import OrderedDict
import requests # Used to send HTTP requests to the API
import json     # Library to convert the JSON files sent back ---> python dictionary
from pprint import pprint # A library to display nicer looking data structures
#from django.core.context_processors import csrf
from login.models import paperHolder
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('registration_complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update((request))
    token['form'] = form

    return render(request, 'register.html', token)


def registration_complete(request):
    return render(request, 'register_complete.html')


def results(request):

    if request.GET.get('search_term'):
        message = request.GET['search_term']
        if message == "":
            message = 'eggs'
    else:
        message = 'eggs'

    # Dictionary of the Querystring parameters and constraints (see website for details)
    keywords = 'keyword: ' + message
    data = {'api_key': 'd094966bbd58635d6772e3c43a0df59a', 'q': keywords, 'p': '10'}

    # Request data from server --> JSON file returned
    response = requests.get("http://api.springer.com/metadata/json", data)

    jr = response.json()
        
    api_results = [OrderedDict([('title',i['title']),
            ('abstract',i['abstract'][8:400]),
            ('publicationDate',i['publicationDate']),
            ('url',i['url'][0]['value']),]) for i in jr["records"]]

    today = "hello there"

    #if request contains url identifier
    if (request.GET.get('url')):
        user_id = request.user.id

        url = request.GET['url']
        #find the right paper in api_results
        for result in api_results:
            if result['url'] == url:
                #create entry in db
                p = paperHolder(user_id=user_id, papername=result['title'], url=result['url'], date=result['publicationDate'])
                #save to db
                p.save()

    return render(request, "results.html", {"api_results" : api_results, "today" : today, "search_term" : message})
