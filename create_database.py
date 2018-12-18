from movie_review.models import db, User, Movie, Review
db.create_all()
user_1 = User(username='user1', email='user1@movie.com', password='this_is_user1')
db.session.add(user_1)
user_2 = User(username='user2', email='user2@movie.com', password='this_is_user2')
db.session.add(user_2)
movie_1 = Movie(name='movie1', date_released=1998, type='comedy', cast='John Doe')
db.session.add(movie_1)
review_1 = Review(title='New Review 1', rate=5, content='this is a test review',
                  user_id=1, movie_id=1)
db.session.add(review_1)
review_2 = Review(title='New Review 2', rate=1, content='this is another test review',
                  user_id=2, movie_id=1)
db.session.add(review_2)
db.session.commit()

# some tests for the database
# User.query.all()
# Review.query.all()
# Movie.query.all()
# user1 = User.query.get(1)
# user1.posts
# user2 = User.query.get(2)
# user2.posts
# movie = Movie.query.get(1)
# movie.reviews
# db.drop_all()
