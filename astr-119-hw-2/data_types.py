import numpy as np 

#integers

i = 10			#integer (number without a decimal point)
print(type(i))	#prints out the data type of (i)

a_i = np.zeros(i, dtype = int)		#declares an array of integers
print(type(a_i))					#returns ndarray (array made with numpy with n dimensions)
print(type(a_i[0]))					#will return int64 (integer with 64 bit precision) 
									#the first element in the array [index starts at 0])

#floats

x = 119.0 			#floating point number (has precision)
print(type(x))		#same as above

y = 1.19e2			#float 119 in scientific notation (119 * 10^2)
print(type(y))		#prints data type

z = np.zeros(i, dtype = np.float32)		#declares an array of floats, specified with a 32 bit precision
print(type(z))
print(type(z[0]))					#same as above