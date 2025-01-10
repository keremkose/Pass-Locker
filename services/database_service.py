from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_URL="sqlite:///./hotel_bookings.db"

engine=create_engine(SQL_URL,connect_args={"check_same_thread":False})
new_session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
base=declarative_base()
metadata=MetaData()
metadata.reflect(bind=engine)

def get_db():
    db=new_session()
    try:
        yield db
    except:
        db.close()