from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from collections import OrderedDict
import requests # Used to send HTTP requests to the API
import json     # Library to convert the JSON files sent back ---> python dictionary
from pprint import pprint # A library to display nicer looking data structures
#from django.core.context_processors import csrf
from login.models import paperHolder, historyHolder
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from datetime import date as d
from datetime import datetime
from login.changekeys import nextkey, getstart
from django.core.cache import cache
from nltk.corpus import stopwords
from login.API_interface import api_strategy, Springer # import all the clases from the API strategy
import nltk


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
    search_history = []
    if request.GET.get('url'):
        url = request.GET.get('url')
        paperHolder.objects.filter(user_id=this_user_id, url=url).delete()

    data = serializers.serialize( "python", paperHolder.objects.filter(user_id=this_user_id ))
    for item in data:
        for stuff, value in item.items():
                if (stuff == "fields"):
                    saved_papers.append(value)
    search_data = serializers.serialize( "python", historyHolder.objects.filter(user_id=this_user_id))
    for item in search_data:
        for key, value in item.items():
                if(key =="fields"):
                    if value not in search_history:
                        search_history.append(value)
                   



    return render(request, 'account.html', {"saved_papers" : saved_papers, "search_history" : search_history, "lensaved": len(saved_papers), "lenhist": len(search_history)})



def results(request):
    stop = set(stopwords.words('english'))
    user_id=request.user.id
    if cache.get('counter') is None:
        start_key = getstart()
        cache.set('counter', start_key, None)
        api_key = nextkey();
    else:
        api_key = nextkey();

    if request.GET.get('search_term'):
        #remove stop words
        message = request.GET['search_term']
        message = str([i for i in message.lower().split() if i not in stop])
        message = message[1:-1]
        message = message.replace("'", "")
        message = message.replace(",", "")
        if message == "":
            message = 'eggs'
        else:
            if(user_id is not None):
                query = historyHolder(user_id=user_id, searchQuery=request.GET.get('search_term'), dateAndTime=datetime.now())
                query.save()
    else:
        message = 'eggs'


    # Removes the \n newline character
    api_key = api_key[:len(api_key)-1]

    #absWordCount is a variable counting the number of times the first search time occurs in the abstract, likewise for titleWordCount but for title

    # Use the strategy defined in API_interface
    api_interface = api_strategy(Springer())
    api_results = api_interface.search(message, api_key)

    #frequency
    abstractString = ""
    titleString = ""
    for key, paper in api_results.items():
        abstractString += paper['abstract']
        titleString += paper['title']
    totalString = abstractString + titleString
    message = message.split()
    for term in message:
        totalString = totalString.replace(term, "")
    words = nltk.word_tokenize(totalString)
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if not word.isnumeric()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in stop]
    fdist = nltk.FreqDist(words).most_common(3)
    suggested_terms = []
    for word, frequency in fdist:
        suggested_terms.append(word)


    #print(api_results)
    today = "hello there"
    #if request contains url identifier

    if request.method == "POST":
        print(request.POST)
        print("gotem")
        paper_doi = request.POST.get('doi') # get the doi code from the post
        response_data = {}
        print("what's this bruh?", paper_doi)
        paper = api_results[paper_doi]      # find the specific paper information

        if paperHolder.objects.filter(doi=paper_doi).exists():
            print("Item already exists in database")
        else:
            p = paperHolder(doi=paper_doi, user_id=user_id, papername=paper['title'], url=paper['url'], date=paper['publicationDate'])
            p.save()


    return render(request, "results.html", {"api_results" : api_results, "today" : today, "search_term" : message, "suggested_terms" : suggested_terms, "lenapi": len(api_results)})
