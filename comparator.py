import db

def comparator(hash, previous):
    value = db.getdata(hash)
    if value != None:
        value = value.decode()[1:-1].replace('\'','').replace(' ','').split(',')
        # print(previous, ' ', value.decode().split() == previous, ' ', value.decode()[1:-1].replace('\'','').replace(' ','').split(','))
        if value != previous:
            return value
