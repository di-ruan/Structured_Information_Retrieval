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
    entity_set = set()
    for p in topic:
        entity_type = get_prefix(p)
        entity_set.add(entity_type)
    if '/people/person' in entity_set:
        info_list.extend(get_person(topic))
    if '/book/author' in entity_set:
        info_list.extend(get_author(topic))
    if ('/film/actor' in entity_set) or ('/tv/tv_actor' in entity_set):
        info_list.extend(get_actor(topic))
    if ('/organization/organization_founder' in entity_set) or ('/business/board_member' in entity_set):
        info_list.extend(get_business(topic))
    if '/sports/sports_league' in entity_set:
        info_list.extend(get_league(topic))
    if ('/sports/professional_sports_team' in entity_set) or ('/sports/sports_team' in entity_set):
        info_list.extend(get_team(topic))
    return info_list


def get_prefix(entity_type):
    res = re.search('/[a-z_]+/[a-z_]+', entity_type)
    return res.group(0)

"""
Person
        Name                        "/type/object/name"
        Birthday                    "/people/person/date_of_birth"
        Place of Birth              "/people/person/place_of_birth"
        Death(Place, Date, Cause)   ?
        Siblings                    "/people/person/sibling_s"
        Spouses                     "/people/person/spouse_s"
        Description                 "/common/topic/description"
"""


def get_person(topic):
    info_list = list()
    info_list.append([2, "Name", topic["/type/object/name"]["values"][0]["text"]])
    info_list.append([2, "Birthday", topic["/people/person/date_of_birth"]["values"][0]["text"]])
    info_list.append([2, "Place of Birth", topic["/people/person/place_of_birth"]["values"][0]["text"]])
    if not topic["/people/person/sibling_s"]:
        sibling_list = []
        for value in topic["/people/person/sibling_s"]["values"]:
            sibling_list.append(value['property']['/people/sibling_relationship/sibling']['values'][0]['text'])
        info_list.append([3, "Siblings", sibling_list])
    if not topic["/people/person/spouse_s"]:
        spouse_list = []
        for value in topic["/people/person/spouse_s"]["values"]:
            spouse_name = value['property']['/people/marriage/spouse']['values'][0]['text']
            spouse_from = value['property']['/people/marriage/from']['values'][0]['text']
            if value['property']['/people/marriage/from']['/people/marriage/to']['count'] == 0:
                spouse_to = 'now'
            else:
                spouse_to = value['property']['/people/marriage/from']['/people/marriage/to']['values'][0]['text']
            spouse_location = value['property']['/people/marriage/location_of_ceremony']['values'][0]['text']
            spouse_list.append(spouse_name + ' (' + spouse_from + ' - ' + spouse_to + ' ) @ ' + spouse_location)
        info_list.append([3, "Spouses", spouse_list])
    info_list.append([2, "Descriptions", topic["/common/topic/description"]["values"][0]["value"]])
    return info_list

"""
Author
        Books(Title)                    "/book/author/works_written"
        Book About the Author(Title)    "/book/book_subject/works"
        Influenced                      "/influence/influence_node/influenced"
        Influenced by                   ?
"""


def get_author(topic):
    info_list = list()
    if not topic["/book/author/works_written"]:
        book_list = []
        for value in topic["/book/author/works_written"]["values"]:
            book_list.append(value['text'])
        info_list.append([3, "Books", book_list])
    if not topic["/book/book_subject/works"]:
        book_about_list = []
        for value in topic["/book/book_subject/works"]["values"]:
            book_about_list.append(value['text'])
        info_list.append([3, "Books about", book_about_list])
    if not topic["/influence/influence_node/influenced"]:
        influenced_list = []
        for value in topic["/influence/influence_node/influenced"]["values"]:
            influenced_list.append(value['text'])
        info_list.append([3, "Influenced", influenced_list])
    if not topic["/influence/influence_node/influenced_by"]:
        influenced_by_list = []
        for value in topic["/influence/influence_node/influenced_by"]["values"]:
            influenced_by_list.append(value['text'])
        info_list.append([3, "Influenced by", influenced_by_list])
    return info_list

"""
Actor
        FilmsParticipated(Film Name, Character)     "/film/actor/film"
"""


def get_actor(topic):
    info_list = []
    character_list = []
    film_name_list = []
    for film in topic["/film/actor/film"]['values']:
        character_list.append(film['property']['/film/performance/character']['values'][0]['text'])
        film_name_list.append(film['property']['/film/performance/film']['values'][0]['text'])
    if (not character_list) or (not film_name_list):
        info_list.append([4, "Films", ['Character', character_list, 'Film Name', film_name_list]])
    return info_list

"""
BusinessPerson
        Leadership(From, To, Organization, Role, Title)     "/business/board_member/leader_of"
        BoardMember(From, To, Organization, Role, Title)    "/business/board_member/organization_board_memberships"
        Founded(OrganizationName)                           "/organization/organization_founder/organizations_founded"
"""


def get_business(topic):
    info_list = list()
    return info_list

"""
League
        Name                "/type/object/name"
        Sport               "/sports/sports_league/sport"
        Slogan              "/organization/organization/slogan"
        Official Website    "/common/topic/official_website"
        Championship        "/sports/sports_league/championship"
        Teams               "/sports/sports_league/teams"
        Description         "/common/topic/description"
"""


def get_league(topic):
    info_list = list()
    info_list.append([2, "Name", topic["/type/object/name"]["values"][0]["text"]])
    info_list.append([2, "Sport", topic["/sports/sports_league/sport"]["values"][0]["text"]])
    info_list.append([2, "Slogan", topic["/organization/organization/slogan"]["values"][0]["text"]])
    info_list.append([2, "Official Website", topic["/common/topic/official_website"]["values"][0]["text"]])
    info_list.append([2, "Championship", topic["/sports/sports_league/championship"]["values"][0]["text"]])
    if not topic["/sports/sports_league/teams"]:
        team_list = []
        for value in topic["/sports/sports_league/teams"]["values"]:
            team_list.append(value['property']['/sports/sports_league_participation/team']['values'][0]['text'])
        info_list.append([3, "Teams", team_list])
    info_list.append([2, "Description", topic["/common/topic/description"]["values"][0]["value"]])
    return info_list

"""
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


def get_team(topic):
    info_list = list()
    info_list.append([2, "Name", topic["/type/object/name"]["values"][0]["text"]])
    info_list.append([2, "Sport", topic["/sports/sports_league/sport"]["values"][0]["text"]])
    info_list.append([2, "Slogan", topic["/organization/organization/slogan"]["values"][0]["text"]])
    info_list.append([2, "Official Website", topic["/common/topic/official_website"]["values"][0]["text"]])
    info_list.append([2, "Championship", topic["/sports/sports_league/championship"]["values"][0]["text"]])
    if not topic["/sports/sports_league/teams"]:
        team_list = []
        for value in topic["/sports/sports_league/teams"]["values"]:
            team_list.append(value['property']['/sports/sports_league_participation/team']['values'][0]['text'])
        info_list.append([3, "Teams", team_list])
    info_list.append([2, "Description", topic["/common/topic/description"]["values"][0]["value"]])
    return info_list