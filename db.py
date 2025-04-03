from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from application import db


class Products(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    productName: Mapped[String] = mapped_column(String(80), nullable= False)
    productQuantity:  db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Produce Name is {self.productName}, we have {self.productQuantity} in Stock"

    with db.app_context():
        db.create_all()