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
Properties of Interest
Person
        Name                        "/type/object/name"
        Birthday                    "/people/person/date_of_birth"
        Place of Birth              "/people/person/place_of_birth"
        Death(Place, Date, Cause)   ?
        Siblings                    "/people/person/sibling_s"
        Spouses                     "/people/person/spouse_s"
        Description                 "/common/topic/description"

Author
        Books(Title)                    "/book/author/book_editions_published"
        Book About the Author(Title)    "/book/book_subject/works"
        Influenced                      "/influence/influence_node/influenced"
        Influenced by                   ?

Actor
        FilmsParticipated(Film Name, Character)     "/film/actor/film"

BusinessPerson
        Leadership(From, To, Organization, Role, Title)     "/business/board_member/leader_of"
        BoardMember(From, To, Organization, Role, Title)    "/business/board_member/organization_board_memberships"
        Founded(OrganizationName)                           "/organization/organization_founder/organizations_founded"

League
        Name                "/type/object/name"
        Championship        "/sports/sports_league/championship"
        Sport               "/sports/sports_league/sport"
        Slogan              "/organization/organization/slogan"
        OfficialWebsite     "/common/topic/official_website"
        Description         "/common/topic/description"
        Teams               "/sports/sports_league/teams"

SportsTeam
        Name                                            "/type/object/name"
        Description                                     "/common/topic/description"
        Sport                                           "/sports/sports_team/sport"
        Arena                                           "/sports/sports_team/arena_stadium"
        Championships                                   "/sports/sports_team/championships"
        Coaches(Name, Position, From, To)               "/sports/sports_team/coaches"
        Founded                                         "/sports/sports_team/founded"
        Leagues                                         "/sports/sports_team/league"
        Locations                                       "/sports/sports_team/location"
        PlayersRoster(Name, Position, Number, From, To) "/sports/sports_team/roster"
"""

interest = {'/people/person': ['Name', 'date_of_birth', 'place_of_birth', 'death', 'sibling_s', 'spouse_s',
                               'description'],
            '/book/author': ['book_editions_published', 'Influenced'],
            '/film/actor': ['FilmsParticipated', 'Character'],
            '/organization/organization_founder': ['organizations_founded', 'BoardMember'],
            '/business/board_member': ['organizations_founded', 'organization_board_memberships'],
            '/sports/sports_league': ['Name', 'Championship'],
            '/sports/sports_team': ['Name', 'Description'],
            '/sports/professional_sports_team': ['Name', 'Description']}


# the input is the result from the Topic API
def build_infobox(topic):
    info_list = []
    types
    for p in topic:
        entity_type = get_prefix(p)
        if entity_type == '/people/person':
            info_list.append(get_person())
        if entity_type == '/book/author':
            for value in topic[p]['values']:
                info_list.append([entity_types[entity_type], value['text']])
    return info_list


def get_prefix(entity_type):
    res = re.search('/[a-z_]+/[a-z_]+', entity_type)
    return res.group(0)


def get_person():
