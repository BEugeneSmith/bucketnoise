from sqlalchemy import create_engine,MetaData

engine = create_engine('postgresql://postgres:Seattle1989@localhost/postgres',convert_unicode=True)


metadata = MetaData(bind=engine)
