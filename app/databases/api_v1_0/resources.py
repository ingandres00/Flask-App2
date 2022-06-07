from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import DatabasesSchema
from ..models import Databases

datas_v1_0_bp = Blueprint('datas_v1_0_bp', __name__)

datas_schema = DatabasesSchema()

api = Api(datas_v1_0_bp)

class DatasListResource(Resource):
    def get(self):
        datas = Data.get_all()
        result = datas_schema.dump(datas, many=True)
        return result

    def post(self):
        data = request.get_json()
        datas_dict = film_schema.load(data)
        databases = Databases(nombre=datas_dict['nombre'],
                    apellido=datas_dict['apellido'],
                    nacimiento=datas_dict['nacimiento'],
                    edad=datas_dict['edad'],
                    nombrecompleto=datas_dict['nombrecompleto'],
                    numeropedido=datas_dict['numeropedido'],
                    tipopedido= datas_dict['tipopedido']
        )
        databases.save()
        resp = datas_schema.dump(datas)
        return resp, 201

class DatasResource(Resource):
    def get(self, cedula_id):
        databases = Databases.get_by_id(cedula_id)
        if databases is None:
            raise ObjectNotFound('No existe')
        resp = datas_schema.dump(datas)
        return resp
    

api.add_resource(DatasListResource, '/api/v1.0/databases/', endpoint='datas_list_resource')
api.add_resource(DatasResource, '/api/v1.0/databases/<int:cedula_id>', endpoint='datas_resource')
