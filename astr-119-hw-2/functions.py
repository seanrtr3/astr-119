import numpy as np
import sys     #allows us to use a command line argument in the command prompt
			   #		- command line arguments are what you can pass when running a program in the command prompt
			   #gives access to operating system outside of the script
			   #lets programs update on the fly when running programs through the command prompt


#define a function that returns a value
def expo(x):
	return np.exp(x)	#return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):			# for whatever n is, it loops the function i times, 
								#and everytime it loops, it prints the expo function
		print(expo(float(i)))	# call the expo function and prints a float i, where i is an element of a range of n numbers
#what the function does above is print the e^x function up to n times starting at i = 0 to i = n - 1, or, [0, n -1]

#define a main function
def main():
	n = 10	#provide a default function for n

	# check if there is a command line argument provided
	# command line arguments are the entries after python when running a python program through the command prompt
	# there is at least one in the command line argument because the name of the program is the first entry

	if(len(sys.argv) > 1):		# argv - variable arguments
								# if there is more than one in the command line argument
		n = int(sys.argv[1]) 	# index starts at 0, so sys.argv[1] refers to the second entry in the command line argument
								# n gives an integer value of what is entered in the command line argument

	show_expo(n)		#calls the show_expo subroutine


#run the main function
if __name__ == '__main__':		#still unsure what this does
	main()