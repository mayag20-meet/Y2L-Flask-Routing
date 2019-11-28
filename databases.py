from model import Base, Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name):
	product_object = Product(
		name=name)
	session.add(product_object)
	session.commit()

def edit_product(id):
	product_object = session.query(
		Product).filter_by(
		name=name).first()
	# product_object. = 
	session.commit()


def delete_product(id):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()


def querry_all():
	products = session.query(
		Product).all()
	return products 

def query_product(id):
	product = session.query(
		Product).filter_by(
		name=name).first()
	return student

def Add_To_Cart(productID):
	productID_object = productID(
		productID = productID)
	session.add(productID_object)
	session.commit()
