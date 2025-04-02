from sqlalchemy import text
from flask import Flask, render_template, request
from db import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
databaseName = 'InventoryDatabase'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{databaseName}.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#inventory = []

@app.route('/')
def index():
    test_db()
    return render_template('index.html', inventory = inventory)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/product_list')
def product_list():
    return render_template("product_list.html")

@app.route('/add_remove_product', methods=['GET','POST'])
def add_remove_product():
    product_name = request.form.get("Product")
    quantity = request.form.get("Quantity")
    print(product_name, quantity)
    return render_template("add_remove_product.html")

def create_tables():
    with app.app_context():
        db.create_all()

def test_db():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return print("IT WORKS")
    except Exception as ex:
        errorText = str(ex)
        return errorText

#app.app_context().push()

create_tables()

if __name__ == '__main__':
    app.run(debug=True)