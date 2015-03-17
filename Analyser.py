import Search
import re

entity_types = {'/people/person': 'Person',
                '/book/author': 'Author',
                '/film/actor': 'Actor',
                '/tv/tv_actor': 'Actor',
                '/organization/organization_founder': 'BusinessPerson',
                '/business/board_member': 'BusinessPerson',
                '/sports/sports_league': 'League',
                '/sports/sports_team': 'SportsTeam',
                '/sports/professional_sports_team': 'SportsTeam'}

interest = {'Person': ['Name', 'Birthday'],
            'Author': ['Books', 'Influenced'],
            'Actor': ['FilmsParticipated', 'Character'],
            'BusinessPerson': ['Leadership', 'BoardMember'],
            'League': ['Name', 'Championship'],
            'SportsTeam': ['Name', 'Description']}

# the input is the result from the Search API
def build_infobox(results):
    if results is not None:
        for result in results['result']:
            mid = result['mid']
            count = 0
            res_list = []
            topic = Search.get_search_result(mid)
            for p in topic['property']:
                entity_type = get_prefix(p)
                if entity_types[entity_type] is not None:
                    count += 1
                    for value in topic['property'][entity_type]['values']:
                        res_list.append([entity_types[entity_type], value['text']])
            if count > 0:
                return res_list
    return []


def get_prefix(entity_type):
    res = re.search('/[a-z_]+/[a-z_]+', entity_type)
    return res.group(0)