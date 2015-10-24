from random import choice

from app.database import *
from app.scale import *

def current_day():
    result = engine.execute('select * from Days where day = date("now")').first()
    newScale = choose_scale()

    if result == None or result == []:
        name = newScale.scale_name
        engine.execute('insert into Days values(2,date("now"),:1)',name)

        return select_piece(newScale)
    else:
        return select_piece(newScale)

def choose_scale():
    s = choice(PITCHES)
    m = choice(MODES)

    return scale(s,m)

def select_piece(k):
    key = engine.execute('select scale from Days where day == date("now")').first()
    result = engine.execute('select * from Pieces where key like :1 order by random() limit 1',key[0]).first()

    s = ("%s (%i) by %s, Op.%i") % (result[1],result[5],result[3],result[6])

    if result == None:
        return (newScale + ' is unfortunately not in the database. Check out some recommendations below, though.')
    else:
        return s
