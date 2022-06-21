########IMPORT#############
import exctractor
import processor
import comparator
import sys
########VARIABLES##########
path = sys.argv[1]
text = exctractor.extract(path) + 100 * ' '
ftext, places = processor.format(text)
shingles = processor.shingler(ftext)

###################################
# print(text)
# print(ftext)
# print(places)
# print(len(places)==len(ftext))
# print(shingles)
#################################

def checker(shingles):
	before = []
	i = 0
	copy = []

	for key, value in shingles.items():
	    find = comparator.comparator(key, before)
	    if find != None:
	        copy.append(places[i])
	    i += 1
	    before = value
	arr = []

	for i in range(len(copy)):
	    p = places.index(copy[i])
	    arr.append(p)

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

	str = []
	for d in mark:
	    if d[0] == 0 and d[1] == 0:
	        continue
	    # print(d[0], 'd0' , d[1], 'd')
	    try:
	        str.append(text[places[d[0]]:places[d[1]+2]])
	    except IndexError:
      	        str.append(text[places[d[0]]:places[len(places)-1]])
	return str

output = checker(shingles)
lindex = 0
ntext = ''
for s in output:
    i = text.find(s)
    ntext += text[lindex:i] + '<p data-tooltip="Источник: (справа добавить %)" style="background-color:#FF7C7C">' + text[i:i + len(s)] + '</p>' 
    lindex = i + len(s)

print(ntext)
