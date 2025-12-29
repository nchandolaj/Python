# `dict` Memory Allocation

## How Python Allocates Memory for an Empty Dictionary

In Python, when you instantiate an empty dictionary using `d = {}` or `d = dict()`, Python doesn't just allocate a single "bucket" for data. It pre-allocates a specific structure to ensure that the dictionary is ready for high-performance operations immediately.

Here is a breakdown of how that memory is managed at the CPython level.

### 1. The `PyDictObject` Structure
Every Python dictionary is an instance of a C structure called `PyDictObject`. Even when empty, this object takes up a non-trivial amount of memory (usually **64 bytes** to **240 bytes** depending on the Python version and 64-bit architecture) because it contains:

* **Reference Count:** To track how many variables point to this dict.
* **Type Information:** A pointer to the dictionary class.
* **Metadata:** Fields to track the size, number of used slots, and a "version" tag for optimizations.

### 2. The Hash Table (Keys & Values)
Python dictionaries are implemented as **hash tables**. In modern Python (3.6+), dictionaries are "compact," meaning the memory is split into two distinct arrays:

* **The Indices Array:** A small array of integers (the "hash table" part).
* **The Entries Array:** An array that stores the actual `hash`, `key`, and `value`.

### 3. Pre-allocation (Over-provisioning)
When you create an empty dictionary, Python doesn't wait for the first insertion to allocate space for entries. It **pre-allocates** space for **8 slots** by default. 

* **Why 8?** This is a heuristic balance. It’s large enough to hold most small dictionaries without needing to resize immediately, but small enough to keep memory overhead low.
* **The Power of 2:** Python always keeps the table size at a power of 2 ($2^n$). When the dictionary gets about 2/3 full (the "load factor"), Python will trigger a resize, usually doubling or quadrupling the allocated memory.

### 4. Memory Usage Example
Even though there are zero items, the bytes reported by the system represent the "skeleton" of the dictionary and the initial 8-slot entry table. Using `sys.getsizeof()` on an empty dictionary typically returns 64 or 240 bytes depending on your specific Python build.

```python
import sys

empty_dict = {}
print(sys.getsizeof(empty_dict)) # Outputs 64 (or 240 in some environments)
```

### Summary Table: Empty Dict Allocation
| Component | Purpose | Status at Instantiation |
| :--- | :--- | :--- |
| **Header** | Ref counting & GC tracking | Fully allocated |
| **Indices** | Mapping hashes to entries | Pre-allocated (8 slots) |
| **Entries** | Storing Key/Value pointers | Pre-allocated (8 slots) |
| **Load Factor** | Deciding when to resize | Initialized to 0 |

---
# Relevant sub-topics

## The Structure of the Entries Array

To understand the Structure of the **Entries Array**, we have to look at the C source code of CPython (specifically `dictobject.h`).

### 1. What type is the Entries Array?
The entries array is a contiguous array of `PyDictKeyEntry` structures. 

```c
typedef struct {
    Py_hash_t me_hash;    /* Cached hash code of me_key */
    PyObject *me_key;     /* Pointer to the key object */
    PyObject *me_value;   /* Pointer to the value object */
} PyDictKeyEntry;
```

It is **not** a generic array of pointers; it is an array of **structs**. Each struct contains three fields:
1.  **me_hash**: A signed integer (64-bit on most modern systems) representing the cached hash code of the key.
2.  **me_key**: A pointer to the Python object used as the key.
3.  **me_value**: A pointer to the Python object used as the value.

### 2. Is it instantiated with 8 blocks during `dict()`?
**Yes.** When a dictionary is first created, Python allocates space for **8** of these `PyDictKeyEntry` structures. 

* The **Indices Array** is initialized with a size of 8 (containing dummy values like `-1` to indicate "empty").
* The **Entries Array** is allocated to match, providing 8 empty slots ready to be filled. 

This is why `sys.getsizeof({})` is relatively high compared to an empty list. Python is "paying upfront" for those 8 slots to avoid the overhead of calling `malloc` the very first time you add a key.

### 3. Does it contain actual keys/values or pointers?
It contains **pointers**.

In Python, almost everything is an object living on the **Heap**. The dictionary does not "swallow" the object and store it inside its own memory block. Instead:
* The **Key** column stores the **memory address** of the key object.
* The **Value** column stores the **memory address** of the value object.

**Why pointers?** This allows the dictionary to store any data type (strings, integers, custom classes) in a uniform way. Since every pointer is the same size (8 bytes on a 64-bit system), the `PyDictKeyEntry` struct has a predictable, fixed size. 

### Visual Summary of one "Entry" Block
If you add `d["name"] = "Alice"`, one of the 8 slots in the entries array will look like this:

| Field | Content | Size (approx) |
| :--- | :--- | :--- |
| **me_hash** | `123456789` (The hash of "name") | 8 bytes |
| **me_key** | `0x7ffee123` (Address of the string "name") | 8 bytes |
| **me_value** | `0x7ffee456` (Address of the string "Alice") | 8 bytes |
| **Total** | | **24 bytes per slot** |

Since Python pre-allocates 8 of these, that's $8 \times 24 = 192$ bytes just for the entries array, which explains the majority of the memory footprint of an empty dict.

## Dictionary Deletion and Dummy Placeholders

When you delete a key in Python, the dictionary doesn't physically "shrink" the array. Instead, it uses a sentinel value to maintain the integrity of the hash table.

### 1. Why Dummies Exist
Python uses **Open Addressing**. If a deletion left a truly empty (NULL) hole in a collision chain, subsequent lookups for keys further down that chain would stop prematurely, thinking the key doesn't exist.

### 2. The Deletion Process
When `del d[key]` is called:
* The `me_value` pointer is set to `NULL` (releasing the value object).
* The `me_key` pointer is redirected to a unique global **Dummy** object.

### 3. Behavior of Dummy Slots
* **Lookups:** Treat the slot as "occupied by something else"—the search continues to the next slot.
* **Insertions:** Treat the slot as "available"—the new key/value overwrites the dummy.

### 4. Memory Impact
Deleting items does **not** reduce the memory usage of the dictionary. The size of the Entries Array only changes during a resize event (usually triggered by adding items, not removing them).

### 5. When does the memory actually get freed?
The only way to "shrink" the dictionary and clear out the dummy entries is to trigger a **resize**. This happens when:
* You add enough new items to exceed the load factor (approx. 2/3 full).
* Python allocates a **new, fresh table** and copies only the active keys into it, leaving the dummies behind.

