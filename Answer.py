import json


# get the term for query from the question asked by user
def get_term(question):
    term = question[12:]
    if term.endswith('?'):
        return term[:-1]
    return term


# form the query for Freebase MQL API
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


# analyse the result from the Freebase MQL API and get desired information for the answer table
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

