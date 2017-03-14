from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from collections import OrderedDict
import requests # Used to send HTTP requests to the API
import json     # Library to convert the JSON files sent back ---> python dictionary
from pprint import pprint # A library to display nicer looking data structures
#from django.core.context_processors import csrf
from login.models import paperHolder, variable_holder
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from datetime import *
from login.changekeys import nextkey
from django.core.cache import cache



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


def savedPapers(request):
    saved_papers = []
    this_user_id = request.user.id

    if request.GET.get('url'):
        url = request.GET.get('url')
        paperHolder.objects.filter(user_id=this_user_id, url=url).delete()

    data = serializers.serialize( "python", paperHolder.objects.filter(user_id=this_user_id ))
    for item in data:
        for shit, value in item.items():
                if (shit == "fields"):
                    saved_papers.append(value)
    print(saved_papers)
                
    #saved_papers = [OrderedDict([('title', paper.get_field(papername)),
    #    ('url', paper._meta.get_field(url)),
    #    ('date', paper._meta.get_field(date))]) for paper in savedPapers]


    return render(request, 'account.html', {"saved_papers" : saved_papers})

def results(request):

    if cache.get('counter') is None:
        cache.set('counter', 0, None)
        api_key = nextkey();
    else:
        api_key = nextkey();

    if request.GET.get('search_term'):
        message = request.GET['search_term']
        if message == "":
            message = 'eggs'
    else:
        message = 'eggs'

    # Removes the \n newline character
    api_key = api_key[:len(api_key)-1]

    # Dictionary of the Querystring parameters and constraints (see website for details)
    keywords = 'keyword: ' + message
    data = {'api_key': api_key, 'q': keywords, 'p': '10'}

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
        if(user_id is not None):
            url = request.GET['url']
            #find the right paper in api_results
            for result in api_results:
                if result['url'] == url:
                    #create entry in db
                    saved_papers = []
                    data = serializers.serialize( "python", paperHolder.objects.filter(user_id=user_id ))
                    for item in data:
                        for key, value in item.items():
                            if (key == 'fields'):
                                saved_papers.append(value)

                    date = datetime.strptime(result['publicationDate'], "%Y-%m-%d")

                    #check if user has already saved paper change to not in and get rid of useless else statement
                    if OrderedDict([("user_id", user_id), ("papername", result['title']), ("url", result['url']), ("date", date.date())]) in saved_papers:
                        #user has already saved paper
                        print("already got et mate")
                    else:
                        #save that paper
                        p = paperHolder(user_id=user_id, papername=result['title'], url=result['url'], date=result['publicationDate'])
                        p.save()


    return render(request, "results.html", {"api_results" : api_results, "today" : today, "search_term" : message})