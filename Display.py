# info_list is a list of list with 2 elements except for the first one which is the title of the table
# In each pair, the first element is String
# the second element can be String, List, Dictionary
# Case String: display it with a fixed width
# Case List: display en element in a line
# Case Dictionary: display the keys in the first line and values in the second with | in between
# For example, try to parse this list

test_list = [['Bill Gates(AUTHOR, BUSINESS_PERSON)'],
             ['Name', 'Bill Gates'],
             ['Description', 'William Henry "Bill" Gates III is an American business magnate, philanthropist, investor,\
                             computer programmer, and inventor. Gates originally established his reputation as the \
                             co-founder of Microsoft'],
             ['Sliblings', ['Libby Gates', 'Kristi Gates']],
             ['Leadership', {'Organization': 'Microsoft Corporation', 'Role': 'Chief Executive',
                             'Title': 'Chief Executive', 'From-To': '1975-04-04 - now'}]]

def draw_infobox(info_list):
    print "-----------------"
