""" Módulo con creación del engine y la sesión para acceso a la BD. """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# a) SQLite: ruta relativa y nombre de la BD
url = 'sqlite:///ejemplo_ORM.sqlite'
# b) MYSQL: formato "mysql+mysqlconnector://user:password@host:3306/DBname"
# url = "mysql+pymysql://app_user:app_password@localhost:3306/app_db"

engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()  # se usará en el modelo de la BD
