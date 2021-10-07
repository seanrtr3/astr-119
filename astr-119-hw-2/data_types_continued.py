#string

s = 'I am a string.'
print(type(s))				#prints string (str)

#Boolean - logic variables
#It's either true or false, nothing in between (good for conditions)

yes = True					#Boolean value of 'True', which is a protected name
print(type(yes))			#gives bool

no = False 					#Boolean value of 'False'
print(type(no))

# lists - ordered and changeable

alpha_list = ['a', 'b', 'c']		#list initialization (uses square brackets[])
print(type(alpha_list))				#will say list
print(type(alpha_list[0]))			#will say string (elements in the list are strings)
alpha_list.append('d')				#adds the string 'd' to the end of the list
print(alpha_list)					#prints the list

# tuple - ordered and unchangeable

alpha_tuple = ('a', 'b', 'c')		#tuple initialization (uses parenthesis())
print(type(alpha_tuple))			#will say tuple

try:								#will attempt the next line
	alpha_tuple[2] = 'd'			#won't work because TypeError
except TypeError:					#try the above except when we get a TypeError
	print("We can't add elements to tuples!")
print(alpha_tuple)