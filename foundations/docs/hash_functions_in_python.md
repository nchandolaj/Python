Hash Functions in Python Collections

In Python, a **hash function** is a deterministic algorithm that takes an input (like a string, integer, or tuple) and returns a fixed-size integer, known as a **hash value**. 

In collections like `dict` and `set`, this hash value is used to calculate the specific index where data is stored, allowing for near-instantaneous retrieval.

---

## 1. How Python Uses the Hash Function
When you execute an operation like `my_dict["key"] = "value"`, Python performs the following steps:

1.  **Hashing:** The key is passed into the internal `hash()` function.
    * Example: `hash("key")` → `123456789`
2.  **Indexing:** Python uses a bitmask (effectively $hash \pmod{size}$) to map that large integer to a specific slot index in the underlying array.
3.  **Storage:** The key-value pair is stored in that specific "bucket."



---

## 2. Requirements for an Effective Hash Function
For a hash table to maintain $O(1)$ lookup speeds, the hash function must satisfy three criteria:

* **Determinism:** The same input must *always* produce the same hash value within the same process.
* **Efficiency:** It must be computationally inexpensive to calculate.
* **Uniformity:** It must distribute keys evenly across the available slots to prevent "clustering."

---

## 3. Handling Hash Collisions
A **collision** occurs when two different keys result in the same index. 



Python resolves this using **Open Addressing**. If a slot is already occupied:
1.  Python calculates a new index based on a pseudo-random perturbation of the original hash.
2.  It "probes" the next slot to see if it is empty.
3.  During lookup, Python checks the index; if the key doesn't match, it follows the same probe sequence until the key is found or an empty slot is encountered.

---

## 4. Why Immutability is Mandatory
Only **hashable** objects can be used as keys in a dictionary or elements in a set. 
* **Immutable types** (int, str, float, tuple) are hashable because their content never changes, ensuring their hash remains constant.
* **Mutable types** (list, dict, set) are **not** hashable. If a list's content changed after being stored, its hash would change, and Python would look in the "wrong" bucket, making the data unretrievable.

---

## 5. Security: Hash Seed Randomization
To prevent **Hash Denial of Service (DoS)** attacks, Python applies a random "seed" to hashes of strings and bytes. This means `hash("Python")` will produce different results in two different terminal sessions. This prevents attackers from predicting collisions that could slow a dictionary lookup from $O(1)$ to $O(n)$.

---

## 6. Performance Summary

| Operation | Average Complexity | Worst Case |
| :--- | :--- | :--- |
| **Insertion** | $O(1)$ | $O(n)$ |
| **Lookup** | $O(1)$ | $O(n)$ |
| **Deletion** | $O(1)$ | $O(n)$ |

> **Note:** The worst-case $O(n)$ occurs only when the hash table is extremely crowded or the hash function results in excessive collisions. Python automatically resizes the table to avoid this.
