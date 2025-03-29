from db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    productName = db.Column(db.String(80), nullable=False)
    productQuantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Produce Name is {self.productName}, we have {self.productQuantity} in Stock"
