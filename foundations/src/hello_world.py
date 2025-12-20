# The customary hello world!
print("Hello World!")

# Kick & Giggles: Creative ways of saying Hello World!

# Get the ASCII characters
print("\n*** Get the ASCII characters ***\n")
hello_world = "Hello World!"
print(f"{hello_world=}")
hello_world_char = []
hello_world_ascii = []
for char in hello_world:
  print(f"{ascii(char)=}, {ord(char)=}")
  hello_world_char.append(ascii(char))
  hello_world_ascii.append(ascii(char))

print(f"{hello_world_ascii=}")

# Using List Comprehension
print("\n*** Using List Comprehension ***\n")
print(f"{hello_world=}")
hello_world_char = [ascii(char) for char in hello_world]
hello_world_ascii = [ord(char) for char in hello_world]
print(f"{hello_world_char=}")
print(f"{hello_world_ascii=}")
print("".join(chr(i) for i in hello_world_ascii))

# Exception 
print("\n*** Using an Exception ***\n")
try:
  raise Exception("Hello World!")
except Exception as e:
  print(e)

# Function and Environment Variable
print("\n*** Using Function and Environment Variable ***\n")

import os

def hello_world(message):
  print(message)

os.environ['ENV_HELLO_WORLD'] = 'Hello World!'

msg = os.getenv('ENV_HELLO_WORLD', 'Default Hello, World! message')
hello_world(msg)

msg = os.getenv('ENVIRONMENT_HELLO_WORLD', 'Default Hello, World! message')
hello_world(msg)

# logging Module
print("\n*** Using the logging Module ***\n")

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.info("Hello, World!")