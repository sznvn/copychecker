########IMPORT#############
import exctractor
import processor
import comparator
from configuration import path

########VARIABLES##########

text = exctractor.extract(path)

ftext, places = processor.format(text)

shigles = processor.shingler(ftext)

# print(ftext)
# print(places)
# print(len(places)==len(ftext))
# print(shigles)

before = []
i = -100
for key, value in shigles.items():
    find = comparator.comparator(key, before)
    if find != None:
        print(i)
        print(i, ' ', places[i])
        # print(text[places[i]:1])
    before = value
    #print(key, '====>', shigles[key])


if __name__ == '__main__':
    print('PyCharm')

