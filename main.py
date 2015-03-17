import sys
import Search
import Analyser
import Display


def infobox(se, query):
    """
    infobox(search_engine, query)
    The function to generate infobox for the query
    """
    json = se.get_search_result(query)
    print json

    for element in json:
        topic_id = element['mid']
        print topic_id
        topic = se.get_topic_result(topic_id)
        print topic
        info_list = Analyser.build_infobox(topic)
        # Parse and analyze the topic
        # Get out of the loop if the topic is valid
        # Otherwise, continue to check the next topic
        if not info_list:
            Display.draw_infobox(info_list)
            break


def question(se, quest):
    """
    question(search_engine, question)
    The function to generate result for a question
    """
    # Analyze the question in the query first
    query = quest   # temp to do
    json = se.get_mql_result(query)


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
