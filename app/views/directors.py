from flask_restx import Resource, Namespace
from app.dao.schemas.directors import DirectorSchema
from app.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    directors_schema = DirectorSchema(many=True)

    def get(self):
        directors = director_service.get_all()
        return self.directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    director_schema = DirectorSchema()

    def get(self, did: int):
        director = director_service.get_one(did)
        return self.director_schema.dump(director), 200
