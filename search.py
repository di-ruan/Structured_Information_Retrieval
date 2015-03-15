import json
import urllib

api_key = 'AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo'

query = 'blue bottle'
service_url1 = 'https://www.googleapis.com/freebase/v1/search'
params = {
    'query': query,
    'key': api_key
}
url = service_url1 + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for result in response['result']:
    print result['name'] + ' (' + str(result['score']) + ')'


service_url2 = 'https://www.googleapis.com/freebase/v1/topic'
topic_id = '/m/0d6lp'
params = {
    'key': api_key,
    'filter': 'suggest'
}
url = service_url2 + topic_id + '?' + urllib.urlencode(params)
topic = json.loads(urllib.urlopen(url).read())
for property in topic['property']:
    print property + ':'
    for value in topic['property'][property]['values']:
        print ' - ' + value['text']