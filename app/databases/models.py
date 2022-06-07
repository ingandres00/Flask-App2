from app.db import db, BaseModelMixin


class Databases(db.Model, BaseModelMixin):
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    nacimiento = db.Column(db.Integer)
    edad = db.Column(db.Integer)
    nombrecompleto = db.Column(db.String)
    numeropedido = db.Column(db.Integer)
    tipopedido = db.Column(db.String)
   
    def __init__(self, nombre, apellido, nacimiento, edad, nombrecompleto, numeropedido, tipopedido):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.edad = edad
        self.nombrecompleto = nombrecompleto
        self.numeropedido = numeropedido
        self.tipopedido = tipopedido

    def __repr__(self):
        return f'databases({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'




