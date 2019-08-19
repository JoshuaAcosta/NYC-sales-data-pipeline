"""Database model"""
from api import db


class Transaction(db.Model):
    """table listing transactions"""
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    borough = db.Column(db.String, nullable=False)
    neighborhood = db.Column(db.String)
    building_class_category = db.Column(db.String)
    address = db.Column(db.String)
    apartment_number = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    residential_units = db.Column(db.Integer)
    commercial_units = db.Column(db.Integer)
    total_units = db.Column(db.Integer)
    land_square_feet = db.Column(db.Integer)
    gross_square_feet = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    building_class_at_time_of_sale = db.Column(db.String)
    sale_price = db.Column(db.Numeric)
    sale_date = db.Column(db.Date)

    def __repr__(self):
        return '<Transaction %r>' % self.id
