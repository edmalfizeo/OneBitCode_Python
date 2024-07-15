import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

database = os.environ.get('DB_NAME2')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')

encoded_password = quote_plus(password.encode('utf-8'))

DATABASE_URL = f"postgresql://{user}:{encoded_password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine)
session = sessionLocal()

base = declarative_base()
