from random import choice

from app.database import *
from app.scale import *

def current_date():
    result = engine.execute('select current_date').first()
    newScale = choose_scale()

    if result == None or result == []:
        name = newScale.scale_name
        engine.execute('insert into days values(1,current_date,:1)',name)

        return select_piece(newScale)
    else:
        return select_piece(newScale)

def choose_scale():
    s = choice(PITCHES)
    m = choice(MODES)

    return scale(s,m)

def select_piece(k):
    key = engine.execute('select scale from days where day = current_date').first()
    result = engine.execute('select * from pieces where key like %s order by random() limit 1',key[0]).first()

    if result == None or result == []:
        return (newScale + ' is unfortunately not in the database. Check out some recommendations below, though.')
    else:
        s = ("%s (%i) by %s, Op.%i") % (result[1],result[5],result[3],result[6])
        return s
