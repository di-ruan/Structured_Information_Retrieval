import sys
import Search
import Analyser
import Display
import Answer


def infobox(se, query):
    """
    infobox(search_engine, query)
    The function to generate infobox for the query
    """
    q = ' '.join(query)
    json = se.get_search_result(q)

    info_list = None

    for element in json:
        topic_id = element['mid']
        topic = se.get_topic_result(topic_id)

        # Parse and analyze the topic
        # Get out of the loop if the topic is valid
        # Otherwise, continue to check the next topic
        title = ' '.join(query).title()
        info_list = Analyser.build_infobox(topic, title)
        if len(info_list) > 0:  # Nonempty result
            print info_list
            break

    if info_list is None:
        print 'There is no result for \'' + q + '\'!'
    else:
        Display.draw_infobox(info_list)


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
    business_person_result = se.get_mql_result(business_person_query)
    author_answer = Answer.get_answer(author_result, 'author')
    business_person_answer = Answer.get_answer(business_person_result, 'business_person')
    author_answer.extend(business_person_answer)

    Display.draw_answer(author_answer, question)



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

    # Mode: infobox or question
    if argv[1] == 'infobox' or argv[1] == 'question':
        mode = argv[1]
    else:
        print 'Type should be either \"infobox\" or \"question\"'
        return

    # Query
    query = argv[2:]

    # Get the search engine object with the given API key
    se = Search.get_engine(api_key)

    if mode == 'question':
        question(se, query)
    else:
        infobox(se, query)

if __name__ == "__main__":
    main(sys.argv[1:])
