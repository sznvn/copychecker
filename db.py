#########################################
#
#   Модуль для внесения работ в базу    #
#
#########################################


import redis
from itertools import permutations
from configuration import width
from processor import hashstore

r = redis.Redis('localhost')

def getdata(hash):
    return r.get(hash)

def setdata():
    a = 0

def updateDB(array):
    half = int(width / 2)
    for word in range(half, len(array) - half):
        shingle = []
        for i in range(-half, half + 1):
            shingle.append(array[word + i])

        permutated = list(permutations(shingle))
        for i in range(len(permutated)):
            unit = ''

            ###################
            for place in permutated[i]:
                unit += place
            print(unit, ' ', shingle, ' ', hashstore(unit))
            r.set(hashstore(unit), str(shingle))



