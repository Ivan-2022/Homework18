from app.dao.model.movies import Movie
from app.dao.model.directors import Director
from app.dao.model.genres import Genre


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_movies(self, mid=None, **kwargs):
        query = self.session.query(Movie)
        if mid:
            return query.get(mid)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f"Movie.{key}") == int(value))
        return query

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
