import math

# 1 - Acess the math module and print the value of pi
print("--------------------")
print('Acess the math module and print the value of pi')
print(math.pi)
print(f'{math.pi:.2f}')

# 2 - Acess the number of Euler and print it
print("--------------------")
print('Aceess the number of Euler and print it')
print(math.e)
print(f'{math.e:.2f}')

# 3 - Round a number
num1 = 10.4
print("--------------------")
print('Round a number')
print(math.floor(num1))
print(math.ceil(num1))

# 4 - Calculate the factorial of a number
print("--------------------")
print('Calculate the factorial of a number')
num2 = int(input('Enter a number for the factorial: '))
print(math.factorial(num2))

# 5 - Calculate the potence of a number
print("--------------------")
print('Calculate the potence of a number')
num3 = int(input('Enter a number: '))
potence = int(input('Enter the potence: '))
print(math.pow(num3, potence))

# 6 - Calculate the square root of a number
print("--------------------")
print('Calculate the square root of a number')
num4 = int(input('Enter a number: '))
print(math.sqrt(num4))

# 7 - Calculate the GCD of two numbers
print("--------------------")
print('Calculate the GCD of two numbers')
num5 = int(input('Enter a number: '))
num6 = int(input('Enter another number: '))
print(math.gcd(num5, num6))

# 8 - Calculate the logarithm of a number
print("--------------------")
print('Calculate the logarithm of a number')
num7 = int(input('Enter a number: '))
print(math.log(num7))