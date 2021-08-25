from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='views')  # is a special variable in python that is just the name of the module

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
    return render_template('home.html',  posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


# @app.route("/about")
# def about():
#     return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)  # enable debug to debug frequent changes without restarting application


#### Theories used

# used template inheritance to to avoid repeated sections are getting written inside teplates