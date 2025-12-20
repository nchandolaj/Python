'''
Python variables
'''

# Variable and Memory Address
print("\n*** Variable and Memory Address ***")
sample = 32
sample_address = id(sample)
print(f"\n{sample=}, {sample_address=}")

# Local and Global Variables
print("\n*** Local and Global Variables ***")

print("\nLocal variables can only be used in a method or classes that your specify.")
print("\nGlobal variables can be used in any part of the program without issue.")
