from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Piece(Base):
    __tablename__ = 'Pieces'
    piece_id = Column(Integer, primary_key=True)
    piece_name = Column(String(50), unique=False)
    type = Column(String(15), unique=False)
    composer = Column(String(15), unique=False)
    key = Column(String(15), unique=False)
    year_completed = Column(Integer,unique=False)
    opus_number = Column(Integer,unique=False)


    def __init__(self,
            piece_id=None,
            piece_name=None,
            type=None,
            composer=None,
            key=None,
            year_completed=None,
            opus_number=None ):

        self.piece_id = piece_id
        self.piece_name = piece_name
        self.type = type
        self.composer = composer
        self.key = key
        self.year_completed = year_completed
        self.opus_number = opus_number


    def __repr__(self):
        return '<Piece %r>' % (self.piece_name)

class Day(Base):
    __tablename__ = 'Days'
    day_id = Column(Integer, primary_key=True)
    day = Column(DateTime,unique=False)
    scale = Column(String,unique=False)

    def __init__(self,day_id=None,day=None,scale=None):

        self.day_id = day_id
        self.day = day
        self.scale = scale

    def __repr__(self):
        return '<Day %r, Scale %r>' % (self.day,self.scale)
