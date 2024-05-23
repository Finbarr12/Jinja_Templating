from flask import Flask,request
import ccy
from views.views import products

app = Flask(__name__)

app.register_blueprint(products)

@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or 'USD'
    return '{0} {1}'.format(currency_code, amount)