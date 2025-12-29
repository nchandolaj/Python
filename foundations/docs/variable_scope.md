# Local and Global Variable

In Python, **Scope** determines where a variable can be seen and used. The two most common types are Local and Global.

## 1. Global Variables
A global variable is declared **outside** of all functions. It is accessible from anywhere in your code—both inside and outside of functions.

* **Lifetime:** They exist as long as the program is running.
* **Purpose:** Best for constants or configurations that every part of your program needs to know.

```python
# This is a Global Variable
city = "New York"

def show_city():
    # We can read the global variable here
    print(f"The city is {city}")

show_city()
print(city) # Also accessible outside
```

## 2. Local Variables
A local variable is declared **inside** a function. It only exists while that function is executing.

* **Lifetime:** They are created when the function starts and destroyed when the function finishes.
* **Purpose:** Used for temporary data that doesn't need to be remembered once the function is done.

```python
def get_total():
    # This is a Local Variable
    total = 100
    print(total)

get_total()
# print(total)  <-- This would cause a NameError
```

## Comparison Table
| Feature | Local Variable | Global Variable |
| :--- | :--- | :--- |
| **Declaration** | Inside a function body. | Outside of all functions. |
| **Accessibility** | Only within that specific function. | Anywhere in the script. |
| **Lifetime** | Deleted when function ends. | Lives until the program exits. |
| **Safety** | High (won't affect other parts). | Low (easy to change accidentally). |

## The `global` Keyword
By default, you can **read** a global variable inside a function, but you cannot **change** it. If you try to change it, Python creates a new local variable with the same name instead (this is called "shadowing").

To actually modify a global variable, you must use the `global` keyword:

```python
count = 0 # Global

def increment():
    global count # Tells Python to use the global one, not create a local one
    count += 1

increment()
print(count) # Output: 1
```

### Key takeaway: Variable Shadowing
If you have a global variable named `x` and a local variable named `x`, Python will always prioritize the **local** one while inside the function. 
This ensures that functions remain independent and don't accidentally "break" the rest of your program.
