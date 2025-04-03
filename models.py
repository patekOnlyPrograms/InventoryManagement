from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from __main__ import db


class Products(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    productName: Mapped[String] = mapped_column(String(80), nullable= False)
    productQuantity: Mapped[int] = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Produce Name is {self.productName}, we have {self.productQuantity} in Stock"

