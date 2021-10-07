x = [0.0, 3.0, 5.0, 2.5, 3.7]		#an array is a list of numbers
print(type(x))

#removing the third element
x.pop(2)							#it pops off the (index)
print(x)

#removes the 2.5 element
x.remove(2.5)
print(x)

#add an element to the end
x.append(1.2)
print(x)

#get a copy
y = x.copy()					#produces a 'deep' copy of x in memory (so it doesn't change the value of the variable)
print(y)

#how many elements are 0.0
print(y.count(0.0))

#print the index with value 3.7
print(y.index(3.7))

#sort the list (increasing numerical order)
y[0] = 5.9			#adds 5.9 in the beginning of the list
print(y)
y.sort()
print(y)

#reverse sort (decreasing numerical order)
y.reverse()
print(y)

#remove all elements
y.clear()
print(y)