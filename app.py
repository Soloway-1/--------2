from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Конфігурація бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orderman.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель для таблиці з піцами
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

# Створення бази даних
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu_page():
    # Отримання всіх піц з бази даних
    menu = Pizza.query.all()
    return render_template('menu.html', menu=menu)

if __name__ == '__main__':
    app.run(port=1234, debug=True)