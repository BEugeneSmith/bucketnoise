from sqlalchemy import create_engine,MetaData,Table
engine = create_engine('sqlite:////home/es/Desktop/scales/test.db', convert_unicode=True)
metadata = MetaData(bind=engine)
