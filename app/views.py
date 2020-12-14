from flask import render_template,url_for, flash,redirect
from app import app
from .forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = '49740a2c2a37bf0e2b89f7'

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

@app.route('/register',methods = ['GET', 'POST'])
def register():

    '''
    View root page function that returns the about page and its data
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{fom.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():

    '''
    View root page function that returns the about page and its data
    '''
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)