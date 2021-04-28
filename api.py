from products import *

# GET
# route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    '''Function to get all the products in the database'''
    return jsonify({'ProductType': ProductType.get_all_products()})

# route to get product by id
@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    return_value = ProductType.get_product(id)
    return jsonify(return_value)

# POST
# route to add new product
@app.route('/products', methods=['POST'])
def add_product():
    '''Function to add new product to our database'''
    request_data = request.get_json()  # getting data from client
    ProductType.add_product(request_data["name"], request_data["producttype_id"],
                    request_data["producttype"])
    response = Response("Product added", 201, mimetype='application/json')
    return response

# PUT
# route to update product with PUT method
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    '''Function to edit product in our database using product id'''
    request_data = request.get_json()
    ProductType.update_product(id, request_data['name'], request_data['producttype_id'],                                      request_data['genre'])
    response = Response("Product Updated", status=200, mimetype='application/json')
    return response

# DEL
# route to delete product using the DELETE method
@app.route('/products/<int:id>', methods=['DELETE'])
def remove_product(id):
    '''Function to delete product from our database'''
    ProductType.delete_product(id)
    response = Response("Product Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)

