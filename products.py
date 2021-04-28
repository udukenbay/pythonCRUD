from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


# the class ProductType will inherit the db.Model of SQLAlchemy
class ProductType(db.Model):
    __tablename__ = 'products'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    producttype_id = db.Column(db.Integer, nullable=False)
    producttype = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'producttype_id': self.producttype_id, 'producttype': self.producttype}
        # this method we are defining will convert our output to json

    def add_product(_name, _producttype_id, _producttype):
        '''function to add product to database using _name, _producttype_id, _producttype
        as parameters'''
        # creating an instance of our Product constructor
        new_product = ProductType(name=_name, producttype_id=_producttype_id, producttype=_producttype)
        db.session.add(new_product)  # add new product to database session
        db.session.commit()  # commit changes to session

    def get_all_products():
        '''function to get all products in our database'''
        return [ProductType.json(product) for product in ProductType.query.all()]

    def get_product(_id):
        '''function to get product using the id of the product as parameter'''
        return [ProductType.json(ProductType.query.filter_by(id=_id).first())]
        # ProductType.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_product(_id, _name, _producttype_id, _producttype):
        '''function to update the details of a product using the id, name,
        producttype_id and producttype as parameters'''
        product_to_update = ProductType.query.filter_by(id=_id).first()
        product_to_update.name = _name
        product_to_update.producttype_id = _producttype_id
        product_to_update.producttype = _producttype
        db.session.commit()

    def delete_product(_id):
        '''function to delete a product from our database using
           the id of the product as a parameter'''
        ProductType.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database