import Search


class Analyser:

    entity_types = {'/people/person': 'Person',
                    '/book/author': 'Author',
                    '/film/actor': 'Actor',
                    '/tv/tv_actor': 'Actor',
                    '/organization/organization_founder': 'BusinessPerson',
                    '/business/board_member': 'BusinessPerson',
                    '/sports/sports_league': 'League',
                    '/sports/sports_team': 'SportsTeam',
                    '/sports/professional_sports_team': 'SportsTeam'}


    @staticmethod
    def get_mids(self, results):
        return_list = []
        if results is not None:
            for result in results['result']:
                return_list.append(result['mid'])
        return return_list

    @staticmethod
    def get_(self, mids):
        if mids is not None:
            for mid in mids:
                topic = Search.get_search_result(mid)
                topic['property']