# Lambda Functions

A **Lambda function** in Python is a small, anonymous function that is defined without a name. While standard functions are defined using the `def` keyword, lambdas use the `lambda` keyword. 

They are often called "one-liners" because they are restricted to a single expression.

## 1. Syntax and Structure
The structure of a lambda is very specific:
$$\text{lambda } \text{arguments} : \text{expression}$$

* **Arguments:** Just like a regular function, it can take any number of inputs.
* **Expression:** This is the logic that gets executed and **automatically returned**. You cannot use statements like `return`, `pass`, or `assert` inside a lambda.

## 2. Standard vs. Lambda Comparison
To understand the difference, look at how we would write a function that squares a number:

**Using `def`:**
```python
def square(x):
    return x * x

print(square(5)) # Output: 25
```

**Using `lambda`:**
```python
square_lambda = lambda x: x * x

print(square_lambda(5)) # Output: 25
```

## 3. Advanced Sorting (The "Key" Parameter)
The most powerful use of lambda in Python is as a "helper" inside other functions, especially `sort()` or `sorted()`. This allows you to sort complex data structures (like lists of lists or dictionaries).

### **Example: Sorting a List of Tuples**
Imagine you have a list of students and their grades, and you want to sort by the **grade** (the second element), not the name.

```python
students = [("Alex", 88), ("Bernie", 95), ("Charlie", 78)]

# x represents each tuple in the list
# x[1] tells Python to use the grade for sorting
students.sort(key=lambda x: x[1])

print(students)
# Output: [('Charlie', 78), ('Alex', 88), ('Bernie', 95)]
```

### **Example: Sorting by Multiple Criteria**
You can even sort by the length of a string, or any other logic:
```python
words = ["apple", "banana", "cherry", "date"]
words.sort(key=lambda x: len(x))

print(words) # Output: ['date', 'apple', 'banana', 'cherry']
```

## 4. Lambda with Map and Filter
Lambdas are frequently paired with `map()` (to transform data) and `filter()` (to extract data).

| Function | Purpose | Example |
| :--- | :--- | :--- |
| **Map** | Applies logic to every item | `map(lambda x: x * 2, [1, 2, 3])` |
| **Filter** | Keeps items that are True | `filter(lambda x: x > 10, [5, 12, 18])` |

## 5. When to Avoid Lambdas
While they are convenient, you should avoid them if:
* **The logic is complex:** If you need `if/else` blocks (beyond a simple ternary) or multiple lines, use a real `def` function.
* **Readability suffers:** If a teammate (or future you) can't understand the one-liner at a glance, it's better to name the function.

