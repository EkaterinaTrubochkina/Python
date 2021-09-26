import re

init_text = '''  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix"iZ" with correct "is", but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

m, new = [], []
new_line = []
# Not universal approach :
# b = init_text.replace('\n\n\n\n','')
# print(b)
#
# c = b.replace('  ','')
# print(c)
# d = c.replace('. ','')
# print(d)
# k = d.split('.')
# print(k)
# for i in k:
#     m.append(i.capitalize())
# print(m)

# More universal approach:
# divide the text into sentences
# and remove the non-letter from the beginning of the sentence
# and write all the first letters with a capital letter
k = init_text.split('.')
# print(k)
for i in k:
    if i.startswith('  ') or i.endswith('  '):
        d = i.lstrip()
        m.append(d.capitalize())
    elif i.startswith('\n\n\n\n') or i.startswith('\n\n\n\n  '):
        d = i.lstrip()
        m.append(d.capitalize())
    elif i.startswith(' '):
        d = i.lstrip()
        m.append(d.capitalize())

# put dot and fix "iz"
for l in m:
    if not l.endswith("."):
        l += "."
        new.append(l.replace('iz ', 'is '))

# creation of new line from last words in all sentence
for t in new:
    res = re.findall(r'^.*\b(\w+).*$', t)
    new_line.append(res)

text = []
text_2 = ''
final_sent = ''
for p in new_line:
    text += p
for q in text:
    text_2 += q + ' '
new.append(text_2.capitalize())

# final string
for w in new:
    final_sent += w + '\n'
print(final_sent)

# now try to count all whitespaces in initial text
for u in init_text:
    k = init_text.count(" ") + init_text.count("\n")

print("Number of waterspaces = {0}".format(k))