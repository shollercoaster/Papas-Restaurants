import os
import sys  #commands used to affect Python runtime environment
from sqlalchemy import Column, ForeignKey, Integer, String  #for mapper code
from sqlalchemy.orm import declarative_base  #for configuration code
from sqlalchemy.orm import relationship  #for foreign key relationships (useful in mapper code)
from sqlalchemy import create_engine  #used for configuration code at the end of a file

Base = declarative_base()  #initialises a Base object letting us know that our classes are SQLAlchemy classes

class Restaurant(Base):

    __tablename__ = 'restaurant'   #representation of our table in the database
    
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class MenuItem(Base):

    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



######insert at ebd of file######
engine = create_engine('sqlite:///restaurantmenu.db')  #instance of create_engine class that makes a new file used like a database 

Base.metadata.create_all(engine)  #creates database and adds necessary tables