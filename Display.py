import textwrap

W = 100
T = '+--------------------------------------------------------------------------------------------------+'
H = '+-------------------+------------------------------------------------------------------------------+'
V = '|'
WS = ' '
W_LEFT = 20
W_BODY = 80

# info_list is a list of list with 2 elements except for the first one which is the title of the table
# In each pair, the first element is String
# the second element can be String, List, Dictionary
# Case String: display it with a fixed width
# Case List: display en element in a line
# Case Dictionary: display the keys in the first line and values in the second with | in between
# For example, try to parse this list

test_list = [[1, 'Bill Gates(AUTHOR, BUSINESS_PERSON)'],
             [2, 'Name', 'Bill Gates'],
             [2, 'Description', 'William Henry "Bill" Gates III is an American business magnate, philanthropist,\
                                investor, computer programmer, and inventor. Gates originally established his \
                                reputation as the co-founder of Microsoft'],
             [3, 'Siblings', ['Libby Gates', 'Kristi Gates']],
             [4, 'Leadership', ['Organization', ['Microsoft Corporation', '', ''], 'Role',
                                ['Chief Executive', '', 'CTO'], 'Title', ['Chief Executive', 'COO', 'CFO'],
                                'From-To', ['', '', '1975-04-04 - now']]]]

answer_list = [['Bill Gates', 'Business Person', ['Microsoft Corporation', 'Microsoft Research']],
               ['Di Ruan', 'Author', ['Amazon']],
               ['Jie-gang Kuang', 'Business Person', ['VMWare', 'Computer Engineering']]]

def padding_space(strlist, target_size):
    if target_size > len(strlist):
        for i in range(target_size - len(strlist)):
            strlist.append(' ')
    return strlist


def draw_title(title):
    if len(title) != 1:
        print 'The length of type 1 is incorrect'
        return
    l = W - len(V+WS)*2
    text = textwrap.wrap(title[0], l)
    for t in text:
        print V + WS + t.center(l) + WS + V
    print H


def draw_items(item):
    if len(item) != 2:
        print 'The length of type 2 or 3 is incorrect'
        return
    lt = W_LEFT - (len(V)+len(WS)*2)
    lb = W_BODY - len(V+WS)*2
    topic = textwrap.wrap(item[0], lt)
    if type(item[1]) is list:
        content = []
        for obj in item[1]:
            content = content + textwrap.wrap(obj, lb)
    else:   # Should be string (or unistring)
        content = textwrap.wrap(item[1], lb)
    h = max(len(topic), len(content))
    topic = padding_space(topic, h)
    content = padding_space(content, h)
    for i in range(h):
        print V + WS + topic[i].ljust(lt) + WS + V + WS + content[i].ljust(lb) + WS + V
    print H


def draw_table(item):
    if len(item) != 2:
        print 'The length of type 4 is incorrect'
        return
    if type(item[1]) is not list:
        print 'The items for a table should be a list'
        return
    lt = W_LEFT - (len(V)+len(WS)*2)
    topic = textwrap.wrap(item[0], lt)


def draw_infobox(info_list):
    print T
    for item in info_list:
        if item[0] == 1:
            draw_title(item[1:])
        elif item[0] == 2 or item[0] == 3:
            draw_items(item[1:])
        elif item[0] == 4:
            draw_table(item[1:])


def draw_answer(author_answer, question):
    print '-----'