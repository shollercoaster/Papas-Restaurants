from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

myFirstRestaurant.name = "Papa's Pizzeria"
session.add(myFirstRestaurant)
session.commit()
print(myFirstRestaurant.name)

session.query(Restaurant).all()
cheesepizza = MenuItem(name = 'Cheese Pizza', description = "Made with all natural ingredients and free mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
cheesepizza.name = "Cheese Pizza"
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
firstResult = session.query(Restaurant).first()
print(firstResult.name)
print(session.query(Restaurant).all())
items = session.query(MenuItem).all()
# for item in items:
#     print(item.name)
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
veggieBurgerDetails = []
for veggieBurger in veggieBurgers:
    veggieBurgerDetails.append([veggieBurger.id, veggieBurger.price, veggieBurger.restaurant.name])

print(veggieBurgerDetails)
PapaVeggieBurger = session.query(MenuItem).filter_by(id = 12).one()
PapaVeggieBurger.price = 2.99
session.add(PapaVeggieBurger)
session.commit()
print(PapaVeggieBurger.price)

for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()

veggieBurgerDetails = []
for veggieBurger in veggieBurgers:
    veggieBurgerDetails.append([veggieBurger.id, veggieBurger.price, veggieBurger.restaurant.name])
print(veggieBurgerDetails)

papasPizzas = session.query(Restaurant).filter_by(name = "Papa's Pizzeria")
for place in papasPizzas:
    session.delete(place)
    session.commit()

pizzaPalaces = session.query(Restaurant).filter_by(name = "Pizza Palace").all()
pizzaPalaces[0].name = "Papa's Pizzeria"
session.add(pizzaPalaces[0])
session.commit()
print(pizzaPalaces[0].name)

# spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
# print(spinach.restaurant.name)

# session.delete(spinach)
# session.commit()

# spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()  will give no row was found error
