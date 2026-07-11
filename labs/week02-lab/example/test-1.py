print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (¦Ð * r0…5)")
print("   - Calculate circumference (2 * ¦Ð * r)")
print("   - Use 3.14159 for ¦Ð")
print()
# input
r = input("Radius: ")
r = float(r)
#process
area = 3.14159 * r ** 2
circumference = 2 * 3.14159
#output
print(area)
print(circumference)