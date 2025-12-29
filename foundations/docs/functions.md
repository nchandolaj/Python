# Python Functions

*Focus: Gain an understanding of Python functions.*

In Python, functions are the building blocks of reusable code. They allow you to group a set of instructions together so you can run them multiple times without rewriting them.

## The `def` Keyword
The `def` keyword (short for **define**) is used to create a function. It tells Python: "I am about to define a block of code that should only run when I call it later."

```python
def function_name():
    # Code block starts here
    print("Hello, World!")

# Calling the function
function_name()
```
### Key Rules for `def`:
* **The Colon (:):** Every `def` statement must end with a colon.
* **Indentation:** The code inside the function must be indented (usually 4 spaces).
* **Naming:** Function names should be lowercase and use underscores (e.g., `calculate_total`).

## Parameters vs. Arguments
These terms are often used interchangeably, but there is a specific technical difference between them based on where they are used.

### 1. Parameters (The Placeholders)
Parameters are the variables listed inside the parentheses in the **function definition.** They act as placeholders for the data the function needs to do its job.

### 2. Arguments (The Real Data)
Arguments are the actual values sent to the function when it is **called**.

### Comparison Table
| Feature | Parameter | Argument |
| :--- | :--- | :--- |
| **Location** | Found in the def line. | Found in the function call. |
| **Purpose** | Defines what kind of data is needed. | Provides the actual data to work with. |
| **Example** | def greet(name): (name is the parameter) | greet("Alice") ("Alice" is the argument) |

## Putting it Together
In a typical setup, the value provided in the function call is assigned to the parameter name for the duration of that specific function execution.

```python
# 'length' and 'width' are **PARAMETERS**
def calculate_area(length, width):
    area = length * width
    print(f"The area is {area}")

# 5 and 10 are **ARGUMENTS**
calculate_area(5, 10)
```
In this case, the value **5** is assigned to length and **10** is assigned to width for the duration of that specific function call.

---

# Default Arguments or keyword arguments (`**kwargs`)

## 1. Default Arguments
Sometimes you want a parameter to have a "standard" value if the user doesn't provide one. You can assign this directly in the `def` line.
```python
def greet(name, message="Welcome!"):
    print(f"Hello {name}, {message}")

greet("Alice")               # Uses default: Hello Alice, Welcome!
greet("Bob", "Good morning") # Overrides default: Hello Bob, Good morning
```
> **Note:** Parameters with default values must always come **after** parameters without default values.

## 2. Keyword Arguments (`kwargs`)
Normally, arguments are assigned by position. However, you can also pass them by name. This makes your code much more readable, especially with many parameters.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Using keyword arguments (order doesn't matter here)
describe_pet(pet_name="Luna", animal_type="Cat")
```

## 3. Handling Multiple Arguments: `*args` and `**kwargs`
What if you don't know how many items a user will send? Python uses two special symbols for this:

### `*args` (Non-Keyword Arguments)
The asterisk (`*`) packs all extra positional arguments into a **tuple**. Use this when you want to pass a list-like collection of items.

### `**kwargs` (Keyword Arguments)
The double asterisk (`**`) packs all extra named arguments into a **dictionary**. Use this when you want to pass a set of named properties.

### Example in Action
```python
def make_pizza(size, *toppings, **delivery_details):
    print(f"Making a {size} pizza with:")
    for topping in toppings:
        print(f"- {topping}")
    
    if "address" in delivery_details:
        print(f"Shipping to: {delivery_details['address']}")

make_pizza("Large", "Pepperoni", "Mushrooms", address="123 Python Lane")
```

### Summary Checklist
* `*args`: Turns arguments into a Tuple ().
* `**kwargs`: Turns arguments into a Dictionary {}.
* **Order matters**: The standard order in a function definition is: `standard parameters`, `*args`, `default parameters`, `**kwargs`.

---

# Function Arguments - Pass By Object Reference

## Python's Passing Mechanism: Pass by Object Reference
Python does not use standard "Pass by Value" or "Pass by Reference." Instead, it passes a reference to the object. The outcome depends on whether the object can be changed (mutable) or not (immutable).

### 1. Immutable Objects (Integers, Strings, Tuples)
When you pass an immutable object, the function cannot modify the original value. Any attempt to change it results in the creation of a new object locally within the function scope.

> **Result:** The original variable outside the function remains unchanged.

> **The Exception:** When you prefix an immutable object (like an integer or string) with the `global` keyword inside a function, you are granting that function the authority to **reassign** the global variable to a new value. Without the `global` keyword, trying to change an immutable variable inside a function simply creates a new local variable, leaving the original untouched. With `global`, you are telling Python: "Don't create a local variable; change the one sitting in the global scope."

### 2. Mutable Objects (Lists, Dictionaries, Sets)
When you pass a mutable object, the function receives a reference to the same object used outside. Modifying the object (e.g., adding an item to a list) affects the original variable.

> **Result:** The original object is updated.

### 3. The "Reassignment" Trap: Modifying vs. Reassigning
It is important to note that even with mutable objects, **reassigning** the variable inside the function breaks the link to the original.
* **Modifying:** Changing the contents of a mutable object (e.g., `list.append()`) updates the original.
* **Reassigning:** Setting the parameter to a brand new value (e.g., `list = [1, 2]`) breaks the link to the original variable and creates a new local reference.

```python
# CASE 1: Modifying (Changes the original)
def modify_list(items):
    items.append(4)  # Modifies the existing object in memory

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

# CASE 2: Reassigning (Does NOT change the original)
def reassign_list(items):
    items = [10, 20] # Points 'items' to a brand new object; link to original is broken

another_list = [1, 2, 3]
reassign_list(another_list)
print(another_list) # Output: [1, 2, 3]
```

### Comparison Summary
* Immutable types: Original stays the same (looks like Pass by Value).
* Mutable types: Original can be changed (looks like Pass by Reference).

