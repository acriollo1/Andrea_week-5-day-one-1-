#Andrea Criollo
##############################################################################################################
# what are tuples?
# exactly the same thing as an array only it is immutable, once you define the tuple,
#you cannot change it or modify it
#you define a tuple with () instead of [] like you would in lists
#once you define it, you cannot change it
#example
coordinates = (4, 5)
# get the first element in the above tuple
print(coordinates[0])
# lets make this a multidimensional array
coordindates2 = [(4, 5), (6, 7), (80, 34)]
#get the second element of the second item in coordinates2
print(coordindates2[1][1])
# we use parentheses not [] in tuples
my_tuple1 = (1, 2, 3, 4)
print(my_tuple1[1])
# get the second item in the tuple1 above
my_tuple = (1, 2, (10, 20), 4)

# get the second item in the 3rd item above
#hint multidimensional array thinking
print(my_tuple[2][1])
# place these numbers in separate variables from the tuple below
t = (1, 2, 3)
x, y, z = t
print(x,y, z)
#get me the length of the above tuple --- there are two ways of doing this... len(), count()...  use count if you want to get how many times an item appears in a tuple
print(len(my_tuple))
# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(my_tuple.count(2))
# Convert the following tuple to a list, and store it in a variable called my_list.

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
my_list = list(my_tuple)
print(my_list)
#Extract the elements of the following tuple into four variables: a, b, c, d

my_tuple = (1, 2, 3, 4)
a, b, c, d = my_tuple
print(a, b, c, d)
#################################################sets######################################################
#sets are simmilar to tuples. th eonly difference is that they will not contain or print out any repeated elements.
my_firstSet = set((1,2,2,2,2,3,4,5))
print(my_firstSet)
print(2 in my_firstSet)#true
print(6 in my_firstSet)#false
# Join the following sets into one, called my_set_3:

set1 = {1, 2, "three", "four"}

set2 = {"three", 4, 5}
s3 = set1.union(set2)
print(s3)
s3.add(8)
print(s3)
# Remove a random item from the following set, using set methods.

raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle.remove("Rachel")
print(raffle)
raffle.remove("Phoebe")
print(raffle)

# Add the name Gunther to the following set, using set methods:

raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle.add("Tom")
print(raffle)
#################################################booleans######################################################
# booleans
# a boolean can only have 2 values -- true or False
 #my_bool = 5 > 4
#print(my_bool)

# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to

# you can also construct booleans to see if values ar in a variable or not found
my_list = [1,2,3,4,5,6,7]
my_bool = 5 in my_list#true
my_bool = 5 not in my_list#false

# so we can see if we can make logical decisions if something is true or not
var1 = True
var2 = False
print(type(var1))
print(var1)

list = [1,2,3,4,5,6]
control = 5 in list
print(type(control))
print(control)

# Booleans Practice

# Make a comparison that returns a boolean and store the result (True/False) in a variable called test
test = 5==4
print(test)
# Check if 17834/34 is greater than 87*56 and print the boolean result to the screen using print()
result = 17834/34 > 87*56
print(result)
# Check if the square root of 25 is equal to 5 and display the result (boolean) on the screen using print
import math 
print(math.sqrt(25)==5)


#############################################next week ################################################
#dictionaries and  sets

# dictionaries
# another data structure that stores data that can be unstructured
# employee = {'first_name': 'steven',
#             'last_name': 'pretti',
#              'weight': 37.2,
#               'size': 5.77
#              'height:' 6}
# print(employee['weight'])

#challenge 1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.

#challenge 2:
# Use print to returns the second item of the list called points2, inside the following dictionary.

# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
my_dict = {
    "values_1": {
        "v1": 3,
        "v2": 6
    },
    "points": {
        "points1": 9,
        "points2": [10, 300, 15]
    }
}
# print(my_dict[]) #Use dictionary indices to extract the second item of points2

#challenge 2
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:

# name: Karen

# surname: Jurgens

# age: 36

# occupation: Editor

# country: Colombia

# to do this, you should not change the line of code already written, but update the values using dictionary methods.

# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}

#################################share with instructor when finished#############################