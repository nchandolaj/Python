# Python Control Flow: Comparators, Logical Operators, and Conditionals

*Focus: Master Python's decision-making power. Understand how the language evaluates truth. This involves three layers: comparing values, combining those comparisons, and using the result to branch your code.*


## 1. Comparators (Relational Operators)
Comparators are symbols used to compare two values. Every comparison results in a **Boolean** value: either `True` or `False`.

| Operator | Meaning | Example | Result |
| :--- | :--- | :--- | :--- |
| `==` | **Equal to** | `5 == 5` | `True` |
| `!=` | **Not equal to** | `5 != 3` | `True` |
| `>` | **Greater than** | `10 > 5` | `True` |
| `<` | **Less than** | `2 < 1` | `False` |
| `>=` | **Greater than or equal to** | `5 >= 5` | `True` |
| `<=` | **Less than or equal to** | `4 <= 1` | `False` |

> **Warning:** A common beginner mistake is using a single `=` (assignment) instead of `==` (comparison). 
> * `x = 10` sets the value. 
> * `x == 10` asks if the value is 10.


## 2. Logical Operators
Logical operators allow you to combine multiple comparisons into a single complex condition.

### `and` (The Strict Operator)
Returns `True` only if **both** statements are true.
* `(5 > 3) and (10 < 20)` $\rightarrow$ `True`
* `(5 > 3) and (10 > 20)` $\rightarrow$ `False`

### `or` (The Flexible Operator)
Returns `True` if **at least one** statement is true.
* `(5 > 3) or (10 > 20)` $\rightarrow$ `True`
* `(1 == 2) or (10 == 20)` $\rightarrow$ `False`

### `not` (The Reverser)
Flips the result. If something is `True`, `not` makes it `False`.
* `not (5 == 5)` $\rightarrow$ `False`


## 3. Conditionals: `if`, `elif`, `else`
Conditionals use the Boolean results from the operators above to determine which block of code to execute.

### The `if` Statement
The starting point. If the condition is `True`, the indented code runs.

### The `elif` (Else If) Statement
Used to check additional conditions only if the previous ones were `False`. You can have as many `elif` blocks as you need.

### The `else` Statement
The "catch-all." It runs only if **none** of the preceding conditions were `True`.


### Comprehensive Example:
```python
temperature = 25
is_raining = True

if temperature > 30:
    print("It's a hot day!")
elif temperature >= 20 and not is_raining:
    print("Perfect weather for a walk.")
elif temperature >= 20 and is_raining:
    print("It's warm but wet. Bring an umbrella.")
else:
    print("It might be a bit chilly.")
```

