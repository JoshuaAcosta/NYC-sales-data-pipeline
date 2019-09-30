"""API Resources """
from flask_restful import Resource
from flask import request
from models import Transaction, transaction_schema


class ZipcodeResources(Resource):
    def get(self, zipcode):
        """returns transactions by zipcode"""
        result = Transaction.query.filter_by(zip_code=zipcode).all()
        output = transaction_schema.dump(result)
        return {"transactions" : output}

class NeighborhoodResources(Resource):
    def get(self, neighborhood):
        """returns transactions by neighborhood"""
        result = Transaction.query.filter_by(neighborhood=neighborhood).all()
        output = transaction_schema.dump(result)
        return {"transactions" : output}

class DateResources(Resource):
    def get(self):
        """returns transactions by date range provided"""
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        result = Transaction.query.filter(Transaction.sale_date >= from_date, Transaction.sale_date <= to_date ).all()
        output = transaction_schema.dump(result)
        return {"transactions" : output}
