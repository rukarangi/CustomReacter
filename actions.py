import discord
import re
from database import dbSession, User

def addUser(name, id, admin):
    user = User(name=name, discordid=id, admin=admin)
    try:
        dbSession.add(user)
        dbSession.commit()
        print(f"added user: {name}")
    except:
        print(f"user: {name} id already in the database")
    
    return