# `dict` Hash Collisons



## Detailed Hash Collision Handling in Python's 8-Slot Dictionary

When multiple keys produce the same initial index—a **hash collision**—Python must find an alternative slot. It uses a robust mechanism called **Open Addressing with Perturbative Probing**.

### 1. The Initial Index Calculation
Before a collision even occurs, Python determines the starting slot using the key's hash. For an empty dictionary with **8 slots**, the mask is `7` (binary `111`).
* The index is calculated as: `index = hash(key) & mask`.
* If the `Indices Array` at that position contains `-1`, the slot is empty and no collision occurs.

### 2. The Probing Algorithm (The "Next" Slot)
If the initial slot is occupied by a different key, Python enters a loop to find the next available slot. Unlike simple linear probing (which just checks `index + 1`), Python uses a formula designed to scramble the search pattern and avoid "clustering."

The CPython source code defines the recurrence relation for the next index as:
`j = ((5 * j) + 1 + perturb) & mask`

#### Breaking down the variables:
* **`5 * j + 1`**: This multiplier ensures that the probe sequence will eventually visit every single slot in the table (since 5 is coprime to any power of 2).
* **`perturb`**: This is initialized to the full `hash(key)`. In each iteration of the probe, it is updated using `perturb >>= 5` (right-shifted by 5 bits).
* **`mask`**: For an 8-slot dict, this is always `7`. It ensures the result stays within the bounds of the array.

### 3. The Logic of "Perturb"
The use of `perturb` is Python's "secret sauce" for high performance. 
* **Lower Bits vs. Higher Bits:** Initial indices only use the lowest bits of a hash. If two keys have hashes that end in the same three bits (e.g., `...010` and `...010`), they will collide.
* **Scrambling the Sequence:** By incorporating the right-shifted higher bits of the hash into the `perturb` value, Python ensures that these two keys will follow **completely different** probe sequences after the first collision. This prevents "clumping" where many keys fight over the same sequence of fallback slots.

### 4. Comparison Logic During Probing
At every probed slot, Python performs a two-stage check to see if it has found the correct key:
1.  **Identity Check (`is`):** It compares the memory addresses of the keys. If `key_in_slot is new_key`, it's a match. This is lightning-fast.
2.  **Equality Check (`==`):** If the addresses differ, it checks if the hashes match. If the hashes match, it finally calls the `__eq__` method. This order prevents expensive equality checks (like comparing long strings) unless it is highly likely they are the same.

### 5. Collision Capacity and Resizing
Because collisions degrade performance from $O(1)$ toward $O(n)$, Python strictly manages the **Load Factor**.
* **The 2/3 Rule:** Once the dictionary is roughly **66% full** (5 or 6 items in an 8-slot table), the collision probability becomes too high.
* **The Resize:** Python will allocate a new, larger table (typically doubling in size to 16 slots) and "re-hash" all existing keys into the new slots. This effectively resets the collision chains.


### Summary Table: Collision Resolution
| Feature | Implementation | Purpose |
| :--- | :--- | :--- |
| **Strategy** | Open Addressing | Keep all data in one contiguous memory block. |
| **Probing** | `(5*j + 1 + perturb) & mask` | Avoid linear clusters and visit all slots. |
| **Perturbation** | `hash >> 5` | Use higher-order hash bits to diversify probe paths. |
| **Equality** | `is` then `==` | Optimize for speed by avoiding unnecessary method calls. |

---

## Detailed Trace of a Hash Collision and Probing Sequence

This trace demonstrates the mathematical path Python takes when two distinct keys hash to the same initial index in an 8-slot dictionary.

### 1. The Scenario
We are working with a standard 8-slot dictionary (Mask = `7` or `0b111`). 
* **Key A Hash:** `...000101` (Binary) $\rightarrow$ Decimal `5`.
* **Key B Hash:** `...011101` (Binary) $\rightarrow$ Decimal `29`.

**Initial Index Calculation:**
* Key A: `5 & 7 = 5`
* Key B: `29 & 7 = 5`

Since Key A is already stored at **Index 5**, Key B triggers a **collision**.

### 2. Step 1: The Initial Collision
Python attempts to place Key B at **Index 5**.
* It checks the `Indices Array` at position 5.
* It finds a pointer to an entry containing **Key A**.
* It performs an identity check: `Key B is Key A` (False).
* It performs an equality check: `Key B == Key A` (False).
* **Result:** Python must find a new slot using the probing formula.

### 3. Step 2: The First Probe
Python calculates the next index using the recurrence: `j = (5 * j + 1 + perturb) & mask`.

* **Current j:** 5
* **Perturb:** 29 (Initial perturb is the full hash value)
* **Calculation:** `(5 * 5) + 1 + 29 = 55`
* **Masking:** `55 & 7 = 7`
* **Result:** Python moves to **Index 7**.

Python checks Slot 7. If it is empty (`-1`), Key B is stored here. If Slot 7 is occupied by a different key, it continues to the second probe.

### 4. Step 3: The Second Probe
Before the next calculation, Python updates the `perturb` value to incorporate higher-order bits of the hash.

* **Update Perturb:** `perturb >>= 5` (In C, `29 >> 5` results in **0**).
* **Current j:** 7
* **Calculation:** `(5 * 7) + 1 + 0 = 36`
* **Masking:** `36 & 7 = 4`
* **Result:** Python moves to **Index 4**.

### 5. Why This Sequence is Effective
| Probe | Index | Why it chose this |
| :--- | :--- | :--- |
| **Start** | 5 | Determined by the lowest 3 bits of the hash (29 & 7). |
| **Probe 1** | 7 | Influenced by the initial index and the full hash value. |
| **Probe 2** | 4 | Influenced by the previous index and shifted hash bits. |

Even if another key (Key C) also collided at **Index 5** but had a different full hash (e.g., hash = 13), its `perturb` value would be different, leading it to a **different** first probe index. This "shuffling" prevents different collision chains from merging into one long, slow sequence.

### 6. Final Logic: Insertion
Once an empty (`-1`) or **Dummy** slot is found:
1. The **Entries Array** gets a new struct: `{hash: 29, key: &KeyB, value: &ValueB}`.
2. The index of this new entry (e.g., `1` if it's the second item added) is written into the **Indices Array** at the resolved probe position (e.g., Index 7).

