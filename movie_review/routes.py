from flask import render_template, flash, redirect, url_for, request
from movie_review.forms import RegistrationForm, LoginForm
from movie_review import app, db, bcrypt
from movie_review.models import User, Review, Movie
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['get', 'post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # user exists and password is correct, then login
            login_user(user, remember=form.remember.data)
            flash("Login successful! ", "success")
            # next_page = request.args.get("next")
            # if next_page is None:
            #     return redirect(url_for("home"))
            # else:
            #     return redirect(next_page)
            return redirect(url_for("account"))
        else:
            flash("Login Unsuccessful. Please try again.", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/review")
def review():
    movies = Movie.query.all()
    reviews = Review.query.all()
    return render_template("review.html", title="Review", movies=movies, reviews=reviews)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("home")


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")
