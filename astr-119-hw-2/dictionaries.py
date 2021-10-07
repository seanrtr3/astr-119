#Dictionaries associate different data types with each other
#like looking up a word in the dictionary

#define a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {							#dictionaries declared with {}
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10					#last elements does not have a comma
}
print(type(example_dict))		#will say dict

#get a value via key
course = example_dict["class"]			#will go through each element in the dictionary and search up the key, and assigns the dictionary the value
print(course)

#change a value via key
example_dict["awesomeness"] += 1 	#increase awesomeness by 1
print(example_dict)

#print the dictionary
for x in example_dict.keys():		#makes a list of the keys, and x is every element in the key
	print(x, example_dict[x])		#prints each element and the value