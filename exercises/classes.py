#!/usr/bin/python3.6

# CLASSES

class MyClass:

  # Default initialization method
  # Will be called when class is instantialized
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart

  def f(self):
    return 'Helloworld!'

class Dog:

  # Data attributes will OVERRIDE class methods
  # Best to have a convention for class methods
  # Maybe start method name with a _

  # this variable is shared by ALL instances of this class
  # tricks = []

  def __init__(self,name):
    self.name = name
    self.tricks = []

  def _add_trick(self, trick):
    self.tricks.append(trick)

  def _show_tricks(self):
    return self.tricks

if __name__ == '__main__':
  d = Dog('Fido')
  d._add_trick('roll over')
  d._add_trick('play dead')
  print(d._show_tricks())
