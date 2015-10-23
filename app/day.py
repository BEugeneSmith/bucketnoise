from random import choice

from app.database import *
from app.scale import *
#from app.models import *

def current_day():

    result = engine.execute('select * from Days where day = date("now")')

    if result == None:
        newScale = choose_scale()
        name = newScale.scale_name
        engine.execute('insert into Days values(2,date("now"),:1)',name)

        return select_piece()
    else:
        return select_piece()

def choose_scale():
    s = choice(PITCHES)
    m = choice(MODES)

    return scale(s,m)

def select_piece():
    key = engine.execute('select key from Days where date == date("now")').first()
    result = engine.execute('select * from Pieces where key = :1 order by random() limit 1',key).first()

    if result == None:
        return 'not in database'
    else:
        return result
