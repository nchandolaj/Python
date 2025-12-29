'''
Iterations
'''
print("*** Iterations using 'for' loops ***")
print("\nfor i in range (11):")
for i in range (5):
  print (f"  {i=}")

print("\nfor i in range (2, 5):")
for i in range (2, 5):
  print (f"  {i=}")

print("\nfor i in range (2, 9, 3):")
for i in range (2, 9, 3):
  print (f"  {i=}")  


print("\n*** Iterations using 'while' loops ***")
print("\nwhile (i < n):")
n = 15
i = 2
while (i < n):
  if i in [3, 9, 11]:
    print(f'      continue at {i=}')
    i += 1
    continue
  print (f"  {i=} of {n=}")
  if i == 13:
    print(f'      break at {i=}')
    break
  i += 1