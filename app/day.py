from random import choice

from app.database_prod import *
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

    join_tbl = "SELECT pn.piece_name,pd.key,pd.composer,pd.year_completed,pd.opus_number,pd.number,pl.video_link,pl.imslp_link FROM piece_name pn JOIN piece_data pd ON pn.piece_id=pd.piece_id JOIN piece_links pl ON pn.piece_id=pl.piece_id"
    key = engine.execute('SELECT scale FROM days WHERE day = current_date').first()
    s = ''
    testKey = ("'"+key[0]+"'")

    query = ("SELECT * FROM (%s) s WHERE key = %s ORDER BY random() LIMIT 1 " % (join_tbl,testKey))
    result = engine.execute(query).first()

    if result == None or result == []:
        s = ("%s is unfortunately not in the database. Check out some recommendations below, though." % (k))
    else:
        if result[4] == 10000:
            s = ("%s (%i) by %s") % (result[0],result[3],result[2])
        else:
            s = ("%s (%i) by %s, Op.%i") % (result[0],result[3],result[2],result[4])

    video_key = ''

    if result[6] != '':
        video_key = (result[6])
    else:
        video_key = 'JNsKvZo6MDs'

    return [s,k,key[0],video_key]
