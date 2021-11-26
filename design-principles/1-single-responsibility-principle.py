"""Single Responsibility Principle(SRP) / Seperation Of Concerns(SOC)
1. 'Class' should have its primary responsibility
2. Avoid 'God Object' - Don't overload your objects with too many responsibilities!
3. Enforeces idea that should have a single reason to change.
4. Changes that should related to primary responsibility.

"""
# 'Class' Should have its primary responsibility!!
# It should not take on other responsibility!
# Avoid 'GOD OBJECT', Don't overload your objects with too mnay responsibilities!
# It enforces idea that a class should have a single reaons to change
# and that change should be somehow related to it's primary responsibility.

class Jounal:
    """
    Jounal's primary responsibility is to keep the entries!!
    """

    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entires[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)


    """
    Break SRP!!!
    Break the single responsbility principle
    giving a 'Jounal' additional responsibility
    """

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, url):
    #     pass

    """
    Problem!!!
    We've added a secondary responsibility to the jounal.
    Not only does the Jounal now store entires and allow us to mainipulate the entires,
    but it's now taking on the responsbility of persistence by providing functionality for
    saving and loading the jouanl from resoruces.

    This is a bad idea for a number of reasons.
    1. If you think about a complete application.
    you also have other different types might have their own save and load 
    and this functionality might have to be centrally changed at some point.

    you have to go every single class inside your application
    and change their save method or change their load method
    """

j = Jounal()
j.add_entry('I creid today')
j.add_entry('I was a car')

class PersistenceManager:
    """ Responsible for saving a particular object. like jounal
    """

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

# file = r''
# PersistenceManager.save_to_file(j, file)
# with open(file) as fh:
#     print(fh.read())


""" ANTI PATTERN
1. God Object
Everythin in the kitchen sink into a single class

It enforces idea that a class should have a single reaons to change
and that change should be somehow related to it's primary responsibility.
"""