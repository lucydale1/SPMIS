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

def count_occurrences(keyWord, countString):
    # print(keyWord)
    # print(countString)
    # print(countString.lower().split().count(keyWord))
    return countString.lower().split().count(keyWord)

class Springer(API):
    def search(self, message, api_key):
        keywords = 'keyword: ' + message                   # set user search term as keywork
        data = {'api_key': api_key, 'q': keywords, 'p': '100'}   # set request.get.data with the required fields

        # Save response from API
        response = requests.get("http://api.springer.com/metadata/json"
                                "", data)

        jr = response.json()
        api_results = [OrderedDict([('title', i['title']),
                                    ('abstract', i['abstract'][8:600]),
                                    ('publicationDate', i['publicationDate']),
                                    ('url', i['url'][0]['value']), ('titleWordCount', count_occurrences(message, i['title']))]) for i in
                                    jr["records"]]
        
        return api_results


class Scopus(API):
    def search(self, message, api_key):
        API_KEY = "1b1115545b64df3c0cefc15bb7baff8b"
        # API key temp. hardcoded, can change later.
        # Change 'count' in 'resp' in order to change num of articles returned.

        resp = requests.get("http://api.elsevier.com/content/search/scopus?query=SRCTITLE(networks) \
                            &field=dc:identifier,prism:issn,dc:title,citedby-count,prism:coverDate,dc:creator, \
                            prism:publicationName, dc:description&count=5",
                            headers={'Accept': 'application/json', 'X-ELS-APIKey': API_KEY})

        results = resp.json()
        # pprint(results['search-results']['entry'][0])

        Scopus_ids = []  # List of scopus_ids, actual data needed

        papers = [OrderedDict([('title', i['dc:title']),
                               ('abstract', 'none'[:200]),
                               ('publicationDate', i['prism:coverDate']),
                               ('url', i['prism:url']),
                               ('issn', i['prism:issn'])]) for i in results['search-results']['entry']]
        return papers;