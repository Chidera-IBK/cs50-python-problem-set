expression = input("Expression: ")

ex = expression.split()

x = int(ex[0])
z = int(ex[2])

y = ex[1]

if y == "+":
    print(f'{x + z :.1f}')
elif y == "-":
    print(f'{x -  z :.1f}')
elif y == "/":
    print(f'{x / z :.1f}')
elif y == "*":
    print(f'{x * z :.1f}')
else:
    print("Enter a valid operation")
