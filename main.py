########IMPORT#############
import exctractor
import processor
import comparator
import db
from configuration import path

########VARIABLES##########

text = exctractor.extract(path)

ftext, places = processor.format(text)

shingles = processor.shingler(ftext)
# print(text)
# print(ftext)
# print(places)
# print(len(places)==len(ftext))
# print(shingles)

before = []
i = 0
copy = []
#
for key, value in shingles.items():
    # print(i, ' ', key, ' ', value)
    less = int(i / 6)
    find = comparator.comparator(key, before)
    if find != None:
        a = 0
        print(find)
        copy.append(places[i])
        # print(text[places[less]:places[less+1]])
        # print(text[places[less]:places[less+10]])
    i += 1
    before = value


print(copy)
d = []
length = 0
last = 0
s = ''
for i in range(len(copy)):
    p = places.index(copy[i])
    print(p)
    #print(p - 1, '---', last)
    if p - 1 == last:
        s += text[places[p]:places[p + 1]]
        print(s)
    else:
        d.append(s)
        s = ''
    last = p

print(d)


# db.updateDB(ftext)
# print('--------------------', value)
# print(text[103:222])
#print(copy)
# print(ftext)

if __name__ == '__main__':
    print(int(7/6))

