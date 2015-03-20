import textwrap

W = 100
N = '+'
L = '-'
V = '|'
WS = ' '
W_LEFT = 20
W_BODY = 80
W_NAME = 30
W_TYPE = 20
W_LIST = 50

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


def col_to_row(column):
    c = len(column)
    r = len(column[0])
    row = []
    for i in range(r):
        tmp = []
        for j in range(c):
            tmp.append(column[j][i])
        row.append(tmp)
    return row


def organize_row(row, bound):
    wrap = []
    for r in row:
        wrap.append(textwrap.wrap(r, bound))
    h = max(map(len, wrap))
    for r in wrap:
        padding_space(r, h)
    return col_to_row(wrap)


def draw_title(title):
    if len(title) != 1:
        print 'The length of type 1 is incorrect'
        return
    l = W - len(V+WS)*2
    text = textwrap.wrap(title[0], l)
    for t in text:
        print V + WS + t.center(l) + WS + V
    print N + L*(W_LEFT-len(N)*2) + N + L*(W_BODY-len(N)) + N


def draw_items(item):
    if len(item) != 2:
        print 'The length of type 2 or 3 is incorrect'
        return
    lt = W_LEFT - len(V+WS)*2
    lb = W_BODY - (len(WS)*2+len(V))
    topic = textwrap.wrap(item[0], lt)
    if type(item[1]) is list:
        content = []
        for obj in item[1]:
            content = content + textwrap.wrap(obj, lb)
    else:   # Should be string (or unistring)
        content = textwrap.wrap(item[1], lb)
    h = max(len(topic), len(content))
    padding_space(topic, h)
    padding_space(content, h)
    for i in range(h):
        print V + WS + topic[i].ljust(lt) + WS + V + WS + content[i].ljust(lb) + WS + V
    print N + L*(W_LEFT-len(N)*2) + N + L*(W_BODY-len(N)) + N


def draw_table(item):
    if len(item) != 2:
        print 'The length of type 4 is incorrect'
        return
    if type(item[1]) is not list:
        print 'The items for a table should be a list'
        return
    lt = W_LEFT - len(V+WS)*2
    topic = textwrap.wrap(item[0], lt)
    column = item[1][0]
    col_num = len(column)
    content = col_to_row(item[1][1:])
    lb = W_BODY/col_num - (len(WS)*2+len(V))
    lb_1st = W_BODY - (W_BODY/col_num)*(col_num-1) - (len(WS)*2+len(V))
    col = organize_row(column, lb)
    table = []
    for c in content:
        table = table + organize_row(c, lb)
    h = len(col) + 1 + len(table)   # '1' for the separate line
    padding_space(topic, h)
    for i in range(h):
        if i < len(col):
            s = WS + col[i][0].ljust(lb_1st) + WS + V
            for c in col[i][1:]:
                s = s + WS + c.ljust(lb) + WS + V
            print V + WS + topic[i].ljust(lt) + WS + V + s
        elif i > len(col):
            s = WS + table[i-len(col)-1][0].ljust(lb_1st) + WS + V
            for c in table[i-len(col)-1][1:]:
                s = s + WS + c.ljust(lb) + WS + V
            print V + WS + topic[i].ljust(lt) + WS + V + s
        else:
            s = L*(lb_1st+2) + N
            for i in range(1, col_num):
                s = s + L*(lb+2) + N
            print V + WS*(W_LEFT-len(N)*2) + N + s
    print N + L*(W_LEFT-len(N)*2) + N + L*(W_BODY-len(N)) + N


def draw_infobox(info_list):
    print N + L*(W-len(N)*2) + N
    for item in info_list:
        if item[0] == 1:
            draw_title(item[1:])
        elif item[0] == 2 or item[0] == 3:
            draw_items(item[1:])
        elif item[0] == 4:
            draw_table(item[1:])


def draw_answer_table(item):
    if len(item) != 3:
        print 'The length of answer is incorrect'
        return
    if type(item[2]) is not list:
        print 'The items for a table should be a list'
        return
    ln = W_NAME - len(V+WS)*2
    lt = W_TYPE - (len(WS)*2+len(V))
    ll = W_LIST - (len(WS)*2+len(V))
    name = textwrap.wrap(item[0], ln)
    atype = textwrap.wrap(item[1], lt)
    plist = item[2]
    row = col_to_row([plist])
    plist = []
    for r in row:
        plist = plist + organize_row(r, ll)
    padding_space(atype, len(plist))
    h = 2 + len(plist)
    padding_space(name, h)
    print V + WS + name[0].ljust(ln) + WS + V + WS + 'As'.ljust(lt) + WS + V + WS + 'Creation'.ljust(ll) + WS + V
    print V + WS + name[1].ljust(ln) + WS + N + L*(W_TYPE-len(N)) + N + L*(W_LIST-len(N)) + N
    for i in range(2, h):
        j = i - 2
        print V + WS + name[i].ljust(ln) + WS + V + WS + atype[j].ljust(lt) + WS + V + WS + plist[j][0].ljust(ll) + WS + V
    print N + L*(W_NAME-len(N)*2) + N + L*(W_TYPE-len(N)) + N + L*(W_LIST-len(N)) + N


def draw_answer(answer_list, question):
    print N + L*(W-len(N)*2) + N
    l = W - len(V+WS)*2
    text = textwrap.wrap(question, l)
    for t in text:
        print V + WS + t.center(l) + WS + V
    print N + L*(W_NAME-len(N)*2) + N + L*(W_TYPE-len(N)) + N + L*(W_LIST-len(N)) + N
    for item in answer_list:
        draw_answer_table(item)
