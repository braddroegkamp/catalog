from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

# Create session and connect to DB
engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="First User", email="first.user@firstuser.com")
session.add(User1)
session.commit()


# Items for categoryA
categoryA = Category(user_id=1, name="categoryA")

session.add(categoryA)
session.commit()


item1a = Item(user_id=1, name="item1a", description="This is item 1a!",
              category=categoryA)

session.add(item1a)
session.commit()


item2a = Item(user_id=1, name="item2a", description="This is item 2a!",
              category=categoryA)

session.add(item2a)
session.commit()


item3a = Item(user_id=1, name="item3a", description="This is item 3a!",
              category=categoryA)

session.add(item3a)
session.commit()


# Items for category2
categoryB = Category(user_id=1, name="categoryB")

session.add(categoryB)
session.commit()


item1b = Item(user_id=1, name="item1b", description="This is item 1b!",
              category=categoryB)

session.add(item1b)
session.commit()


item2b = Item(user_id=1, name="item2b", description="This is item 2b!",
              category=categoryB)

session.add(item2b)
session.commit()


# Items for category3
categoryC = Category(user_id=1, name="categoryC")

session.add(categoryC)
session.commit()


item1c = Item(user_id=1, name="item1c", description="This is item 1c!",
              category=categoryC)

session.add(item1c)
session.commit()


print "added initial categories and items!"
