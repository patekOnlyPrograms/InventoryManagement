from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, String, Integer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///InventoryDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Product

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    test_db()
    return render_template('index.html', inventory=inventory)


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




def test_db():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return print("IT WORKS")
    except Exception as ex:
        errorText = str(ex)
        return errorText

app.run(debug=True)