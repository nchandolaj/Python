# Hash Functions in Computer Science

A **Hash Function** is a mathematical algorithm that maps data of arbitrary size (often called a "message" or "key") to a bit string of a fixed size (the "hash value," "digest," or "fingerprint"). 

Mathematically, it can be represented as:
$$h = H(S)$$
Where $S$ is the input data and $h$ is the resulting fixed-size integer.

> In Python, a **hash function** is a deterministic algorithm that takes an input (like a string, integer, or tuple) and returns a fixed-size integer, known as a **hash value**.
> In the context of hash collections like `dict` and `set`, this hash value is used to calculate the specific index where that data should be stored in memory.

---

## 1. Core Properties of a "Good" Hash Function

To be useful in Computer Science, a hash function must possess several key characteristics:

* **Determinism:** The same input must always result in the same output.
* **Efficiency:** It must be computationally fast to generate the hash.
* **Pre-image Resistance:** It should be computationally infeasible to reverse the process (find $S$ from $h$).
* **Avalanche Effect:** A small change in the input (changing one bit) should result in a drastically different hash.
* **Collision Resistance:** It should be extremely difficult to find two different inputs that produce the same output ($H(S_1) = H(S_2)$).

---

## 2. Common Use Cases

### **A. Data Structures (Hash Tables/Maps)**
This is the most common use in software engineering. Hash functions allow for $O(1)$ average-time complexity for data retrieval.
* **How it works:** The hash value acts as an index in an array where the data value is stored.
* **Example:** Python `dict`, Java `HashMap`, C++ `unordered_map`.

### **B. Data Integrity & Checksums**
Used to verify that data hasn't been corrupted during transmission or storage.
* **How it works:** A file's hash is calculated before and after transfer. If the hashes match, the file is intact.
* **Algorithms:** CRC32, MD5 (non-cryptographic), SHA-256.

### **C. Cryptography & Security**
Used to protect sensitive information like passwords.
* **How it works:** Instead of storing a plain-text password, systems store the hash. When you log in, your input is hashed and compared to the stored version.
* **Salting:** To prevent "Rainbow Table" attacks, a random string (salt) is added to the password before hashing.

### **D. Deduplication & Caching**
Hash functions can identify duplicate files or data blocks across massive systems without comparing the entire content byte-by-byte.

---

## 3. Python Implementation Examples

### **Simple Non-Cryptographic Hash (For Data Structures)**
Python provides a built-in `hash()` function for objects. Note that for strings, this value is randomized per session for security.

```python
# Hashing different data types
print(f"Hash of 'Gemini': {hash('Gemini')}")
print(f"Hash of 42: {hash(42)}")
print(f"Hash of (1, 2, 3): {hash((1, 2, 3))}")

# Lists are mutable and therefore NOT hashable
try:
    hash([1, 2, 3])
except TypeError as e:
    print(f"Error: {e}")
```

### Cryptographic Hashing (Using hashlib)
For security or data integrity, use the hashlib library which implements algorithms like SHA-256.

```python
import hashlib

def generate_sha256(text):
    # Encode the string to bytes
    encoded_text = text.encode()
    
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(encoded_text)
    
    # Return the hexadecimal representation of the digest
    return hash_object.hexdigest()

data = "Top Secret Message"
print(f"SHA-256 Digest: {generate_sha256(data)}")
```
---

## 4. Hash Collisions and Resolution
Because the input space is infinite and the output space is finite (e.g., a 256-bit integer), collisions are mathematically inevitable (based on the **Pigeonhole Principle**).

**Resolution Strategies:**
* **Chaining:** Each bucket in the hash table points to a linked list of all items that hashed to that index.
* **Open Addressing:** If a collision occurs, the system looks for the next available "slot" in the array using a probe sequence.

---
## 5. Summary Table
| Category | Typical Algorithms | Primary Goal |
| :--- | :--- | :--- |
| Non-Cryptographic | MurmurHash, FNV-1, Jenkins | Speed, Uniformity |
| Cryptographic | SHA-256, SHA-3, BLAKE2 | Security, Collision Resistance |
| Checksums | CRC32, Adler-32 | Error detection in transmission |

> **Note:**
> * **Warning:** MD5 and SHA-1 are now considered "broken" for cryptographic purposes because collisions can be generated relatively easily with modern hardware. Use **SHA-256** or better for security.
