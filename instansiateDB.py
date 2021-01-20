from database import engine
from sqlalchemy import Table, MetaData
from sqlalchemy import create_engine, Column, Integer, String, Boolean


meta = MetaData()

users = Table(
	'users', meta,
	Column('id', Integer, primary_key=True),
	Column('name', String(20), nullable = False),
	Column('discordid', Integer, unique=True, nullable = False),
	Column('admin', Boolean),
)

meta.create_all(engine)