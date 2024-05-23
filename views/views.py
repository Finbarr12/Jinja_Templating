from flask import Flask,Blueprint,render_template,abort
from model.model import PRODUCTS
products = Blueprint("products", __name__)

@products.route("/")
@products.route("/home")
def welcome():
    return 'Welcome to Our Store'


@products.route("/allproducts")
def allProducts():
    allproduces = PRODUCTS

    return render_template("index.html",productsComplete = allproduces)


@products.route ("/product/<key>")
def getProducts(key):
    product = PRODUCTS.get(key)

    if not product:
        abort(404)
    
    return render_template("product.html", singleProduct = product)
