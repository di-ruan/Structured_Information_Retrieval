import json
import urllib


def get_engine(api_key):
    return Search(api_key)


class Search:

    service_url_search = 'https://www.googleapis.com/freebase/v1/search'
    service_url_topic = 'https://www.googleapis.com/freebase/v1/topic'
    service_url_mql = 'https://www.googleapis.com/freebase/v1/mqlread'

    def __init__(self, api_key):
        self.api_key = api_key

    # call Freebase Search API and return the result
    def get_search_result(self, query):
        """
        get_search_result(query)
        Object method to get the search result via Freebase Search API
        """
        params = {
            'query': query,
            'key': self.api_key
        }
        url = self.service_url_search + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        if not response.has_key('result'):
            return None
        return response['result']

    # call Freebase Topic API and return the result
    def get_topic_result(self, topic_id):
        """
        get_topic_result(topic_id)
        Object method to get the topic result via Freebase Topic API
        """
        params = {
            'key': self.api_key
        }
        url = self.service_url_topic + topic_id + '?' + urllib.urlencode(params)
        topic = json.loads(urllib.urlopen(url).read())
        if not topic.has_key('property'):
            return None
        return topic['property']

    # call Freebase MQL API and return the result
    def get_mql_result(self, query):
        """
        get_mql_result(query)
        Object method to get the search result via Freebase MQL API
        """
        params = {
            'query': query,
            'key': self.api_key
        }
        url = self.service_url_mql + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())
        if not response.has_key('result'):
            return None
        return response['result']
