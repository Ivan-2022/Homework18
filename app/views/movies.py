from flask import request
from flask_restx import Resource, Namespace
from app.dao.schemas.movies import MovieSchema
from app.implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    movies_schema = MovieSchema(many=True)

    def get(self):
        movies = movie_service.get_all()
        return self.movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        new_movie = movie_service.create(req_json)
        return "", 201, {'location': f"{movie_ns.path}/{new_movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    movie_schema = MovieSchema()

    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return self.movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        self.movie_schema.dump(movie_service.update(mid, req_json))
        return "", 204

    def patch(self, mid: int):
        req_json = request.json
        self.movie_schema.dump(movie_service.update_partial(mid, req_json))
        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return "", 204
