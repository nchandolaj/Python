# Introduction to Python

*Focus: This topic covers the basics of the Python langauge. This page also serves as a placeholder for elementary language topics that aren't covered as a separated detailed discussion elsewhere.*

Python is a high-level, general-purpose programming language that has become the industry standard for everything from web development to data science and artificial intelligence. 
Created by *Guido van Rossum* and first released in 1991, its design philosophy centers on one thing: **readability.**

## 1. An Interpreted Language
Unlike "compiled" languages (like C++ or Rust) where the entire program must be translated into machine code before it can run, Python is **interpreted**.

* **How it works:** An "interpreter" reads your code line-by-line and executes it immediately.
* **The Benefit:**
  - **Debuggability:** This makes debugging much faster because you can see errors the moment the interpreter hits a problematic line.
  - **Portablility:** It also makes Python "platform-independent," meaning the same code can run on Windows, Mac, or Linux without modification.

## 2. Structural Whitespace (Indentation)
In most programming languages, indentation is just for visual neatness. In Python, **it is a syntax requirement.**

* **Code Blocks:** While other languages use curly braces `{ }` to show where a function or loop starts and finishes, Python uses **indentation** (standardized as 4 spaces).
* **The Logic:** If two lines of code have the same level of indentation, they belong to the same block. If a line is indented further, it is "nested" inside the statement above it.

**Example Comparison:**

```python
# Other languages (like JS) use braces:
if (isLoggedIn) {
  console.log("Welcome!");
}

# Python uses indentation:
if is_logged_in:
    print("Welcome!")  # This space defines the block
```
