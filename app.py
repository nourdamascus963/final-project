from flask import Flask, jsonify, request

app = Flask(__name__)

products = []
# Technical Debt:
# - No input validation on product data
# - No persistent storage (in-memory list only)
# - No error handling for invalid indexes
# These will be improved in future iterations.
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products", methods=["POST"])
def add_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201

@app.route("/products/<int:index>", methods=["PUT"])
def update_product(index):
    products[index] = request.json
    return jsonify(products[index])

@app.route("/products/<int:index>", methods=["DELETE"])
def delete_product(index):
    products.pop(index)
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
