from sqlalchemy import Column, String, Integer, Boolean , ForeignKey
from sqlalchemy.orm import relationship,validates
from services.database_service import base
import re

class UserModel(base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    surname=Column(String)
    username=Column(String,unique=True)
    email=Column(String,unique=True)
    password=Column(String)
    
    password=relationship("Passwords",back_populates="user")
    
    @validates("email")
    def validate_email(self,key,email):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email):
            raise ValueError(f"Invalid email address: {email}")
        return email

class Password(base):
    __tablename__="Passwords"
    id=Column(Integer,primary_key=True,autoincrement=True)
    username_or_email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    description=Column(String,nullable=True)
    user_id=Column(Integer,ForeignKey("Users.id"),nullable=False)
    user=relationship("Users",back_populates="password")
