# Filter Function

In Python, `filter()` is the companion to `map()`. While `map()` **transforms** every item in a list, `filter()` **selects** items based on whether they meet a specific condition.

## 1. How it Works
The `filter()` function calls a specified function for each item of an iterable and returns only those for which the function returns `True`.

**The Syntax:**
$$filter(function, iterable)$$

## 2. Basic Usage
To use `filter()`, you need a function that returns a **Boolean** (`True` or `False`).

```python
numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Define the condition
def is_even(n):
    return n % 2 == 0

# Step 2: Apply filter
evens = filter(is_even, numbers)

# Step 3: Convert to list
print(list(evens)) # Output: [2, 4, 6]
```

## 3. Using `filter()` with Lambda
Just like `map()`, `filter()` is most efficient when used with a lambda function for simple logic.

```python
users = ["admin", "guest", "alex", "root", "user123"]

# Only keep usernames longer than 4 characters
long_users = list(filter(lambda name: len(name) > 4, users))

print(long_users) # Output: ['admin', 'guest', 'user123']
```

## 4. Map and Filter Together
You will often see these two functions chained together. For example, "Filter out the odd numbers, then square the remaining even numbers."

```python
nums = [1, 2, 3, 4, 5]

# 1. Filter for evens: [2, 4]
# 2. Map to square them: [4, 16]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print(result) # Output: [4, 16]
```

## 5. Comparison: Map vs. Filter vs. Reduce

| Function | Action | Result Size |
| :--- | :--- | :--- |
| **Map** | Transform every item | Same as input |
| **Filter** | Select items based on condition | Smaller than or equal to input |
| **Reduce** | Combine all items into one | A single value |
