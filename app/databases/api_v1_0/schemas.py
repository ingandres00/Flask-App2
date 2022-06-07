from marshmallow import fields

from app.ext import ma


class DatabasesSchema(ma.Schema):
    cedula = fields.Integer(dump_only=True)
    nombre = fields.String()
    apellido = fields.String()
    nacimiento = fields.Integer()
    edad = fields.Integer()
    nombrecompleto = fields.String()
    numeropedido = fields.Integer()
    tipopedido = fields.String()



