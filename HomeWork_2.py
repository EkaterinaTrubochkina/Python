import random, string
# 1.create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# creation list of dicts and filling of random keys and values
my_list = []
for i in range(random.randint(2, 10)):
    sup_dict = {}
    for j in range(random.randint(1, 16)):
        sup_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
    my_list.append(sup_dict)
print(my_list)
#list = [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}] #tests
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# interaction in dict items in list
# looking to keys and values in all dicts
# if not in new list then add
# else  - check value and specify place
# then search for values in new and final dicts
final_dict, support_dict = {}, {}

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
                support_dict.update({key: my_list.index(dictionary)+1})
print(final_dict)  #tests
print(support_dict)  #tests
for key in final_dict:
    if key in support_dict:
        final_dict[key + '_' + str(support_dict[key])] = final_dict.pop(key)
print(final_dict)

