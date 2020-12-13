from flask import render_template
from app import app

posts = [
    {
        'author': 'Ariso Okanga',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'December 13,2020'

    },
    {
        'author': 'Barbara Charlotte',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'December 13,2020'

    }
]
# Views
@app.route('/')
@app.route('/home')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():

    '''
    View root page function that returns the about page and its data
    '''
    return render_template('about.html', title='About')
