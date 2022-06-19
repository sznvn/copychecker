import db

def comparator(hash, previous):
    value = db.getdata(hash)
    # print(hash, '1', value)
    if value != None:
        value = value.decode()[1:-1].replace('\'','').replace(' ','').split(',')
        # print(set(value), '   ', set(value) == set(previous), '    ', set(previous))
        # print(hash, '2', value)
        if set(value) != set(previous):

            # print(value)
            return value
