# data structure in python

# list
my_list = [1,2,5.98, "Hello", True] # list can  contain different datatypes

#accessing list elements
print(my_list[0]) # accessing the first element of the list
print(my_list[3]) # accessing the fourth element of the list

# adding elements to the list
my_list.append("WHAT") # adding an element to the end of the list
my_list.insert(2, "INSERTED") # adding an element at a specific index
print(my_list)

# removing elements from the list
my_list.remove(5.98) # removing an element by value
my_list.pop(5)# removing an element by index
print(my_list)

# loop through the list
for item in my_list:
    print(item)


# tuple : tuple can also contain different datatypes but it is immutable(cannot be changed after creation)
gps_coordinates = (27.7172, 85.3240) # tuple with two float values
print(gps_coordinates[0]) # accessing the first element of the tuple

# dictionary : dictionary is a collection of key-value pairs
intro = {
    "name": "Bijena",
    "age": 23,
    "city": "Pokhara"
}
print(intro["name"]) # accessing the value of the key "name"
# adding a new key-value pair to the dictionary
intro["profession"] = "Student"
print(intro)
print(intro.get("age")) # accessing the value of the key "age" using get method
# remove element from the dictionary
del intro["city"] # removing the key "city" and its value
print(intro)
intro.pop("age") # removing the key "age" and its value using pop method
print(intro)

# loop through the dictionary
for key in intro:
    print(key, ":", intro[key])

for key, value in intro.items():
    print(key, ":", value)

print(intro.keys()) # printing all the keys of the dictionary
print(intro.values()) # printing all the values of the dictionary
print(intro.items()) # printing all the key-value pairs of the dictionary

# get method
print(intro.get("name")) # accessing the value of the key "name" using get method
intro.update({"name": "Jenns", "age": 24}) # updating the value of the key "name" and adding a new key-value pair "age"
print(intro)
intro.clear() # clearing all the key-value pairs from the dictionary
print(intro)



# SET : set is a collection of unique elements i.e. it does not allow duplicate values
my_set = {1, 2, 3, 4, 5}
print(my_set) # printing the set
my_set.add(6) # adding an element to the set
print(my_set)
my_set.remove(3) # removing an element from the set
print(my_set)

listdup = [1, 2, 2, 3, 4, 4, 5]
print(listdup)
setfromlist = set(listdup) # converting a list with duplicate values to a set to get unique values
print(setfromlist)

# list , dictionary  ,tuple set

#duplicate values in list. eg - shopping list 

#indexing in list and tuple

#key value pair in dictionary , example - student data in college 

#immutable in tuple , example - gps coordinates of a place

#unique value