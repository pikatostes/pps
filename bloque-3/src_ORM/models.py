"""" Módulo que crea modelo User para BD."""

from sqlalchemy import Column, Integer, String

# Importamos módulo "propio" con creación del engine y la sesión
import db


class User(db.Base):
    __tablename__ = 'users'

    # Añadido tamaño en strings para mysql..
    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False)
    username = Column(String(32), nullable=False)
    password = Column(String(32), nullable=False)
    edad = Column(Integer, nullable=False)

    def __init__(self, email, username, password, edad):
        self.email = email
        self.username = username
        self.password = password
        self.edad = edad

    def __str__(self):
        return f"User: {self.username} {self.email} | {self.edad} "

    # se utiliza al imprimir una lista de usuarios directamente con print
    def __repr__(self):
        return f'\n User: {self.username}, {self.email} | {self.edad} )'

    # Sobre __str_- y __repr__
    #  https://www.analyticslane.com/2020/07/03/diferencias-entre-str-y-repr-en-python/
