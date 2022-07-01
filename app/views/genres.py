from flask_restx import Resource, Namespace
from app.dao.schemas.genres import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    genres_schema = GenreSchema(many=True)

    def get(self):
        genres = genre_service.get_all()
        return self.genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    genre_schema = GenreSchema()

    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return self.genre_schema.dump(genre), 200
