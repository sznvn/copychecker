########IMPORT#############
import exctractor
import processor
import comparator
from configuration import path

########VARIABLES##########

text = exctractor.extract(path)

ftext, places = processor.format(text)

shingles = processor.shingler(ftext)

# print(ftext)
# print(places)
# print(len(places)==len(ftext))
# print(shigles)

before = []
i = 0

for key, value in shingles.items():
    i += 1
    less = int(i / 6)
    find = comparator.comparator(key, before)
    if find != None:

        print(text[places[less]:places[less+1]])
    before = value
    #print(key, '====>', shigles[key])


if __name__ == '__main__':
    print(int(7/6))

