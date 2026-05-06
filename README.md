# Automobile Inheritance Practice

## Goal

In this activity, you will practice **inheritance** by building a small vehicle inventory system similar to the automobile example from the book.

You will create one general class that stores information all vehicles have in common, then create three more specific vehicle classes that inherit from it.

By the end, you should understand how a subclass can reuse code from a superclass while adding its own specialized data.

---

## Big Idea: Generalization and Specialization

In the real world, some objects are general categories and others are specialized versions of those categories.

For example:

- A vehicle is a general category.
- A car is a more specific kind of vehicle.
- A truck is a more specific kind of vehicle.
- An SUV is a more specific kind of vehicle.

This is an **is a** relationship:

- A car **is a** vehicle.
- A truck **is a** vehicle.
- An SUV **is a** vehicle.

In programming, this relationship can be modeled using **inheritance**.

---

## Vocabulary

| Term | Meaning |
|---|---|
| Class | A blueprint for creating objects |
| Object | An instance of a class |
| Superclass | The general class that other classes inherit from |
| Subclass | A specialized class that inherits from a superclass |
| Inheritance | When one class receives attributes and methods from another class |
| Mutator | A method that changes an attribute value, often called a setter |
| Accessor | A method that returns an attribute value, often called a getter |
| `__init__` method | The constructor method that runs when an object is created |
| `super()` | A way for a subclass to call a method from its superclass |

---

## Project Overview

You will create a Python module named:

```text
vehicles.py
```

Inside that file, you will create these classes:

```text
Automobile
Car
Truck
SUV
```

The `Automobile` class will store the information that every vehicle has.

The `Car`, `Truck`, and `SUV` classes will inherit from `Automobile` and add one extra piece of information specific to that type of vehicle.

You will also create a second file named:

```text
vehicle_demo.py
```

That file will create vehicle objects and print their information.

---

## Part 1: Plan the Superclass

Before writing code, answer these questions in comments at the top of your `vehicles.py` file:

1. What do all vehicles in this example have in common?
2. Which class should be the superclass?
3. Which classes should be subclasses?
4. Why would it be inefficient to write totally separate `Car`, `Truck`, and `SUV` classes with no inheritance?

Do not skip this step. You should be able to explain the design before coding it.

---

## Part 2: Create the `Automobile` Class

Create a class named `Automobile`.

This class should keep track of these four pieces of data:

- make
- model
- mileage
- price

### Requirements

Your `Automobile` class must include:

- an `__init__` method
- private attributes using double underscores
- setter methods for each attribute
- getter methods for each attribute

### Important

Do not just make public variables like this:

```python
self.make = make
```

Use private attributes like the book example does.

Example pattern:

```python
self.__some_attribute = some_value
```

You will need to apply that pattern to all four automobile attributes.

---

## Part 3: Add Mutators and Accessors

In the `Automobile` class, create methods that allow the program to change and retrieve the data.

You should have setter methods similar to:

```text
set_make
set_model
set_mileage
set_price
```

You should also have getter methods similar to:

```text
get_make
get_model
get_mileage
get_price
```

### Check Yourself

Before moving on, your `Automobile` class should be able to answer these questions:

- What is the vehicle's make?
- What is the vehicle's model?
- What is the vehicle's mileage?
- What is the vehicle's price?

---

## Part 4: Create the `Car` Subclass

Now create a class named `Car` that inherits from `Automobile`.

A car has all the regular automobile information, plus one extra piece of information:

- number of doors

### Requirements

The `Car` class must:

- inherit from `Automobile`
- have its own `__init__` method
- use `super()` to initialize the inherited automobile data
- create a private attribute for the number of doors
- have a setter for the number of doors
- have a getter for the number of doors

### Think Before You Code

The `Car` constructor needs to receive five values:

```text
make, model, mileage, price, doors
```

Only one of those values belongs directly to the `Car` class.

The other four should be handled by the superclass.

Your job is to decide which values should be sent to `super()` and which value should be stored by the `Car` class itself.

---

## Part 5: Create the `Truck` Subclass

Create a class named `Truck` that inherits from `Automobile`.

A truck has all the regular automobile information, plus one extra piece of information:

- drive type

Examples of drive type might include:

```text
2WD
4WD
AWD
```

### Requirements

The `Truck` class must:

- inherit from `Automobile`
- have its own `__init__` method
- use `super()` to initialize the inherited automobile data
- create a private attribute for drive type
- have a setter for drive type
- have a getter for drive type

### Hint

If your `Car` class is working, the `Truck` class should feel very similar. The main difference is the name of the extra attribute.

---

## Part 6: Create the `SUV` Subclass

Create a class named `SUV` that inherits from `Automobile`.

An SUV has all the regular automobile information, plus one extra piece of information:

- passenger capacity

### Requirements

The `SUV` class must:

- inherit from `Automobile`
- have its own `__init__` method
- use `super()` to initialize the inherited automobile data
- create a private attribute for passenger capacity
- have a setter for passenger capacity
- have a getter for passenger capacity

---

## Part 7: Create the Demo File

Create a second file named:

```text
vehicle_demo.py
```

At the top of the file, import your `vehicles` module.

Then create one object from each subclass:

- one `Car`
- one `Truck`
- one `SUV`

Use realistic sample data. Do not copy the exact values from another student.

### Example Data Format

Your objects should include information like this:

```text
make
model
year or model name depending on your design
mileage
price
special attribute
```

Remember: your `Automobile` class should only store the fields assigned in this activity. Do not add extra fields unless your teacher approves it.

---

## Part 8: Display the Inventory

In `vehicle_demo.py`, print a small used car inventory report.

Your output should clearly show the information for each vehicle.

Example format:

```text
USED CAR INVENTORY

The following car is in inventory:
Make: 
Model: 
Mileage: 
Price: 
Number of doors: 

The following pickup truck is in inventory:
Make: 
Model: 
Mileage: 
Price: 
Drive type: 

The following SUV is in inventory:
Make: 
Model: 
Mileage: 
Price: 
Passenger capacity: 
```

You need to fill in the values using your getter methods.

Do not print private attributes directly.

---

## Part 9: Test Your Program

Run your demo file.

Your program should:

- import the `vehicles` module successfully
- create three objects successfully
- print all inherited automobile data
- print each subclass's special data
- avoid errors related to missing methods or misspelled names

### Common Errors to Watch For

| Error | Possible Cause |
|---|---|
| `NameError` | You misspelled a class or variable name |
| `AttributeError` | You called a method that does not exist or is spelled differently |
| `TypeError` | Your constructor is missing an argument or has too many arguments |
| Import error | Your file name or import statement is incorrect |
| Private attribute issue | You tried to access `__attribute` directly from outside the class |

---

## Part 10: Add Comments Explaining Inheritance

Add at least three comments in your code that explain what inheritance is doing.

Your comments should explain things like:

- why `Car`, `Truck`, and `SUV` do not need to rewrite the make/model/mileage/price code
- what `super()` is doing
- why each subclass only needs to store its own special attribute

These comments should be in your own words.

---

## Part 11: Reflection Questions

At the bottom of your `vehicle_demo.py` file, answer these questions in comments:

1. Which class is the superclass?
2. Which classes are subclasses?
3. What attributes are inherited by all three subclasses?
4. What attribute is unique to the `Car` class?
5. What attribute is unique to the `Truck` class?
6. What attribute is unique to the `SUV` class?
7. Why is inheritance useful in this example?
8. What could go wrong if you copied and pasted the same automobile code into all three subclasses instead?

---

## Required Files to Submit

Submit both files:

```text
vehicles.py
vehicle_demo.py
```

---

## Grading Checklist

| Requirement | Points |
|---|---:|
| `Automobile` superclass created correctly | 15 |
| Private attributes used in `Automobile` | 10 |
| Getter and setter methods included for automobile data | 15 |
| `Car` subclass uses inheritance and adds doors | 10 |
| `Truck` subclass uses inheritance and adds drive type | 10 |
| `SUV` subclass uses inheritance and adds passenger capacity | 10 |
| Demo file creates one object of each subclass | 10 |
| Output is clear and uses getter methods | 10 |
| Comments explain inheritance and `super()` | 5 |
| Reflection questions completed | 5 |
| **Total** | **100** |

---

## Optional Challenge

After your main program works, add one of these improvements:

### Option A: Better Price Formatting

Display the price with a dollar sign and commas.

Example:

```text
Price: $21,500.00
```

### Option B: Add a `__str__` Method

Add a `__str__` method to one or more classes so the object can return a nicely formatted description of itself.

### Option C: Add Input

Ask the user to enter the information for one vehicle, then create the correct object from the user's answers.

### Option D: Add a New Subclass

Create a new subclass such as:

- Motorcycle
- ElectricCar
- Van

The new subclass must inherit from `Automobile` and add one new unique attribute.

---

## Final Reminder

The goal is not just to make the program run.

The goal is to understand the relationship between a superclass and a subclass.

When you finish, you should be able to say:

```text
A Car is an Automobile.
A Truck is an Automobile.
An SUV is an Automobile.
```

That is inheritance.
