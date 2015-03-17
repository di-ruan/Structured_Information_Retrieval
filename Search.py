import json
import urllib


class Search:

    # api_key = 'AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo'
    service_url_search = 'https://www.googleapis.com/freebase/v1/search'
    service_url_topic = 'https://www.googleapis.com/freebase/v1/topic'
    service_url_mql = 'https://www.googleapis.com/freebase/v1/mqlread'

    def __init__(self, api_key):
        self.api_key = api_key

    # return the result of the Freebase Search API
    @staticmethod
    def get_search_result(self, query):
        # query = 'bill gates'
        params = {
            'query': query,
            'key': self.api_key
        }
        url = self.service_url_search + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        return response['result']

    # return the result of the Freebase Topic API
    @staticmethod
    def get_topic_result(self, topic_id):
        # topic_id = '/m/0d6lp'
        params = {
            'key': self.api_key,
            'filter': 'suggest'
        }
        url = self.service_url_topic + topic_id + '?' + urllib.urlencode(params)
        topic = json.loads(urllib.urlopen(url).read())

    # return the result of the Freebase MQL API
    @staticmethod
    def get_mql_result(self, query):
        # query = = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]
        params = {
            'query': json.dump(query),
            'key': self.api_key
        }
        url = self.service_url_mql + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        return response['result']