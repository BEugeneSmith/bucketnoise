from random import choice

from app.database import *
from app.scale import *

def current_date():
    result = engine.execute('SELECT current_date').first()
    newScale = choose_scale()

    if result == None or result == []:
        name = newScale.scale_name
        engine.execute('INSERT INTO days VALUES(((SELECT COUNT(*) FROM days)+1),current_date,%s)',name)



        return select_piece(name)
    else:
        return select_piece(newScale.scale_name)

def choose_scale():
    s = choice(PITCHES)
    m = choice(MODES)

    return scale(s,m)

def select_piece(k):
    key = engine.execute('SELECT  scale FROM days WHERE day = current_date').first()
    result = engine.execute('SELECT * FROM pieces WHERE key LIKE %s ORDER BY random() LIMIT 1',key[0]).first()
    s = ''

    if result == None or result == []:
        s = ('%s is unfortunately not in the database. Check out some recommendations below, though.' % (k))
    else:
        s = ("%s (%i) by %s, Op.%i") % (result[1],result[5],result[3],result[6])

    return [s,k]
