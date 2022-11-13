# Decoupled vs Coupled
class IEngine:
    def do_engine_stuff(self):
        pass

class DiselEngine(IEngine):
    def do_engine_stuff(self):
        pass
## Car & DieselEnginer is coupled
class Car:
    def __init__(self):
        self.engine = DiselEngine()
    
    def accelerate(self):
        self.engine.do_engine_stuff()

## Car & engine are decoupled 
class Car2:
    def __init__(self, engine : IEngine):
        self.engine = engine

    def accelerate(self):
        self.engine.do_engine_stuff()

# _______________________________________________________________________
# Encapsulate what varies

def checkout_book(customer, book):
    if (
        customer and
        customer.fine <= 0.0 and 
        customer.card and 
        customer.card.expiration is None and
        book and not book.is_checked_out
    ):
        customer.books.append(book)
        book.is_checkd_out = True
    return customer
# This is easy to read and wont change even if checkout requirements vary
def checkeout_book(customer, book):
    if (customer.can_check_out(book)):
        customer.checkout(book)
    return customer

# _______________________________________________________________________
# Liskov Substitution Principle (broken)

class Rectangle:
    def set_width(self, width: float):
        self._width = width
    
    def set_height(self, height: float):
        self._height = height

    def area(self):
        return self._width * self._height

## Square is not rectangle
class Square(Rectangle):
    def set_height(self, height: float):
        self._height = height
        self._width = height

    def set_width(self, width: float):
        self._height = width
        self._width = width

rectangle = Square()
rectangle.set_width(5)
rectangle.set_height(2)
# If we are type checking like this we are most defenatly LSP principle
if type(rectangle) is Rectangle:
    assert rectangle.area() == 10
elif type(rectangle) is Square:
    assert rectangle.area() == 4
# _______________________________________________________________________
# Open Close principle

class Order:
    def __init__(self):
        pass
    
    def shipping(self, shipping):
        # If/Else Indicates we are breaking OCP Use Interface for shipping and add Ground and Air
        if(shipping == "ground"):
            return 0
        if(shipping == "air"):
            return 1
