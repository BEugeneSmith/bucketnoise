from random import choice

from app.database import *
from app.scale import *

def current_date():
    ''' returns scale for the current date '''
    today = engine.execute('SELECT current_date').first()
    newScale = choose_scale()

    result = engine.execute('SELECT * FROM days where day = %s',today[0]).first()

    if result == None or result == []:
        name = newScale.scale_name
        engine.execute('INSERT INTO days VALUES(((SELECT COUNT(*) FROM days)+1),%s,%s)',today[0],name)

        return select_piece(name)
    else:
        return select_piece(newScale.scale_name)

def choose_scale():
    ''' returns random scale out of 24 '''
    s = choice(PITCHES)
    m = choice(MODES)

    return scale(s,m)

def select_piece(k):
    ''' returns piece '''
    key = engine.execute('SELECT scale FROM days WHERE day = current_date').first()
    s = ''
    testKey = ("'"+key[0]+"'")

    query = ("SELECT * FROM pieces WHERE key = %s ORDER BY random() LIMIT 1" % (testKey))
    result = engine.execute(query).first()

    if result == None or result == []:
        s = ("%s is unfortunately not in the database. Check out some recommendations below, though." % (k))
        result = ['https://www.youtube.com/watch?v=AeJX7fxz-f4']
    else:
        s = ("%s (%i) by %s, Op.%i") % (result[1],result[5],result[3],result[6])

    video_key = ''

    try:
        video_key = ("'"+result[8]+"'")
    except:
        video_key = 'na'

    return [s,k,key[0],video_key]
