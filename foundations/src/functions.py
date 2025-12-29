'''
Python Functions
'''

# First functions
def calculate_area(length, width):
  return length * width

length, width = 10, 30
area = calculate_area(length, width)
print(f"For {length=} and {width=}, {area=}")

# Second function
def celsius_to_fahrenheit(c):
  return (c * 9/5) + 32

c = 5
print (f"Celsius {c} is that same as {celsius_to_fahrenheit(c)} Fahrenheit.")