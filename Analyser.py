import Search

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


def build_infobox(self, results):
    mids = []
    if results is not None:
        for result in results['result']:
            mids.append(result['mid'])
    for mid in mids:
        topic = Search.get_search_result(mid)
        topic['property']