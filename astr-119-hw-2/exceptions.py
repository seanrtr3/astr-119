#python exeptions let you deal with unexpected results
#this is so that we don't get an error code if we can foresee the error

try:
	print(a) 	#a is NOT DEFINED
except:
	print('a is not defined!')

#specific errors to help with cases
try:
	print(a)			#this will fail again because a is not defined
except NameError:		#NameError is what the error actually is
	print('a is still not defined')
except:
	print('Something else went wrong')

#this will break our program
print(a)