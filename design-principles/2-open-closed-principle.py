""" Open Close Principle(OCP)

open for extension!
closed for modification!

"""

from enum import Enum

class Color(Enum):
    RED   = 1
    GREEN = 2
    BLUE  = 3


class Size(Enum):
    SMALL  = 1
    MEDIUM = 2
    LARGE  = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Imagine if one of the requirements in application
# is being able to filter products by colour.
class ProductFilter:

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    """ NOT GOOD """
    # Needs for filtering size
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    # This entire apporach does not sacle!
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

""" Violate Open closed principles

When you add new functionality,
you add by extention not by modification

In addition to breaking the 'open close principle',
it's causing a 'state of space explosion' lel

"""

""" GOOD: Enterprise pattern """
# 1. Specification

class Specification:
    # Determines whether or not a particular item satisfies a particular criteria

    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        # large_blue = large & ColorSpecification(Color.BLUE)
        return AndSpecification(self, other)

class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):

    def __init__(self, size):
        self.size = size 

    def is_satisfied(self, item):
        return item.size == self.size


class Filter:
    def filter(self, items, spec):
        pass

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':

    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree  = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]


    """ BAD EXAMPLE """
    # pf = ProductFilter()
    # for p in pf.filter_by_color(products, Color.GREEN):
    #     print(f' - {p.name} is green')

    """ GOOD EXAMPLE """
    pf = BetterFilter()

    green = ColorSpecification(Color.GREEN)
    for p in pf.filter(products, green):
        print(p.name)

    large = SizeSpecification(Size.LARGE)
    for p in pf.filter(products, large):
        print(p.name)

# Combinator ---
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))
# end: combinator ---

# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))

large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
for p in pf.filter(products, large_blue):
    print('Product(large and blue):', p.name)

