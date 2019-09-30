"""Database model"""
from api import db
from marshmallow import Schema, fields


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
    sale_price = db.Column(db.Float)
    sale_date = db.Column(db.Date)
    dollar_per_square_foot = db.Column(db.Float)

    def __repr__(self):
        return '<Transaction %r>' % self.id


class TransactionSchema(Schema):
    """Marshmallow schema"""
    id = fields.Integer()
    borough = fields.Str()
    neighborhood = fields.Str()
    building_class_category = fields.Str()
    address = fields.Str()
    apartment_number = fields.Str()
    zip_code = fields.Integer()
    residential_units = fields.Integer()
    commercial_units = fields.Integer()
    total_units = fields.Integer()
    land_square_feet = fields.Integer()
    gross_square_feet = fields.Integer()
    year_built = fields.Integer()
    building_class_at_time_of_sale = fields.Str()
    sale_price = fields.Float()
    sale_date = fields.Date()
    dollar_per_square_foot = fields.Float()

transaction_schema = TransactionSchema(many=True)

