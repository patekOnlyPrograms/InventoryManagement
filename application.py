from sqlalchemy import text
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///InventoryDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
from models import Products



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
    if request.method == 'POST':
        productName = request.form.get("Product")
        productQuantity = int(request.form.get("Quantity"))
        print(productName, productQuantity)
        newProduct = Products(productName = productName, productQuantity = productQuantity)
        db.session.add(newProduct)
        db.session.commit()
        return render_template("add_remove_product.html")
    return render_template("add_remove_product.html")


def test_db():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return print("IT WORKS")
    except Exception as ex:
        errorText = str(ex)
        return errorText


if __name__ == '__main__':
    app.run(debug=True)