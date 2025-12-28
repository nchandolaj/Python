# Python Deep Dive: Memory Management

Python is an **interpreted language**, meaning it doesn't talk to the OS directly; it uses the Python Interpreter (**CPython**) as a mediator.

## 1. The Memory Hierarchy: Python vs. OS
When you start a Python process, the OS allocates a **large chunk of virtual memory** to the interpreter. Python then takes over management of that block so it doesn't have to "ask" the OS for permission every time you create a small variable (which would be slow).

### The OS Layer (Raw Memory)
The OS manages physical RAM using **Pages**. When Python needs more space, it makes a system call (like `malloc` in C) to request more pages. The OS doesn't care about "integers" or "strings"; it only sees **blocks of bytes.**

### The Python Layer (The Heap)
Python manages a **Private Heap**. `This is where all Python objects and data structures live.`
* **Arenas:** The largest chunks of memory (256 KB) aligned on page boundaries.
* **Pools:** Arenas are broken into pools (4 KB), which correspond to the size of a virtual memory page.
* **Blocks:** Pools are subdivided into blocks of specific sizes (e.g., a pool for 16-byte objects, a pool for 32-byte objects).

## 2. Object Allocation: "Everything is an Object"
In Python, even a simple integer is a complex C structure. When you write `x = 1000`, the following happens:

1.  **Object Creation:** Python creates a `PyObject` on the heap.
2.  **Ref Count:** It initializes a `ob_refcnt` (Reference Count) to 1.
3.  **Type Pointer:** It sets a pointer to the "Int" type object so Python knows how to treat this data.
4.  **Value:** It stores the actual value.

Because of this overhead, **a simple integer in Python can take up 28 bytes of memory, whereas in C it might only take 4 bytes.**

## 3. The Execution Flow
The interaction during execution follows a specific pipeline that involves the CPU and OS scheduling.

| Phase | Action | OS/Hardware Interaction |
| :--- | :--- | :--- |
| **Compilation** | Source code is turned into **Bytecode** (`.pyc`). | File System (I/O) access. |
| **Interpretation** | The **Virtual Machine (PVM)** loops through bytecode. | CPU registers are used for stack operations. |
| **Execution** | Bytecode is mapped to C functions. | The OS schedules the thread on a physical CPU core. |
| **GIL** | The **Global Interpreter Lock** ensures only one thread runs bytecode at a time. | Prevents multi-core CPU utilization for standard Python threads. |

## 4. Memory Deallocation (Garbage Collection)
Python uses two primary strategies to return memory to the heap (and eventually the OS):

### Reference Counting
The moment an object's reference count hits zero (e.g., you `del x` or a function ends), Python immediately deallocates the memory block. This is highly efficient for most tasks.

### Generational Garbage Collection (GC)
To handle **circular references** (Object A points to B, and B points to A), Python uses a generational GC.
* It periodically scans objects.
* Objects that survive scans are moved to "older" generations (0 → 1 → 2).
* The OS only sees memory being "freed" when Python releases an entire **Arena** back to the system.

## 5. Summary of Interactions
* **Variable Assignment:** Python's Memory Manager finds a free **Block** in its Private Heap; if full, it requests a new **Arena** from the OS.
* **Execution:** The PVM executes bytecode; the OS manages the process state and CPU time.
* **Cleanup:** Reference counting clears the block; if a whole memory page becomes empty, Python may release it back to the OS.
