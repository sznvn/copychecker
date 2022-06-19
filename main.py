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
        # print(find)
        copy.append(places[i])
        # print(text[places[less]:places[less+1]])
        # print(text[places[less]:places[less+10]])
    i += 1
    before = value


# print(copy)

d = []
length = 0
last = 0
s = ''
arr = []
for i in range(len(copy)):
    p = places.index(copy[i])
    arr.append(p)
# print(arr)

#     # print(p)
#     # print(p - 1, '---', last)
#     if p - 1 == last:
#         s += text[places[p]:places[p + 1]]
#         print(s)
#     else:
#         d.append(s)
#         s = ''
#     last = p
# d.append(s)
# print(d)

# print(text[446:476])
# db.updateDB(ftext)
# print('--------------------', value)
# print(text[103:222])
#print(copy)
# print(ftext)

# print('-----------')
before = 0
start, end = 0, 0
mark = []
for cp in arr:
    if before + 1== cp:
        # print(True)
        end = cp
    else:
        # print(False)
        mark.append([start, end])
        start = cp
    before = cp
mark.append([start,end])
# print(mark)

str = []
for d in mark:
    if d[0] == 0 and d[1] == 0:
        continue
    # print(d[0], 'd0' , d[1], 'd')
    str.append(text[places[d[0]]:places[d[1] + 3]])
print(str)






if __name__ == '__main__':
    a = 0
    # print(int(7/6))

# input('Press key')

