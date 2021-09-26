import random
import re
import string

# New HomeWork_2
# variables
my_list = []
final_dict, support_dict = {}, {}


# first def for creation list
def creation_list():

    for i in range(random.randint(2, 10)):
        sup_dict = {}
        for j in range(random.randint(1, 16)):
            sup_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        my_list.append(sup_dict)
    print(my_list)
    return my_list


# second def for creating a combined list
def new_list_from_lists(my_list):
    for dictionary in my_list:
        for key, value in dictionary.items():
            if key not in final_dict:
                final_dict.update({key: value})
            else:
                if value < final_dict.get(key):
                    support_dict.update({key: my_list.count(dictionary)})
                    continue
                else:
                    final_dict.update({key: value})
                    support_dict.update({key: my_list.index(dictionary) + 1})
    for key in final_dict:
        if key in support_dict:
            final_dict[key + '_' + str(support_dict[key])] = final_dict.pop(key)
    return final_dict


# call of functions and getting results for HomeWork_3
print('HomeWork_2:')
result = new_list_from_lists(creation_list())
print(result)


# New HomeWork_3
# variables
init_text = '''  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix"iZ" with correct "is", but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

m, new = [], []
new_line = []


# function for creating list with normalized sentences
def list_of_sentences(init_text):
    k = init_text.split('.')
    k = [x for x in k if x]
    # print(k)
    for i in k:
        if not i.isalpha():
            d = i.lstrip()
            m.append(d.capitalize())
        else:
            m.append(d.capitalize())
    # print(m)
    return m


# function to correction iz to is in LIST
def correction_iz(m):
    for l in m:
        if not l.endswith("."):
            # l += "."
            new.append(l.replace('iz ', 'is '))
    return new


# creation of new line from last words in all sentence and normalize it
def new_line_creating(new):
    text = []
    text_2 = ''

    for t in new:
        res = re.findall(r'^.*\b(\w+).*$', t)
        new_line.append(res)
    for p in new_line:
        text += p
    for q in text:
        text_2 += q + ' '
    new.append(text_2.capitalize())
    return new


# function to creation text and print it from list of sentences
def text_from_list(new):
    final_sent = ''
    # old version : for w in new:
    final_sent = '.\n'.join(new)
    # old version : final_sent += w + '\n'
    print(final_sent)
    return final_sent


# now try to count all whitespaces in initial text
def count_whitespaces(text):
    for u in text:
        k = text.count(" ") + text.count("\n")
    print("Number of whitespaces = {0}".format(k))
    return k


#call of functions and getting results for HomeWork_3
print('\n' + 'HomeWork_3:')
list_of_sentences(init_text)
correction_iz(m)
new_line_creating(new)
text_from_list(new)
count_whitespaces(init_text)