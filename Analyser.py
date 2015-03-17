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

"""
Type of Entity
Properties of Interest
Person	Name, Birthday, Place of Birth, Death(Place, Date, Cause), Siblings, Spouses, Description
Author	Books(Title), Book About the Author(Title), Influenced, Influenced by
Actor	FilmsParticipated(Film Name, Character)
BusinessPerson	Leadership(From, To, Organization, Role, Title), BoardMember(From, To, Organization, Role, Title),
        Founded(OrganizationName)
League	Name, Championship, Sport, Slogan, OfficialWebsite, Description, Teams
SportsTeam	Name, Description, Sport, Arena, Championships, Coaches(Name, Position, From, To), Founded, Leagues,
        Locations, PlayersRoster(Name, Position, Number, From, To)
"""

interest = {'/people/person': ['Name', 'date_of_birth', 'place_of_birth', 'death', 'sibling_s', 'spouse_s',
                               'description'],
            '/book/author': ['book_editions_published', 'Influenced'],
            '/film/actor': ['FilmsParticipated', 'Character'],
            '/organization/organization_founder': ['organizations_founded', 'BoardMember'],
            '/business/board_member': ['organizations_founded', 'BoardMember'],
            '/sports/sports_league': ['Name', 'Championship'],
            '/sports/sports_team': ['Name', 'Description'],
            '/sports/professional_sports_team': ['Name', 'Description']}


# the input is the result from the Topic API
def build_infobox(topic):
    info_list = []
    for p in topic['property']:
        entity_type = get_prefix(p)
        if entity_types[entity_type] is not None:
            for value in topic['property'][entity_type]['values']:
                info_list.append([entity_types[entity_type], value['text']])
    return info_list


def get_prefix(entity_type):
    res = re.search('/[a-z_]+/[a-z_]+', entity_type)
    return res.group(0)