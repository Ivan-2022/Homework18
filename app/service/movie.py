from flask import request
from app.dao.movie import MovieDAO
from app.dao.model.movies import Movie
from app.service.pagination import pagination


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        movies = self.dao.get_movies()
        director_id = request.args.get('director_id', type=int)
        if director_id:
            movies = movies.filter(Movie.director_id == director_id)
        genre_id = request.args.get('genre_id', type=int)
        if genre_id:
            movies = movies.filter(Movie.genre_id == genre_id)
        year = request.args.get('year', type=int)
        if year:
            movies = movies.filter(Movie.year == year)
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        movies = pagination(movies, page, page_size).all()
        return movies

    def get_one(self, mid):
        movie = self.dao.get_movies().filter(Movie.id == mid).first()
        return movie

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, _data):
        movie = self.get_one(mid)
        movie.title = _data["title"]
        movie.description = _data["description"]
        movie.trailer = _data["trailer"]
        movie.year = _data["year"]
        movie.rating = _data["rating"]
        movie.genre_id = _data["genre_id"]
        movie.director_id = _data["director_id"]
        self.dao.update(movie)
        return movie

    def update_partial(self, mid, _data):
        movie = self.get_one(mid)
        if 'title' in _data:
            movie.title = _data['title']
        elif 'description' in _data:
            movie.description = _data['description']
        elif 'trailer' in _data:
            movie.trailer = _data['trailer']
        elif 'year' in _data:
            movie.year = _data['year']
        elif 'rating' in _data:
            movie.rating = _data['rating']
        elif 'genre_id' in _data:
            movie.genre_id = _data['genre_id']
        elif 'director_id' in _data:
            movie.director_id = _data['director_id']
        self.dao.update(movie)
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.dao.delete(movie)
