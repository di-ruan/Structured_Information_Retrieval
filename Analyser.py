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
def build_infobox(topic, title):
    info_list = []
    entity_list = []
    for p in topic:
        entity_type = get_prefix(p)
        entity_list.append(entity_type)
    entities = ''
    if '/people/person' in entity_list:
        info_list.extend(get_person(topic))
        entities += 'PERSON, '
    if '/book/author' in entity_list:
        info_list.extend(get_author(topic))
        entities += 'AUTHOR, '
    if ('/film/actor' in entity_list) or ('/tv/tv_actor' in entity_list):
        info_list.extend(get_actor(topic))
        entities += 'ACTOR, '
    if ('/organization/organization_founder' in entity_list) or ('/business/board_member' in entity_list):
        info_list.extend(get_business(topic))
        entities += 'BUSINESS_PERSON, '
    if '/sports/sports_league' in entity_list:
        info_list.extend(get_league(topic))
        entities += 'LEAGUE, '
    if ('/sports/professional_sports_team' in entity_list) or ('/sports/sports_team' in entity_list):
        info_list.extend(get_team(topic))
        entities += 'SPORTS TEAM, '
    if entities:
        info_list.insert(0, [1, str(title) + '(' + str(entities[:-2]) + ')'])
    return info_list


def get_prefix(entity_type):
    res = re.search('/[a-z_]+/[a-z_]+', entity_type)
    return res.group(0)


def get(entity, paths):
    if entity is not None:
        for path in paths:
            if path == 0 and entity:
                entity = entity[0]
            elif entity and entity.get(path) is not None:
                entity = entity.get(path)
            else:
                entity = ''
                break
    return entity

"""
Person
        Name                        "/type/object/name"
        Birthday                    "/people/person/date_of_birth"
        Place of Birth              "/people/person/place_of_birth"
        Death(Place, Date, Cause)   ?
        Description                 "/common/topic/description"
        Siblings                    "/people/person/sibling_s"
        Spouses                     "/people/person/spouse_s"
"""


def get_person(topic):
    info_list = list()
    info_list.append([2, "Name", get(topic, ["/type/object/name", "values", 0, "text"])])
    info_list.append([2, "Birthday", get(topic, ["/people/person/date_of_birth", "values", 0, "text"])])
    info_list.append([2, "Place of Birth", get(topic, ["/people/person/place_of_birth", "values", 0, "text"])])
    info_list.append([2, "Descriptions", get(topic, ["/common/topic/description", "values", 0, "value"])])
    if get(topic, ["/people/person/sibling_s"]):
        sibling_list = []
        for value in get(topic, ["/people/person/sibling_s", "values"]):
            sibling_list.append(get(value, ['property', '/people/sibling_relationship/sibling', 'values', 0, 'text']))
        info_list.append([3, "Siblings", sibling_list])
    if get(topic, ["/people/person/spouse_s"]):
        spouse_list = []
        for value in get(topic, ["/people/person/spouse_s", "values"]):
            spouse_name = get(value, ['property', '/people/marriage/spouse', 'values', 0, 'text'])
            spouse_from = get(value, ['property', '/people/marriage/from', 'values', 0, 'text'])
            if get(value, ['property', '/people/marriage/from', '/people/marriage/to', 'values', 0, 'text']):
                spouse_to = get(value, ['property', '/people/marriage/from', '/people/marriage/to',
                                        'values', 0, 'text'])
            else:
                spouse_to = 'now'
            spouse_location = get(value, ['property', '/people/marriage/location_of_ceremony', 'values', 0, 'text'])
            spouse_list.append(spouse_name + ' (' + spouse_from + ' - ' + spouse_to + ' ) @ ' + spouse_location)
        info_list.append([3, "Spouses", spouse_list])
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
    if get(topic, ["/book/author/works_written"]):
        book_list = []
        for value in get(topic, ["/book/author/works_written", "values"]):
            book_list.append(value['text'])
        info_list.append([3, "Books", book_list])
    if get(topic, ["/book/book_subject/works"]):
        book_about_list = []
        for value in get(topic, ["/book/book_subject/works", "values"]):
            book_about_list.append(value['text'])
        info_list.append([3, "Books about", book_about_list])
    if get(topic, ["/influence/influence_node/influenced"]):
        influenced_list = []
        for value in get(topic, ["/influence/influence_node/influenced", "values"]):
            influenced_list.append(value['text'])
        info_list.append([3, "Influenced", influenced_list])
    if get(topic, ["/influence/influence_node/influenced_by"]):
        influenced_by_list = []
        for value in get(topic, ["/influence/influence_node/influenced_by", "values"]):
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
    for film in get(topic, ["/film/actor/film", 'values']):
        character_list.append(get(film, ['property', '/film/performance/character', 'values', 0, 'text']))
        film_name_list.append(get(film, ['property', '/film/performance/film', 'values', 0, 'text']))
    if character_list or film_name_list:
        info_list.append([4, "Films", [['Character', 'Film Name'],  character_list, film_name_list]])
    return info_list

"""
BusinessPerson
        Founded                                             "/organization/organization_founder/organizations_founded"
        Leadership(Organization, Role, Title, From/To)      "/business/board_member/leader_of"
        Board Member(Organization, Role, Title, From/To)    "/business/board_member/organization_board_memberships"
"""


def get_business(topic):
    info_list = list()
    if get(topic, ["/organization/organization_founder/organizations_founded"]):
        founded_list = []
        for value in get(topic, ["/organization/organization_founder/organizations_founded", "values"]):
            founded_list.append(value['text'])
        info_list.append([3, "Founded", founded_list])
    if get(topic, ['/business/board_member/leader_of']):
        organization_list = []
        role_list = []
        title_list = []
        date_list = []
        for organization in get(topic, ['/business/board_member/leader_of', 'values']):
            organization_list.append(get(organization, ['property', '/organization/leadership/organization',
                                                        'values', 0, 'text']))
            role_list.append(get(organization, ['property', '/organization/leadership/role',
                                                'values', 0, 'text']))
            title_list.append(get(organization, ['property', '/organization/leadership/title',
                                                 'values', 0, 'text']))
            from_date = get(organization, ['property', '/organization/leadership/from', 'values', 0, 'text'])
            to_date = get(organization, ['property', '/organization/leadership/to', 'values', 0, 'text'])
            date_list.append(from_date + ' / ' + to_date)
        if organization_list or role_list or title_list or date_list:
            info_list.append([4, "Leadership", [['Organization', 'Role', 'Title', 'From/To'], organization_list,
                                                role_list, title_list, date_list]])
    if topic.get("/business/board_member/organization_board_memberships"):
        organization_list = []
        role_list = []
        title_list = []
        date_list = []
        for member in get(topic, ["/business/board_member/organization_board_memberships", 'values']):
            organization_list.append(get(member, ['property',
                                                  '/organization/organization_board_membership/organization',
                                                  'values', 0, 'text']))
            role_list.append(get(member, ['property', '/organization/organization_board_membership/role',
                                          'values', 0, 'text']))
            title_list.append(get(member, ['property', '/organization/organization_board_membership/title',
                                           'values', 0, 'text']))
            from_date = get(member, ['property', '/organization/organization_board_membership/from',
                                     'values', 0, 'text'])
            to_date = get(member, ['property', '/organization/organization_board_membership/to',
                                   'values', 0, 'text'])
            date_list.append(from_date + ' / ' + to_date)
        if organization_list or role_list or title_list or date_list:
            info_list.append([4, "Leadership", [['Organization', 'Role', 'Title', 'From/To'], organization_list,
                                                role_list, title_list, date_list]])
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
    info_list.append([2, "Name", get(topic, ["/type/object/name", "values", 0, "text"])])
    info_list.append([2, "Sport", get(topic, ["/sports/sports_league/sport", "values", 0, "text"])])
    info_list.append([2, "Slogan", get(topic, ["/organization/organization/slogan", "values", 0, "text"])])
    info_list.append([2, "Official Website", get(topic, ["/common/topic/official_website", "values", 0, "text"])])
    info_list.append([2, "Championship", get(topic, ["/sports/sports_league/championship", "values", 0, "text"])])
    if get(topic, ["/sports/sports_league/teams"]):
        team_list = []
        for value in get(topic, ["/sports/sports_league/teams", "values"]):
            team_list.append(get(value, ['property', '/sports/sports_league_participation/team', 'values', 0, 'text']))
        info_list.append([3, "Teams", team_list])
    info_list.append([2, "Description", get(topic, ["/common/topic/description", "values", 0, "value"])])
    return info_list

"""
SportsTeam
        Name                                            "/type/object/name"
        Sport                                           "/sports/sports_team/sport"
        Arena                                           "/sports/sports_team/arena_stadium"
        Championships                                   "/sports/sports_team/championships"
        Founded                                         "/sports/sports_team/founded"
        Leagues                                         "/sports/sports_team/league"
        Locations                                       "/sports/sports_team/location"
        Coaches(Name, Position, From/To)                "/sports/sports_team/coaches"
        PlayersRoster(Name, Position, Number, From/To)  "/sports/sports_team/roster"
        Description                                     "/common/topic/description"
"""


def get_team(topic):
    info_list = list()
    info_list.append([2, "Name", get(topic, ["/type/object/name", "values", 0, "text"])])
    info_list.append([2, "Sport", get(topic, ["/sports/sports_team/sport", "values", 0, "text"])])
    info_list.append([2, "Arena", get(topic, ["/sports/sports_team/arena_stadium", "values", 0, "text"])])
    if get(topic, ["/sports/sports_team/championships"]):
        championships_list = []
        for value in get(topic, ["/sports/sports_team/championships", "values"]):
            championships_list.append(value['text'])
        info_list.append([3, "Championships", championships_list])
    info_list.append([2, "Founded", get(topic, ["/sports/sports_team/founded", "values", 0, "text"])])
    info_list.append([2, "Leagues", get(topic, ["/sports/sports_team/league", "values", 0, 'property',
                                                '/sports/sports_league_participation/league','values', 0,"text"])])
    info_list.append([2, "Locations", get(topic, ["/sports/sports_team/location", "values", 0, "text"])])
    if get(topic, ["/sports/sports_team/coaches"]):
        name_list = []
        position_list = []
        date_list = []
        for coach in get(topic, ["/sports/sports_team/coaches",'values']):
            name_list.append(get(coach, ['property', '/sports/sports_team_coach_tenure/coach', 'values', 0, 'text']))
            position_list.append(get(coach, ['property', '/sports/sports_team_coach_tenure/position', 'values',
                                             0, 'text']))
            from_date = get(coach, ['property', '/sports/sports_team_coach_tenure/from', 'values', 0, 'text'])
            to_date = get(coach, ['property', '/sports/sports_team_coach_tenure/to', 'values', 0, 'text'])
            date_list.append(from_date + ' / ' + to_date)
        if name_list or position_list or date_list:
            info_list.append([4, "Coaches", [['Name', 'Position', 'From/To'], name_list, position_list, date_list]])
    if get(topic, ["/sports/sports_team/roster"]):
        name_list = []
        position_list = []
        number_list = []
        date_list = []
        for player in get(topic, ["/sports/sports_team/roster", 'values']):
            name_list.append(get(player, ['property', '/sports/sports_team_roster/player', 'values', 0, 'text']))
            positions = ''
            for position in get(player, ['property', '/sports/sports_team_roster/position', 'values']):
                positions += position['text'] + ', '
            position_list.append(positions[:-2])
            number_list.append(get(player, ['property', '/sports/sports_team_roster/number', 'values', 0, 'text']))
            from_date = get(player, ['property', '/sports/sports_team_roster/from', 'values', 0, 'text'])
            to_date = get(player, ['property', '/sports/sports_team_roster/to', 'values', 0, 'text'])
            date_list.append(from_date + ' / ' + to_date)
        if name_list or position_list or number_list or date_list:
            info_list.append([4, "PlayersRoster", [['Name', 'Position', 'Number', 'From/To'],  name_list, position_list,
                                                   number_list, date_list]])
    info_list.append([2, "Description", get(topic, ["/common/topic/description", "values", 0, "value"])])
    return info_list
