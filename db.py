#########################################
#
#   Модуль для внесения работ в базу    #
#
#########################################


import redis



r = redis.Redis('localhost')

def getdata(hash):
    return r.get(hash)

def setdata():
    a = 0



