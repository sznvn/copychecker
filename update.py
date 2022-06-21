########IMPORT#############
import exctractor
import processor
import db
from configuration import path

########VARIABLES##########

text = exctractor.extract(path) + 100 * ' '
ftext, places = processor.format(text)
shingles = processor.shingler(ftext)
db.updateDB(ftext)
