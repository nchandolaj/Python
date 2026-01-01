# Map Functions

In Python, `map()` is a built-in function that allows you to process and transform all the items in an iterable (like a list or tuple) without using an explicit `for` loop. It is a cornerstone of **functional programming** in Python.

## 1. How it Works
The `map()` function applies a specific function to every item in an iterable and returns a **map object** (which is an iterator). 

**The Syntax:**
$$map(function, iterable)$$

## 2. Basic Usage
Instead of writing a loop to square every number in a list, you can do it in one line.

```python
numbers = [1, 2, 3, 4]

# Step 1: Define the transformation logic
def square(x):
    return x * x

# Step 2: Use map
result = map(square, numbers)

# Step 3: Convert the map object back to a list to see it
print(list(result)) # Output: [1, 4, 9, 16]
```

## 3. Using `map()` with Lambda
Since `map()` requires a function as its first argument, it is almost always paired with a **Lambda function** for quick, one-off transformations.

```python
prices = [10, 20, 30]

# Add 10% tax to every price
taxed_prices = list(map(lambda p: p * 1.1, prices))

print(taxed_prices) # Output: [11.0, 22.0, 33.0]
```

## 4. Mapping Multiple Iterables
`map()` can take more than one iterable. If you provide multiple lists, the function must take that many arguments. It will stop as soon as the shortest list is exhausted.

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Add corresponding elements from two lists
sums = list(map(lambda x, y: x + y, list1, list2))

print(sums) # Output: [11, 22, 33]
```

## 5. Map vs. List Comprehension
In modern Python, **List Comprehensions** are often preferred over `map()` because they are generally considered more "Pythonic" and readable.

| Method | Syntax |
| :--- | :--- |
| **Map** | `list(map(lambda x: x*2, nums))` |
| **List Comp** | `[x*2 for x in nums]` |

**When to use `map()`?** Use it when the function you are applying is already defined (like `map(int, ["1", "2"])`) or when you are working with very large datasets where you want to keep the result as an iterator to save memory.

