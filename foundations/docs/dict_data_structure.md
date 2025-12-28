# Python Deep Dive: The Python Dictionary (The Hash Table)

The Python dictionary (`dict`) is a highly optimized, **compact, ordered hash table**. Significant changes made in Python 3.6 (and formalized in 3.7) transformed the dictionary from a memory-heavy structure to one that is both space-efficient and maintains insertion order.

## 1. The Modern Structure: Indices and Entries

Before Python 3.6, dictionaries used a single large sparse table. Now, they use a **two-array design** to save memory.

### The `entries` List

This is a dense array that stores the actual data. Each "slot" in this list contains:

* **The Hash:** The full hash of the key.
* **The Key:** A pointer to the key object.
* **The Value:** A pointer to the value object.

### The `indices` List

This is a sparse array that acts as the "map." It only stores integers (indices) that point to the position of the data in the `entries` list.

## 2. The Algorithm: From Key to Index

When you execute `d['key'] = 'value'`, Python follows a specific mathematical pipeline.

### Step 1: The Hash Function

Python calls the internal `hash()` function on the key.

* **Output:** A 64-bit integer (on 64-bit systems).
* **Constraint:** The key must be **hashable** (immutable objects like strings, ints, or tuples).
* **Randomization:** For security (to prevent Hash DoS attacks), Python adds a random "seed" to hashes so they change every time you restart Python.

### Step 2: Modulo for Slot Selection

The hash is much larger than the `indices` list. 

To find a home for the key, Python uses a bitwise mask (effectively a modulo operation).

**index = hash(key) & (mask)** ; where `mask = size_of_indices - 1`.

### Step 3: Probing (Collision Resolution)

If the calculated slot in the `indices` list is already taken by a different key (a **collision**), Python uses **Linear Probing** with a tweak. It uses a **"perturbation" algorithm** to jump to a different slot based on the higher-order bits of the hash:

**j = ((5 times j) + 1 + text{perturb}) & text{mask}**

This ensures that if two keys collide initially, they don't immediately collide on the next jump.

## 3. Memory Management Decisions

The decision to split the table into `indices` and `entries` was a major architectural turning point.

### Why the Change? (Compact Dictionaries)

In the old design, the table was sparse, meaning many "rows" were empty. Since each row contained 24 bytes (hash, key ptr, val ptr), an empty row wasted significant space.

* **New Design:** The `indices` list uses the smallest possible integer type (1 byte for `int8`, 2 bytes for `int16`, etc.) based on the dict size.
* **Space Savings:** This reduced memory footprint by roughly **20% to 25%**.

### The Growth Strategy (Resizing)

Python doesn't wait until the `indices` list is 100% full to grow.

* **Load Factor:** When the dictionary is **2/3 full**, Python triggers a resize.
* **Allocation:** The new size is typically doubled.
* **Re-indexing:** Python creates a new, larger `indices` list and re-inserts all items from the `entries` list. Because the `entries` list is dense, this operation is very cache-friendly for the CPU.

## 4. Key Design Decisions

| Feature | Decision Logic |
| :--- | :--- |
| **Ordering** | By using the dense `entries` list, insertion order is naturally preserved. This was originally an implementation detail but became a language feature. |
| **Deletion** | When an item is deleted, Python doesn't shift the `entries` list (too slow). It marks the slot in `indices` as a **Dummy** (or "Deleted") marker so the probing chain isn't broken. |
| **Small Dicts** | For very small dictionaries, Python pre-allocates space for 8 entries to avoid immediate resizing overhead. |

## 5. Summary of Workflow

1.  **Hash:** `hash("name")` $\rightarrow$ `123456789`
2.  **Map:** `123456789 & 7` (for an 8-slot table) $\rightarrow$ `5`
3.  **Check Indices:** Look at `indices[5]`. If empty, put the next available `entries` index (e.g., `0`) there.
4.  **Store Data:** Put `(hash, "name", "value")` into `entries[0]`.

---

# FAQs

## 1. Does Python create a new entries list of three items (hash, key, value) for every element of the dict object?

Python does not create a separate list object for every element.** Instead, Python allocates **one contiguous block of memory** for the `entries` array. 

Within that single block, it carves out space for "rows," where **each row is a C-struct (not a Python list)** containing exactly three fields: the hash, a pointer to the key, and a pointer to the value.

**The Entry Structure in C**

At the C level (CPython), an entry is defined as a `PyDictKeyEntry`. It is a fixed-size structure:

* **`me_hash` (8 bytes):** Stored as a raw integer so Python doesn't have to re-calculate the hash during lookups or resizing.
* **`me_key` (8 bytes):** A pointer to the Python object used as the key.
* **`me_value` (8 bytes):** A pointer to the Python object used as the value.

Each "row" in the `entries` array is exactly **24 bytes**.

**Allocation Strategy: "The Big Block"**

When you create a dictionary, Python allocates a single chunk of memory to hold multiple entries at once.

1.  **Initial Size:** Python starts by allocating space for **8 entries**. Even if your dictionary has only 1 item, the `entries` array has room for 8 (consuming $8 \times 24 = 192$ bytes for the data part).
2.  **Contiguous Memory:** Because these entries sit side-by-side in RAM, the CPU can scan them very quickly. This is called **Data Locality**.
3.  **Growth:** When you add the 6th item (reaching the 2/3 load factor), Python discards the old block and allocates a new, larger contiguous block (usually doubling the size).

**Visualizing the Memory Layout**
If you have a dictionary `d = {"a": 1, "b": 2}`, the memory looks like this:

| Array Type | Index 0 | Index 1 | Index 2 | ... | Index 7 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Indices** (Sparse) | `0` | `-1` (empty) | `1` | `-1` | `-1` |
| **Entries** (Dense) | `[Hash_A, Ptr_A, Ptr_1]` | `[Hash_B, Ptr_B, Ptr_2]` | (Free) | (Free) | (Free) |

> **Note:** The `indices` list maps the "hash-slotted" position to the actual row number in the `entries` list. This is why the `entries` list can stay "dense" (no gaps) while the `indices` list remains "sparse" (lots of gaps).

**Key Decision: Why a C-struct instead of a Python List?**

Python developers chose a C-array of structs for two major reasons:

1.  **Memory Overhead:** A Python `list` is itself an object with a reference count, type pointer, and size. If every entry were a Python list, you would add **64+ bytes of overhead per key-value pair**. By using a C-struct, the overhead is **zero** beyond the data itself.
2.  **Pointer Indirection:** To read a Python list, the CPU has to "jump" to the list's memory address, then "jump" again to the data. With the current `dict` design, the hash, key, and value pointers are already sitting right next to each other in memory.

