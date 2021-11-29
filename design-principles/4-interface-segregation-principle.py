""" Interface Segregation Principle(ISP)

IDEA

Making interfaces which feature too many element is not a good idea!!!
split them into smallest interface you can build.

Instead of having one large interface with serveral methods in it,
keep things granular. split interface into separate parts that people can implement!

Instead of having this machine class, you would have a class called printer class!
"""

# This interface seems like a good idea 
# because somebody is making a multifunction printer,
# then everything is fine!
from abc import abstractmethod


class Machine:
	def print(self, document):
		raise NotImplementedError

	def fax(self, document):
		raise NotImplementedError

	def scan(self, document):
		raise NotImplementedError

""" OK """
class MultiFunctionPrinter(Machine):
	def print(self, document):
		pass

	def fax(self, document):
		pass

	def scan(self, document):
		pass

""" PROBLEM: in case we build another printer!

Remeber we only have 'Machine' interface to work with.
However somebody is gonna make oldFashion instance
they are still going to see fax & scan as a member.

end up calling fax & scane method, but there is absolutely no effect!


"""
class OldFashionPrinter(Machine):

	# OK
	def print(self, document):
		# certainly for printing, an old fashion printer can print!
		pass
	
	# NOT OK
	def fax(self, document):
		# 1. BAD: DO NOTHING!
		pass

	# NOT OK
	def scan(self, document):
		# 2. BAD: RAISE AN ERROR!
		raise NotImplementedError('Printer cannot scan!')


""" GOOD
"""

class Printer:
	@abstractmethod
	def print(self, document):
		pass


class Scanner:
	@abstractmethod
	def scan(self, document):
		pass

class MyPrinter(Printer):
	def print(self, document):
		print(document)

class Photocopier(Printer, Scanner):
	def print(self, documnet):
		pass

	def scan(self, documnet):
		pass


class MultiFunctionDevice(Printer, Scanner):

	@abstractmethod
	def print(self, documnet):
		pass

	@abstractmethod
	def scan(self, document):
		pass

class MultiFunctionMachine(MultiFunctionDevice):

	def __init__(self, printer, scanner):
		self.scanner = scanner
		self.printer = printer

	def print(self, document):
		self.printer.print(document)

	def scan(self, document):
		self.scanner.scan(document)