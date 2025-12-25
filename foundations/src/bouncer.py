'''
Bouncer: Control Flow in Python

The Bouncer Script: A program that asks for user age.
If age < 18: Print "Too young."
If age >= 18 and < 21: Print "Entry allowed, no wristband."
If age >= 21: Print "Entry allowed, take a wristband."
'''

age = int(input("Whats your age?"))

if age < 18:
  print("Too young.") 
elif age <21:
  print("Entry allowed,  no wristband.")
else:
  print("Entry allowed, take a wristband.")