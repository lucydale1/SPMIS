from login.models import variable_holder
from django.core.cache import cache
from random import randint


def nextkey():
    f = open("login/static/springer_api_keys.txt")
    lines = f.readlines()

    current_key_index = cache.get('counter')
    next_index = (current_key_index + 1) % (len(lines) - 1)
    cache.set('counter', next_index)

    next_key = lines[next_index]
    print("Key used: " + next_key)

    return next_key

def getstart():
    f = open("login/static/springer_api_keys.txt")
    lines = f.readlines()
    start_key = randint(0,len(lines)-1)
    return start_key
