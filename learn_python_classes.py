# VARIABLE TYPES
print(type(5))

my_dict = {}

print(type(my_dict))

my_list = []

print(type(my_list))

# CLASSES
'''
A class is a template for a data type. 
It describes the kinds of information that class will hold and how a programmer 
will interact with that data. We use the pass keyword in Python to indicate that 
the body of the class was intentionally left blank so we don’t cause an IndentationError.
'''
class Facade:
  pass

# INSTANTIATION
'''
A class doesn’t accomplish anything simply by being defined. 
A class must be instantiated. In other words, we must create an instance of the class, 
in order to breathe life into the schematic.
'''
facade_1 = Facade()

# OBJECT-ORIENTED PROGRAMMING
'''
Instantiation takes a class and turns it into an object, 
the type() function does the opposite of that. 
When called with an object, it returns the class that the object is an instance of.
'''
facade_1_type = type(facade_1)

print(facade_1_type)

# CLASS VARIABLES
'''
When we want the same data to be available to every instance of a class we use a class variable.
You can define a class variable by including it in the indented part of your class definition,
and you can access all of an object’s class variables with object.variable syntax.
'''
class Grade:
  minimum_passing = 65

# METHODS
'''
Methods are functions that are defined as part of a class. 
The first argument in a method is always the object that is calling the method. 
Convention recommends that we name this first argument self. 
Methods always have at least this one argument.
We define methods similarly to functions, except that they are indented to be part of the class.
When you call a method it automatically passes the object calling the method as the first argument.
'''
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

# METHODS WITH ARGUMENTS
'''
Methods can also take more arguments than just self.
'''
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area, teaching_table_area, round_room_area)

# CONSTRUCTORS
'''
here are several methods that we can define in a Python class that have special behavior. 
These methods are sometimes called “magic”, because they behave differently from regular methods. 
Another popular term is dunder methods, so-named because they have two underscores 
(double-underscore abbreviated to “dunder”) on either side of them.

The first dunder method we’re going to use is the __init__ method
This method is used to initialize a newly created object.
It is called every time the class is instantiated.

Methods that are used to prepare an object being instantiated are called constructors. 
Every time we create an instance of a class, the __init__ method will be executed. 
Arguments can be passed to the __init__ method if parameters have been defined. 
'''
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

circle = Circle(36)

# INSTANCE VARIABLES
'''
The data held by an object is referred to as an instance variable. 
Instance variables aren’t shared by all instances of a class — 
they are variables that are specific to the object they are attached to.
'''
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"

isabelles_ices.store_name = "Isabelle's Ices"

print(alternative_rocks.store_name, isabelles_ices.store_name)

# ATTRIBUTE FUNCTIONS
'''
If we attempt to access an attribute that is neither a class variable 
nor an instance variable of an object Python will throw an AttributeError.

hasattr() will return True if an object has a given attribute and False otherwise. 
If we want to get the actual value of the attribute, 
getattr() is a Python function that will return the value of a given object and attribute. 
In this function, we can also supply a third argument that will be the default if the object 
does not have the given attribute.

The syntax and parameters for these functions look like this:

hasattr(object, “attribute”) has two parameters:

object : the object we are testing to see if it has a certain attribute
attribute : name of attribute we want to see if it exists

getattr(object, “attribute”, default) has three parameters (one of which is optional):

object : the object whose attribute we want to evaluate
attribute : name of attribute we want to evaluate
default : the value that is returned if the attribute does not exist (note: this parameter is optional)
'''
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# SELF
'''
Instance variables are more powerful when you can guarantee a rigidity 
to the data the object is holding. This convenience is most apparent when 
the constructor creates the instance variables, using the arguments passed in to it.
We can write our classes to structure the data that we need and write methods 
that will interact with that data in a meaningful way.
'''
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# EVERYTHING IS AN OBJECT
'''
Attributes can be added to user-defined objects after instantiation, 
so it’s possible for an object to have some attributes that are not 
explicitly defined in an object’s constructor. We can use the dir() 
function to investigate an object’s attributes at runtime. 
dir() is short for directory and offers an organized presentation of object attributes.
'''
print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object))

# STRING REPRESENTATION
'''
This is a method we can use to tell Python what we want the string representation 
of the class to be. __repr__ can only have one parameter, self, and must return a string.
'''
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# REVIEW
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))