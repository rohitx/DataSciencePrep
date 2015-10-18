## Table of Contents

1. [__Data Structures__](#Data Structures)
 1. [List Methods](#list-methods)
 2. [Set Methods](#set-methods)
2. [__Set Methods__](#Sets)
3. [__Python Classes__](#python-classes)


## List Methods
A *list* is a mutable ordered sequence of items. The items of a list are arbitrary objects and may be of different types. Lists are defined by square brackets and each element is separated by a comma.

Let's look at methods associated with lists

![Lists](figures/figure.jpg)

## Set Methods
In Python `set` and `frozenset` represent arbitrarily unordered collection of unique items. Set objects provide several methods as shown below.

![Sets](figures/figure-1.jpg)
![Sets](figures/figure-2.jpg)

>All mutating methods of set objects, except `pop`, return None


## Python Classes

Python is an object-oriented programming languge, which means it manipulates programming constructs called **objects**. You can think of an object as a single data structure that contains data as well as functions; functions of objects are called **methods**.

A basic class consists only of the `class` keyword, the name of the class, and the class from which the new class **inherits** in parentheses. Our classes will inherit from the `object` class like so:

```python
class NewClass(object):
    # Class commands here
```

In addition to the object we write in the class, we also make use of the `__init__()` function. This function required for classes, and it's used to **initialize** the objects it creates. The `__init__()` function always takes at least one argument, `self`, that refers to the object being created. You can think of `__init__()` as the function that 'boots up' each object the class creates. So for example, we will have:

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
```
The `self` is used by Python to refer to the object being created. This is why it is often called `self`, since this parameter gives the object being created its identify.

Once we have created a class as seen above, we can start to instantiate (create) our first object. Let's use the Animal class and create an animal with a name:

```python
class Animal(object):
    def __init__(self, name):
        self.name = name

kangaroo = Animal('Amanda')
# This command will print the name
print kangaroo.name
```
Now the first argument in an `__init__()` gets is used to refer to the instance object, and by convection that argument is called `self`. If you add additional arguments --for instance name, and age for your object--setting each of those equal to self.name and self.age in the body of the `__init__()` will make it so that when you create an instance object of your `Animal` class, you need to give each instance a name, and age, and those will be associated with the particular instance you create. For example,

```python
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

kangaroo = Animal('Amanda', 2)
# This command will print the name
print kangaroo.name
print kangaroo.age
```

Another important aspect of Python classes is scope. The scope of a variable is the context in which it's visible to the program. Variables that are available everywhere are called **global variables** while those that are only available to members of a certain class are called **member variables**. Variables that are only available to particular instance of a class are called **instance variables**. For example, the variable `is_alive` is a global variable as it is available to all the objects created in the class.

```python
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When a class has its own functions, those functions are called **methods**. We have already seen `__init__()` method. But we can have more. Here `description()` is another method. Note that methods have parentheses while variables such as global variables do not.

```python
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Shere Khan", 35)
hippo.description()
hippo.is_alive
```

**Inheritance** is the process by which one class takes on the attributes and methods of another, and it's used to express an **is-a** relationship. For example, a 'Panda is a bear', so a Panda class could inherit from a Bear class. However, Toyota is not a Tractor so it cannot inherit from a Tractor class. But both Toyota and Tractor are vehicles and so they both inherit from the Vehicle class. In Python, inheritance has a general structure such as:

```python
class DerivedClass(BaseClass):
    # code here
```

Here's another:

```python
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
```

Sometimes you'll work on a derived class or **subclass** and realize that you've overwritten a method or attribute defined in that class' base class (also called a parent or **superclass**). YOu can directly access the attributes or methods of a superclass with Python's built-in `super` call. Here's an example:

```python
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return self.hours * 12

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Ada')
print milton.full_time_wage(10)
```