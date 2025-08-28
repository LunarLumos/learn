from flask import Flask, render_template, request, redirect
from models import ProductDB

app = Flask(__name__)
db = ProductDB()

@app.route("/")
def index():
    products = db.get_all()
    return render_template("index.html", products=products)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    if name.strip():  # Basic validation to prevent empty names
        db.add_product(name)
    return redirect("/")

@app.route("/remove/<int:product_id>")
def remove(product_id):
    db.remove_product(product_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
