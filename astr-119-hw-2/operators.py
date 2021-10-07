x = 9
y = 3

#arithmetic operators
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)		#Modulus - gives the remainder after division
print(x ** y)		#Exponentiation
x = 9.191823
print('Floor divide: ', x // y)		#gives only the whole number increments of a division operation (does not give the remainder or the fractional part)
print('Modulus: ', x % y)			#prints a list starting with Modulus, then the operation

#assignment operators
x = 9
x += 3  		#sets x as x = x + 3 = 12
print(x)
x = 9
x -=3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x **= 3
print(x)

#comparison operators
#Boolean operators - gives true or false value
x = 9
y = 3
print('Does x == y? ', x == y)		#Is x equal to y?
print('Does x != y? ', x != y)		#Is x not equal to y?
print('Is x > y? ', x > y)
print('Is x < y? ', x < y)
print('Is x >= y? ', x >= y)		#Is x greater than or equal to y?
print('Is x <= y? ', x <= y)