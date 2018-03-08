#!/usr/bin/python3.6

# DECORATORS

# From https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
# Decorators have to be customized to the function and its arguments?

def p_decorate(func):
  def func_wrapper(name):
    # format.<object> replaces the {0} index
    return "<p>{0}</p>".format(func(name))
  return func_wrapper

def strong_decorate(func):
  def func_wrapper(name):
    return "<strong>{0}</strong>".format(func(name))
  return func_wrapper

def div_decorate(func):
  def func_wrapper(name):
    return "<div>{0}</div>".format(func(name))
  return func_wrapper

def my_shiny_new_decorator(func):
  # Create a modified function to return
  def wrapper_around_func():
    print('Before function runs ...')
    func()
    print('After function runs ...')
  return wrapper_around_func

def standalone_func():
  print('Standalone function!.')

def func():
  return func

# Assign object to variable
obj = func

# Assign function call to variable
o_call = func()

def shout(word='yes'):
  return word.capitalize() + '!'

def getTalk(kind='shout'):

  def shout(word='yes'):
    return word.capitalize() + '!'

  def whisper(word='yes'):
    return word.lower() + '...'

  if kind == 'shout':
    return shout
  else:
    return whisper

if __name__ == '__main__':

  talk=getTalk() # function shout is returned
  talk_obj=getTalk # function getTalk is returned, DIFFERENT!
  print('TALK_OBJ')
  print('Printing TALK_OBJ')
  print(talk_obj)
  print('Printing TALK_OBJ()')
  print(talk_obj())

  print('TALK')
  print('Printing TALK')
  print(talk) # returns object
  print('Printing TALK()')
  print(talk()) # returns

