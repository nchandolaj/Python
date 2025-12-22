'''
Python data types

Common Data Types:
1. Strings
2. Integers
3. Floating-Point Numbers
4. Boolean
'''



'''
1. Strings
'''

stmt = "This is a sentence"

print(stmt)
print("Statement: " + stmt)
print("Statement: " + stmt)

multi_line = """This is a sentence
with multiple lines"""
print(multi_line)

# Access characters in a string
print ("1st Character = ", stmt[0])
print ("Last Character = ", stmt[-1])

print ("Sliced Characters = ", stmt[5:16])

# String Formatting

## Concatenate
stmt = "Today is " + " a raing day!"
print(stmt)

## Multiply
stmt = "Today " * 3
print(stmt)

## Length
stmt = "Today is Monday"
print(len(stmt))

## Find
stmt = "Tomorrow is Tuesday"
sample = stmt.find('is')
print(sample)

## Lower and Upper Case
stmt = "Hear me ROAR!!!"
print(stmt.lower())
print(stmt.upper())

## Title
print(stmt.title())

'''
2. Integers
'''

x = 5
y = 14
print(x)
print(y)

'''
3. Floating-Point Numbers
'''

x = 3.12452
y = 33.256712
print(x)
print(y)

# Floating-point data types are also used 
# to represent complex and exponential numbers.
x = float.hex(16.234)
print(x)

'''
4. Boolean
'''

A = 12
B = 34
print(A > B)