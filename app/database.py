from sqlalchemy import create_engine,MetaData

#engine = create_engine('postgresql://postgres:Seattle1989@localhost/postgres',convert_unicode=True)
engine = create_engine('postgres://riiovlwhtmovai:ILtFkt0CSXNe-7WLYCu5JkqFjl@ec2-54-225-199-108.compute-1.amazonaws.com:5432/dfu5ac3uhu5qle',convert_unicode=True)


metadata = MetaData(bind=engine)
