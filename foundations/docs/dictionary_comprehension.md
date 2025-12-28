# Dictionary Comprehension

Just like list comprehensions, **Dictionary Comprehensions** allow you to create dictionaries in a single, readable line of code. They follow a very similar logic but require a **key-value pair** instead of a single element.

## 1. Basic Syntax
A dictionary comprehension uses curly braces `{}` and a colon `:` to separate the key from the value.

**The Goal:** Create a dictionary where the key is a number and the value is its square.

**The Standard Way**
```python
numbers = [1, 2, 3, 4]
squares_dict = {}

for n in numbers:
    squares_dict[n] = n**2
```
**The Dictionary Comprehension Way**
```python
squares_dict = {n: n**2 for n in numbers}

# Result: {1: 1, 2: 4, 3: 9, 4: 16}
```

## 2. Conditional Logic (Filtering)
Just like with lists, you can add an `if` statement at the end to filter which items are included.

**The Goal:** Create a dictionary of even numbers and their cubes.
```python
cubes_of_evens = {n: n**3 for n in range(10) if n % 2 == 0}

# Result: {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
```

## 3. Transforming Existing Dictionaries
Dictionary comprehensions are incredibly useful for modifying data already stored in a dictionary, such as swapping keys and values or adjusting values.

**The Goal:** Convert a dictionary of prices from Dollars to Euros.
```python
prices_usd = {'milk': 2.50, 'bread': 1.50, 'eggs': 3.00}
exchange_rate = 0.92

prices_eur = {item: price * exchange_rate for (item, price) in prices_usd.items()}

# Result: {'milk': 2.3, 'bread': 1.38, 'eggs': 2.76}
```

## 4. Swapping Keys and Values
A common technical interview task is to "invert" a dictionary.

```python
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {value: key for (key, value) in original.items()}

# Result: {1: 'a', 2: 'b', 3: 'c'}
```

## Pro-Tip
Use `.items()` when iterating over an existing dictionary in a comprehension. It allows you to access both the key and the value simultaneously, making your code much cleaner.

