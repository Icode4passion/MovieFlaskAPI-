from flask import Blueprint,jsonify,request
from . import db
from .models import Movies
main = Blueprint('main', __name__)
#main = Blueprint('main', __name__)

@main.route('/add_movies',methods=['POST'])
def add_movies():
	movie_data = request.get_json()
	new_movie = Movies(title=movie_data['title'], rating=movie_data['rating'])
	db.session.add(new_movie)
	db.session.commit()

	return 'Done' , 201

@main.route('/movies')
def movies():
	movie_list = Movies.query.all()
	movies = []
	for movie in movie_list:
		movies.append({'title':movie.title, 'rating':movie.rating})

	return jsonify({'movies':movies})
