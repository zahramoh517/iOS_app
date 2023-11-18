from flask import Flask
import flask

# create a class for the users. The class will contain all the user information.

class Users:

  def __init__(self, name, email, password):
    self.name = name
    self.password = password
    self.email = email
    return

  def get_name(self):
    return self.name
  
  def get_password(self):
    return self.password
  
  def get_email(self):
    return self.email