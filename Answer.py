import json
import Search


def get_term(question):
    term = question[12:-1]
    return term


def get_author_query(term, type):
    if type == 'author':
        entity = '/book/author/book_editions_published'
    elif type == 'business_person':
        entity = '/organization/organization_founder/organizations_founded'
    elif type == 'art':
        entity = '/visual_art/visual_artist/artworks'
        entity_type = '/visual_art/visual_artist'
    dic = {
        entity: {"a:name": None, "name~=": term},
        "id": [{}],
        "name": [{}],
        "type": entity_type
    }
    query = json.dumps([dic])
    print query
    se = Search.get_engine('AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo')
    print se.get_mql_result(query)


def get_answer(result):
    answer = []
    return answer

#get_author_query('mona lisa', 'art')
