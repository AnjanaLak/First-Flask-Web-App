from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Anjana Lakshan',
        'title': 'Jurassic Part 5',
        'content': 'First content',
        'date_posted': 'May 20, 2020'
    },

    {
        'author': 'Sasi Evanjana',
        'title': 'Jurassic Part 6',
        'content': 'Second content',
        'date_posted': 'June 20, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',
              'success')  # use f for the flash message because we are using a
        # python version above 3.6
        # In here 'success' is the method
        return redirect(url_for('home'))  # always remember that home is the function not the url path name
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsusseful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


# @app.route("/about")
# def about():
#     return "<h1>About Page</h1>"

