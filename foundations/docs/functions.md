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

