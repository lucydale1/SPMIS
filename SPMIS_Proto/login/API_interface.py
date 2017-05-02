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

# def count_occurrences(keyWord, string):
#     if " " in keyWord:
#         keyWord = keyWord.split()
#     return string.lower().split().count(keyWord)

class Springer(API):

    # @staticmethod
    def search(self, message, api_key):
        # print(message)
        # print(api_key)
        keywords = 'keyword: ' + message                   # set user search term as keywork
        data = {'api_key': api_key, 'q': keywords, 'p': '10'}   # set request.get.data with the required fields

        # Save response from API
        response = requests.get("http://api.springer.com/metadata/json"
                                "", data)

        jr = response.json()
        api_results = [OrderedDict([('title', i['title']),
                                    ('abstract', i['abstract'][8:600]),
                                    ('publicationDate', i['publicationDate']),
                                    ('url', i['url'][0]['value'])]) for i in
                                    jr["records"]]

        return api_results