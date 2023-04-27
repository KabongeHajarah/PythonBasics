          # lists
# unpacking-list
mylist=[1,2,3,5,6,8]
first,second,third,*rest=mylist
# print(first)
# print(second)
# print(third)
print(*rest)

# Indexing
Vegetables= ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(len(Vegetables[-2]))

print(Vegetables[0:3])

Vegetables.append('orange')
print(Vegetables)

# checking if an item exists
print("orange"in Vegetables)

# inserting an intem in a list
Vegetables.insert(1,"Bella")
print(Vegetables)

# removing items
Vegetables.remove("Bella")
print(Vegetables)
 
#  pop , removes the item on the last index if not specified
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']


# del ---> it can be use to remove items in a range or a specified index
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
# del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

#Joining lists
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)

# count method--> Returns the number of time an item appears in a list
ages=[1,2,3,1,2,3,4,4,3,2,2,7]
print(ages.count(2))
# index of an item
print(ages.index(7))
# reversing
ages.reverse()
print(ages)

# sorting
ages.sort()  # sorts in ascending order
print(ages)

ages.sort(reverse=True)  # sorts in descending order
print(ages)

        # EXERCISES
# Get the first item, the middle item and the last item of the list
names=["bella","shat","rayan","juliet","florence"]
print(names[0],names[2],names[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["BELA",20,162,'Single','lugonjo']
print(mixed_data_types)
print(len(mixed_data_types))
mixed_data_types.insert(0,'RAYAN')
print(mixed_data_types)

mixed_data_types.extend('#')
print(mixed_data_types)

print("RAYAN" in mixed_data_types)

print(mixed_data_types[0:3])

# join these lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
newlist=front_end + back_end
print(newlist)
newlist.insert(5,"Python")
print(newlist)


# he following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(f"maximum age:{max(ages)}, minimum age:{ min(ages)} ")
# Add the min age and the max age again to the list
both=(max(ages) + min(ages) )
print(both)
ages.append(both)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
listLength = len(ages)
if listLength % 2 == 0:
    median_age = (ages[listLength // 2 - 1] + ages[listLength// 2]) / 2
else:
    median_age = ages[listLength // 2]
    print(median_age)
# Find the average age (sum of all items divided by their number )
averageNumbers=(sum(ages)/len(ages))
print(averageNumbers)
# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(age_range)


# Compare the value of (min - average) and (max - average), use abs() method
#    abs()--->  is a built-in Python function that returns the absolute value of a number
diff1 = abs(min(ages )- averageNumbers)
diff2 = abs(max(ages) - averageNumbers)
print(f"The comparison is {diff1} and {diff2}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan']
length=len(countries)

middle_index = length // 2
middle_country = countries[middle_index]

print(middle_country)


# Divide the countries list into two equal lists if it is even if not one more country for the first half.
n = len(countries)
if n % 2 == 0:
    half1 = countries[:n//2]
    half2 = countries[n//2:]
else:
    half1 = countries[:n//2 + 1]
    half2 = countries[n//2 + 1:]

print(half1)
print(half2)

new_countries= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 
one,two,three,*rest=new_countries
scanded=one,two,three,*rest
print(scanded)
print(*rest)
# Unpack the first three countries and the rest as scandic countries.


# TUPLES
# Create an empty tuple
names=()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=("bella","shaturah","rayan","juliet")
brothers=("mike","meddy")
print(type(names))
print()
# Join brothers and sisters tuples and assign it to siblings
siblings= sisters + brothers
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family=("florence","allan")
family_members=siblings + family
print(family_members)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables=('cabbage','carrot')
animalProducts=('gee','milk','meat')
food_stuff_tp=fruits+vegetables+animalProducts
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp_list=list(food_stuff_tp)
print(food_stuff_tp_list)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp_list) // 2
middle_items_tp = food_stuff_tp[middle_index-1:middle_index+1] # tuple
middle_items_lt = food_stuff_tp_list[middle_index-1:middle_index+1]
print(middle_items_lt)
print(middle_items_tp)

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp_list[:3])
print(food_stuff_tp_list[-3:])


# Delete the food_staff_tp tuple completely

del (food_stuff_tp)
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in  nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in  nordic_countries)

# Dictionaries

# Create an empty dictionary called dog

dog=dict()

# Add name, color, breed, legs, age to the dog dictionary
dog={
'name':"BRUNO",
'color':"Red",
'breed':"maltese",
'legs':4,
'age':8
}
print(dog)
print(type(dog))
# Create a student dictionary and add first_name, last_name,
#  gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
   'first_name' :'Kabonge',
   'last_name' :'Bella',
   'gender' :'female',
    'age' :21,
    'marital_status' :'single',
    'skills':['python','javascript','aviation','first aid'],
    'country':'uganda',
    'city':'entebbe',
    'address':'lugonjo'
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list


print(student.get('skills'))
print(type(student.get('skills')))


# Modify the skills values by adding one or two skills
new_skills=student['skills'].append('Communication')
print(student.get('skills'))
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
del student["skills"]
print(student)
# Delete one of the dictionaries
del dog





