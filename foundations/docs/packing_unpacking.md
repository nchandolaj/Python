# Python: Packing and Unpacking

In Python, **packing** and **unpacking** refer to the ability to group multiple values into a single variable or, conversely, extract individual values from an iterable (like a list or tuple) into multiple variables.

Think of it like moving house: **Packing** is putting items into a box; **Unpacking** is taking them back out to set up your new room.

## 1. Unpacking
Unpacking allows you to assign elements of an iterable to multiple variables in a single line.

### **Basic Unpacking**
The number of variables on the left must match the number of items in the iterable.

```python
coordinates = (10, 20, 30)
x, y, z = coordinates

print(x) # 10
print(y) # 20
```

### **Extended Unpacking (The `*` Operator)**
If you don't know how many items are in the list, or you only care about a few, use the `*` operator to "catch" the remaining items.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

first, *middle, last = fruits

print(first)  # "apple"
print(middle) # ["banana", "cherry", "date"] (always returns a list)
print(last)   # "elderberry"
```

## 2. Packing
Packing occurs when you collect multiple values into a single variable. This most commonly happens in **function arguments**.

### **Packing with `*args`**
When you use `*` in a function definition, Python packs all positional arguments into a **tuple**.

```python
def sum_all(*numbers):
    # 'numbers' is now a tuple: (1, 2, 3, 4)
    return sum(numbers)

print(sum_all(1, 2, 3, 4)) # 10
```

### **Packing with `**kwargs`**
The `**` operator packs named (keyword) arguments into a **dictionary**.

```python
def create_profile(**details):
    # 'details' is now a dictionary: {"name": "Alex", "age": 25}
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile(name="Alex", age=25)
```

## 3. Quick Comparison

| Feature | Operator | Action | Resulting Type |
| :--- | :--- | :--- | :--- |
| **Unpacking** | `a, b = [1, 2]` | Spreads values into variables | Multiple variables |
| **Packing** | `*args` | Collects values into one variable | Tuple |
| **Dictionary Packing** | `**kwargs` | Collects key-value pairs | Dictionary |

### **A Common Use Case: Swapping Variables**
Python uses unpacking behind the scenes to let you swap variables without a "temporary" third variable:

```python
a = 5
b = 10

a, b = b, a # b and a are "packed" into a tuple and then "unpacked"
```

---

**Would you like to try a small coding exercise where you have to use `*args` and `**kwargs` together?**
