import sys
import Search
import Analyser
import Display
import Answer
from operator import itemgetter


# implement the logic to create the infobox. First, we need to get mi from Freebase Search API. And then iterate
# each mi to get the first one that contains satisfies our requirement and then print the infobox.
def infobox(se, query):
    """
    infobox(search_engine, query)
    The function to generate infobox for the query
    """
    json = se.get_search_result(query)
    if json is None:
        print 'Error in search'
        return

    info_list = None

    for element in json:
        topic_id = element['mid']
        topic = se.get_topic_result(topic_id)
        if topic is None:
            continue

        # Parse and analyze the topic
        # Get out of the loop if the topic is valid
        # Otherwise, continue to check the next topic
        title = query.title()
        info_list = Analyser.build_infobox(topic, title)
        if len(info_list) > 0:  # Nonempty result
            # print info_list
            break

    if info_list is None:
        print 'There is no result for \'' + query + '\'!'
    else:
        Display.draw_infobox(info_list)


# implement the logic to create the answer table. Since we are only interested in the AnswerType such as Author
# and BusinessPerson. We can create queries for those two type and get the result.
def question(se, question):
    """
    question(search_engine, question)
    The function to generate result for a question
    """
    # Analyze the question in the query first
    term = Answer.get_term(question)
    author_query = Answer.get_query(term, 'author')
    business_person_query = Answer.get_query(term, 'business_person')
    author_result = se.get_mql_result(author_query)
    if author_result is None:
        print 'Error in author search'
        return
    business_person_result = se.get_mql_result(business_person_query)
    if business_person_result is None:
        print 'Error in business person search'
        return
    author_answer = Answer.get_answer(author_result, 'author')
    business_person_answer = Answer.get_answer(business_person_result, 'business_person')
    author_answer.extend(business_person_answer)
    if author_answer:
        author_answer = sorted(author_answer, key=itemgetter(0))
        if not question.endswith('?'):
            question = question + '?'
        Display.draw_answer(author_answer, question)


# entry of the program
def main(argv):
    """
    main(argv)
    The entry point of the application
    The input format should be: <API key> <infobox/question> <query>
    """
    # API key
    if argv[0] == 'test':
        # Use the default key
        api_key = 'AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo'
    else:
        api_key = argv[0]

    # Source: normal, file, or interact
    if argv[1] == 'normal' or argv[1] == 'file' or argv[1] == 'interact':
        source = argv[1]
    else:
        print 'Source should be \"normal\", \"file\", or \"interact\"'
        return

    # Mode: infobox or question
    if source != 'interact':
        if argv[2] == 'infobox' or argv[2] == 'question':
            mode = argv[2]
        else:
            print 'Type should be either \"infobox\" or \"question\"'
            return

    # Get the search engine object with the given API key
    se = Search.get_engine(api_key)

    if source == 'normal':
        query = ' '.join(argv[3:])
        if mode == 'question':
            question(se, query)
        else:
            infobox(se, query)
    elif source == 'file':
        qfile = open(argv[3], 'r')
        for line in qfile:
            if line.endswith('\n'):
                line = line[0:-1]
            if mode == 'question':
                question(se, line)
            else:
                infobox(se, line)
    else:   # Interact
        query = ''
        while True:
            try:
                query = raw_input('Anything curious? ')
                print 'Searching...'
                if query.endswith('?'):
                    question(se, query)
                else:
                    infobox(se, query)
            except KeyboardInterrupt:
                print 'Byt~'
                break


if __name__ == "__main__":
    main(sys.argv[1:])
