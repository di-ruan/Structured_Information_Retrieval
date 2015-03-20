import json
import Search


def get_term(question):
    term = question[12:]
    if term.endswith('?'):
        return term[:-1]
    return term


def get_query(term, type):
    if type == 'author':
        entity = '/book/author/works_written'
        entity_type = '/book/author'
    elif type == 'business_person':
        entity = '/organization/organization_founder/organizations_founded'
        entity_type = '/organization/organization_founder'
    elif type == 'art':
        entity = '/visual_art/visual_artist/artworks'
        entity_type = '/visual_art/visual_artist'
    dic = {
        entity: [{"a:name": None, "name~=": term}],
        "id": None,
        "name": None,
        "type": entity_type
    }
    query = json.dumps([dic])
    return query
    #se = Search.get_engine('AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo')
    #print se.get_mql_result(query)


def get_answer(results, type):
    answer = []
    if type == 'author':
        for result in results:
            name = result['name']
            book_list = []
            for org in result['/book/author/works_written']:
                book_list.append(org['a:name'])
            answer.append([name, 'Author',  book_list])
    elif type == 'business_person':
        for result in results:
            name = result['name']
            org_list = []
            for org in result['/organization/organization_founder/organizations_founded']:
                org_list.append(org['a:name'])
            answer.append([name, 'Business Person', org_list])
    return answer

#get_query('microsoft', 'business_person')
