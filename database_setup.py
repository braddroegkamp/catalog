from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///item_catalog.db')

Base.metadata.drop_all(engine)


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name': self.name,
			'id': self.id,
			'email': self.email,
			'picture': self.picture,
		}


class Category(Base):

	__tablename__ = 'category'

	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'user_id': self.user_id
		}


class Item(Base):

	__tablename__ = 'item'

	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	last_time = Column(DateTime, default=datetime.now)

	@property
	def serialize(self):
		return {
			'name':  self.name,
			'description':  self.description,
			'id':  self.id,
			'category_id': self.category_id,
			'user_id': self.user_id,
			'last_time': self.last_time
		}


Base.metadata.create_all(engine)