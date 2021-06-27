import urllib.parse

from sqlalchemy import create_engine, insert
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer, Numeric, CheckConstraint, ForeignKey
from datetime import datetime

engine = create_engine("mysql+pymysql://root:%s@localhost/testdb" % urllib.parse.quote_plus('root@123'))

dbConnection = engine.connect()

metadata = MetaData()

# customers table stores all the information about the customer. It consists of following columns:

# id - primary key
# first_name - first name of customer
# last_name - last name of customer
# username - a unique username
# email - a unique email
# address - customer address
# town - customer town name
# created_on - date and time of account creation
# updated_on - date and time the account was last updated

customers = Table('customers', metadata,
            Column('id', Integer(), primary_key=True),
            Column('first_name', String(100), nullable=False),
            Column('last_name', String(100), nullable=False),
            Column('username', String(50), unique=True, nullable=False),
            Column('email', String(200), nullable=False),
            Column('address', String(200), nullable=False),
            Column('town', String(50), nullable=False),
            Column('created_on', DateTime(), default=datetime.now),
            Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)
# items table stores information about products. It consists of following columns:

# id - primary key
# name - item name
# cost_price - cost price of item
# selling_price - selling price of item
# quantity - quantity of item in the stock

items = Table('items', metadata,
            Column('id', Integer(), primary_key=True),
            Column('name', String(200), nullable=False),
            Column('selling_price', Numeric(10, 2), nullable=False),
            Column('quantity', Integer(), nullable=False),
            CheckConstraint('quantity > 0', name='quantity_check')
            )

# orders stores information about the orders made by the customers. It consists of following columns:

# id - primary key
# customer_id - foreign key to id column in the customers table
# date_placed - date and time the order was placed
# date_shipped - date and time the order was shipped

orders = Table('orders', metadata,
            Column('id', Integer(), primary_key=True),
            Column('customer_id', ForeignKey('customers.id')),
            Column('date_placed', DateTime(), default=datetime.now),
            Column('date_shipped', DateTime())
            )
# order_lines stores details of items in the each order. It consists of following columns:

# id - primary key
# order_id - foreign key to id column in the orders table
# item_id - foreign key to id column in the items table
# quantity - quantity of item ordered

order_lines = Table('order_lines', metadata,
                Column('id', Integer(), primary_key=True),
                Column('order_id', ForeignKey('orders.id')),
                Column('item_id', ForeignKey('items.id')),
                Column('quantity', Integer())
                )

metadata.create_all(engine)

ins = customers.insert().values(
    first_name = 'John',
    last_name = 'Green',
    username = 'johngreen',
    email = 'johngreen@gmail.com',
    address = '164 Hidden Valley Road',
    town = 'Norfolk'
)

r = dbConnection.execute(ins)

print(r.inserted_primary_key)

ins = insert(customers).values(
    first_name = 'Katherine',
    last_name = 'Wilson',
    username = 'katwilson',
    email = 'katwilson@gmail.com',
    address = '4685 West Side Avenue',
    town = 'Peterbrugh'
)

r = dbConnection.execute(ins)
print(r.inserted_primary_key)

