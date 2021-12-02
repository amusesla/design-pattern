""" Dependency Inversion Principle(DIP)

1. high level classes or module should not dpend directly on low level moduels.
Instaed, they should depends on abstraction.

So essentially you just want to depend on interfaces rather than concrete implementations.
because taht waywhat you can do is you can swap one for the other.

*does not directly related to dependency injection.

"""

from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
	PARENT  = 0
	CHILD   = 1
	SIBLING = 2

class Person:
	def __init__(self, name):
		self.name = name

class RelationshipBrowser:
	@abstractmethod
	def find_all_children_of(self, name): pass

# low level moduel (good)
class Relationships(RelationshipBrowser):
	def __init__(self):
 		self.relations = []

	def add_parent_and_child(self, parent, child):
		self.relations.append(
			 (parent, Relationship.PARENT, child)
		)
		self.relations.append(
			(child, Relationship.CHILD, parent)
		)

	def find_all_children_of(self, name):
		for r in self.relations:
			if r[0].name == name and r[1] == Relationship.PARENT:
				yield r[2].name

# low level module (bad)
# class Relationships:
# 	def __init__(self):
# 		self.relations = []

# 	def add_parent_and_child(self, parent, child):
# 		self.relations.append(
# 			(parent, Relationship.PARENT, child)
# 		)
# 		self.relations.append(
# 			(child, Relationship.CHILD, parent)
# 		)

class Research:
	def __init__(self, browser):
		for p in browser.find_all_children_of('John'):
			print(f'John has child called {p}')

# high level module(bad)
# class Research:
# 	def __init__(self, relationships):
# 		relations = relationships.relations
# 		for r in relations:
# 			if r[0].name == 'John' and r[1] == Relationship.PARENT:
# 				print(f'John has a child called {r[2].name}.')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

""" BAD : Imagine if you decide to change from a list to dictionary(relations).
In this case, what's happening is your accessing the internal storage mechanism of relations,
which is a low level module in your high level module. 
"""


