import requests # Used to send HTTP requests to the API
from collections import OrderedDict

class api_strategy:
    def __init__(self, func=None):
        if func:
            self.method= func

    def search(self, search_terms, api_key):
        return self.method.search(search_terms, api_key)


# the interface which all the API strategies must inherit from
class API:
    def search(self):
        pass

def rankPapers(api_results, searchTerms):

    for key, paper in api_results.items():
        c=0
        for term in searchTerms.split():
            c += paper['abstract'].lower().split().count(term)
            c += 2*(paper['title'].lower().split().count(term))
        paper['relevancyNum'] = c

    print(api_results)

    api_results = OrderedDict(api_results)
    # api_results = sorted(api_results, key=lambda k: k['relevancyNum'], reverse=True)
    api_results = OrderedDict(sorted(api_results.items(), key=lambda k: k[1]['relevancyNum'], reverse=True))
    print(api_results)

    return api_results

   # return

class Springer(API):
    def search(self, message, api_key):
        keywords = 'keyword: ' + message                   # set user search term as keywork
        data = {'api_key': api_key, 'q': keywords, 'p': '100'}   # set request.get.data with the required fields

        # Save response from API
        response = requests.get("http://api.springer.com/metadata/json"
                                "", data)

        jr = response.json()
        api_results = {i['doi']: OrderedDict([('title', i['title']),
                                    ('abstract', i['abstract'][8:600]),
                                    ('publicationDate', i['publicationDate']),
                                    ('url', i['url'][0]['value']),
                                    ('doi', i['doi'])]) for i in
                                    jr["records"]}


        return rankPapers(api_results, message)
