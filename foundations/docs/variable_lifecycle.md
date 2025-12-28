# Python Deep Dive: Python Variable

`Focus: Understanding the Lifecycle of a Python Variable - From Memory Allocation to Deallocation`

In Python, the lifecycle of a variable is managed by the **CPython Runtime**. Unlike lower-level languages where you manually manage memory, Python uses an automated system that abstracts the interaction between your code and the OS.

## 1. Declaration vs. Instantiation: Is there a distinction?

In languages like C or Java, you **declare** a variable by stating its type (e.g., `int x;`), which reserves memory. In Python, these concepts are merged and behave differently.

* **Declaration:** In Python, declaration does not exist in the traditional sense. You cannot reserve a name without a value. A "declaration" only happens at the moment of **Binding**.
* **Instantiation:** This is the process of creating an **object** (an instance of a class) in memory.
* **The Python Distinction:** When you write `x = 1000`, Python:
    1.  **Instantiates** an integer object with the value `1000` on the heap.
    2.  **Binds** the name (label) `x` to that object.

> **Key Takeaway:** In Python, variables are just **names pointing to objects**. The variable itself doesn't "hold" the data; it holds a reference (memory address) to the object that holds the data.

## 2. The Lifecycle Stages

The lifecycle of an object follows four distinct phases:

### A. Creation and Allocation
When an object is created, the **Python Memory Manager** looks for a free block in its private heap.
* If the object is a small integer (between -5 and 256), Python doesn't create a new object; it points your variable to a `pre-allocated `interned" object` to save memory.
* For larger objects, it allocates a `PyObject` structure.

### B. Reference Counting (The "Live" Phase)
Every object has a header called `ob_refcnt`. 
* If you set `y = x`, the reference count for the object `1000` increases to 2.
* If you pass the object to a function, the count increases.
* As long as the count is $> 0$, the OS/Python keeps the memory reserved.

### C. Garbage Collection (The "Cleanup" Phase)
Python uses two mechanisms to end the lifecycle:

#### 1. Immediate Deallocation
As soon as a reference count hits zero, the memory is marked as free. For the vast majority of objects, the "frequency" of collection is **instantaneous**. As soon as an object's reference count reaches zero, **Python's memory manager** immediately calls the deallocation function for that object. 

There is no waiting period or background "sweep" for these objects.
* **Trigger:** The `ob_refcnt` hitting 0.
* **Timing:** Real-time (Deterministic).
* **Result:** The memory block is returned to Python's internal **Free List** or **Pool** so it can be reused immediately by the next variable you create.

#### 2. Generational GC 
Periodically, Python scans for "Reference Cycles" (Object A points to B, and B points to A, but no one else points to them). If an object has a reference count of 0, the Generational Garbage Collector (the `gc` module) never even sees it—it's already gone. 

The GC exists specifically to find objects that have a reference count **greater than zero** but are unreachable (Circular References). The frequency of this "Cyclic GC" is not based on time (seconds), but on **Allocation Thresholds**.

### The Three Generations
Python categorizes objects into three generations based on how many "surveys" they have survived:
* **Generation 0:** Newly created objects.
* **Generation 1:** Objects that survived one GC sweep.
* **Generation 2:** Long-lived objects.

**The Threshold Trigger**
The GC runs based on a **net allocation count**:
$$\text{Net Allocations} = \text{Allocations} - \text{Deallocations}$$

You can check your current thresholds using `gc.get_threshold()`:
```python
import gc
print(gc.get_threshold()) 
# Output: (700, 10, 10)
```

* **Gen 0 Sweep:** Occurs when the number of allocations minus deallocations exceeds 700. This happens very frequently in active programs.
* **Gen 1 Sweep:** Occurs after Generation 0 has been swept 10 times.
* **Gen 2 Sweep:** Occurs after Generation 1 has been swept 10 times (and usually only if the "long-lived" object count has grown sufficiently).

### D. Releasing to the OS
Python is "greedy." When an object is deleted, Python usually keeps that memory in its **Private Heap** for future Python objects rather than giving it back to the OS immediately. It only returns memory to the OS when an entire **Arena** (256KB block) is completely empty.

## 3. Memory Allocation for Different Data Types

Because "Everything is an Object," Python data types have significant overhead compared to raw C types. You can check the size of any object using `sys.getsizeof()`.

### Common Data Types (on a 64-bit system)

| Data Type | Memory Usage (Approx) | Why so large? |
| :--- | :--- | :--- |
| **int (0)** | 24 - 28 bytes | Includes ref count, type pointer, and size. |
| **float** | 24 bytes | Simple double-precision values wrapped in an object. |
| **str (empty)** | 49 - 51 bytes | Includes encoding info, length, and hash cache. |
| **list (empty)** | 56 bytes | Includes space for pointers to elements. |
| **dict (empty)** | 232 bytes | Large because it uses a hash table for $O(1)$ lookup. |

### Why Integers Grow
Python integers have **arbitrary precision**. If you store a massive number, Python allocates more "digits" (30-bit chunks) to accommodate it.
* `sys.getsizeof(1)` $\rightarrow$ 28 bytes
* `sys.getsizeof(10**100)` $\rightarrow$ 72 bytes

## 4. Summary Table

| Phase | Responsibility |
| :--- | :--- |
| **Name Binding** | Mapping a string (label) to a memory address in a **Namespace**. |
| **Object Allocation** | Requesting a block from the **Python Heap**. |
| **Deallocation** | Decrementing `ob_refcnt` and triggering the **Garbage Collector**. |
