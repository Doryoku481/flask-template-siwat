from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #title = "Welcome Page"
    return render_template('index.html', title="Welcome Page")

@app.route('/about')
def about():
    title = 'About page'
    name = 'siwat'
    email = 'std.67122420314'
    mobile = '0643013036'
    age = 20
    return render_template('about.html', title=title, name=name, email=email, mobile=mobile, age=age)   

@app.route('/favarite/foods')
def favarite_foods():
    title = 'Favarite Foods page'
    foods = ['ชาบู', 'หมูกระทะ', 'ซูชิ']
    return render_template('favorite_foods.html', title=title, foods=foods)

@app.route('/favarite/sports')
def favarite_sports(): 
    title = 'Favarite Sports page'
    sports = ['ฟุตบอล', 'บาสเกตบอล', 'ว่ายน้ำ']
    return render_template('favorite_sports.html', title=title, sports=sports)

@app.route('/favarite/movies')
def favarite_movies(): 
    title = 'Favarite Movies page'
    movies = ['Avengers Endgame','Ready Player One','Godzilla','Kong','Fast & Furious 9']
    return render_template('favorite_movies.html', title=title, movies=movies)