########IMPORT#############
import exctractor
import processor
import db
import sys
########VARIABLES##########
path = sys.argv[1]
text = exctractor.extract(path)
ftext, places = processor.format(text)
shingles = processor.shingler(ftext)
db.updateDB(ftext)
