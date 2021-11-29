""" Liskov Substitution Principle(LSP)

IDEA
If you have a class that inherited base class,
the interface that takes base class should work with inherited class

"""

class Rectangle:
	def __init__(self, width, height):
		self._height = height
		self._width = width

	@property
	def area(self):
		return self._width * self._height

	def __str__(self):
		return f'Width: {self._width}, Height: {self._height}'

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

class Square(Rectangle):
	def __init__(self, size):
		Rectangle.__init__(self, size, size)

	@Rectangle.width.setter
	def width(self, value):
		self._width = self._height = value

	@Rectangle.height.setter
	def height(self, value):
		self._height = self._width = value

# Works fine with 'Rectangle'
# rc = Rectangle(2, 3)
# user_it(rc)

""" Breaking the liskov substitution principle using inheritance

PROBLEM
side effect of rc.height is also changing the width of Square. 
since the class 'Square' uses the size for width and height, 
the w = rc.width in function 'use_it', no longer valid.

from the High level perspective,
this function only works for 'class Rectangle'.
This does not work on any derived classes!!

This is the Direct violation of 'Liskov Substitution Principle'

"""
def user_it(rc):
	w = rc.width

	# PROBLEM
	rc.height = 10
	expected = int(w * 10)
	print(f'Expected area of {expected}, got {rc.area}')

sq = Square(5)
user_it(sq)

