import sys
import Search

def main(argv):
    """
    main(argv)
    The entry point of the application
    """
    if len(argv) == 2:
        if argv[0] == 'test':
            # Use the default key
            api_key = 'AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo'
            query = argv[1:]
        else:
            api_key = argv[0]
            query = argv[1:]
    else:
        print 'Usage: <key> <query>'
        return

    se = Search.get_engine(api_key)
    json = se.get_search_result(query)
    print json

    for element in json:
        topic_id = element['mid']
        print topic_id
        topic = se.get_topic_result(topic_id)
        print topic
        # Parse and analyze the topic, break if it is valid
        if True:
            break

if __name__ == "__main__":
    main(sys.argv[1:])
