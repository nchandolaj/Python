'''
Python basics
'''

# User Prompts
print("\n*** User Prompts: Input() ***")

#county = input("Which county do you live in?")
county = 'Santa Clara'

print(f"{county} is a beautiful county!")

# String Literals
print("\n*** String Literals ***")

prompt = "Once upton a time,"
prompt += " there was a programmer..."
prompt += "\n His name was Guido van Rossum."
prompt += " He developed a software language."
prompt += "\n Do you know the name of the software language?"
#software_language = input(prompt)
software_language = 'Python'

print("Guido van Rossum developed " + software_language + "!")

# Comments
print("\n*** Comments ***")

print("\n# This is a comment with a single line.\n")

print("''' \n This is a comment \n with two lines. \n'''")

# Operators
print("\n*** Operators: +, -, *, /, %, // ***")

print(f"Addition = + \t\t{(4 + 5) = }")
print(f"Substraction = - \t{(4 - 5) = }")
print(f"Multiplication = * \t{(4 * 5) = }")
print(f"Division = / \t\t{(4 / 5) = }")
print(f"Modulus = %  \t\t{(8 % 5) = } \tModulus is the remainder of a division operations.")
print(f"Floor Division = // \t{(9 // 4) = } \tFloor Division is the nearest integer of the quotient.") 

# Bitwise Operators
print("\n*** Bitwise Operators: AND (&), OR (|), XOR (^), NOT (~) ***")

# Augmented Assignment Operators
print("\n*** Augmented Assignment Operators: +=, -=, *=, /=, %=, //=, **=, &=, |= ***\n")




