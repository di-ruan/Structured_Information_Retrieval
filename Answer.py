import re
import json


def get_term(question):
    term = ''
    return term

def get_author_query(term, type):
    query = []
    if type == 'author':
        entity = 'author'
    elif type == 'business_person':
        entity = 'business_person'
    return query

def get_answer(result):
    answer = []
    return answer