import numpy as np #np is convention for numpy


def main():		# creates a function named main():
	i = 0 		# i is a string, declared with a number 0, initialized as variable i
	n = 10 
	x = 119.0 # floating point numbers are declared with a . (a decimal number)
			  # floats sets a precision (sig figs)

			  #python loops over an integer n, starting with 0 and ending with n - 1

	# numpy can be used to declare arrays quickly
	# an array is a collection of numbers that are indexed by another number

	y = np.zeros(n, dtype = float) # creates an array with n = 10 zeros, and each element is a floating point number

	#for loops can be used to iterate with a variable
	# i.e. iterate over each element in the array y

	#the below for loop changes the array of zeros to an array that follows the formula below
	for i in range(n):  # i in range [0, n-1] -> (0-9)
		y[i] = 2.0 * float(i) + 1.0 # set y = 2 * i + 1 as floats

		# since y is an array of n = 10 zeros
		# the for loop will start with the ith element in y (which is 0 for the first element)
		# then makes the number 1 according to the above formula
		# then loops again to the second element, but i = 1 (from above)
		# so the second element in y is now 3
		# and so on and so forth until the range(n), where n = 10 defined above 

	# we can iterate through a variable array
	for y_element in y:		#this creates a loop that goes through every element in n
		print(y_element)	#this prints each element

	print(y)	# this prints the whole array at once



#execute the main function
if __name__ == "__main__":
	main()