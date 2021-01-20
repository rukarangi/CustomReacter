from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database.db", echo=True)
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
dbSession = DBSession()

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable = False)
	discordId = Column(Integer, unique=True, nullable = False)
	admin = Column(Boolean)

	def __str__(self):
		return f"User: {name} {discordId}"

	def as_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"discordId": self.discordId
		}

