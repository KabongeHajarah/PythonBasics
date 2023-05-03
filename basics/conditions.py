# Get user input using input(“Enter your age: ”). If user is 18 or older,
#  give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
 

user_input=input(("Enter your age: "))
change_Age_to_Int=int(user_input)
if change_Age_to_Int >=18:
    print(" You are old enough to drive")
else:
 duration= 18 -change_Age_to_Int
 
 print(f"You need more {duration} years to learn to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input.
#  You can use a nested condition to print 'year' for 1 year difference in age,
#  'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
your_age=input(("Enter your age: "))
change_Age_to_Int=int(user_input)
my_age=21
duration_age= abs(change_Age_to_Int - my_age)
if change_Age_to_Int >my_age:
    if duration_age ==1:
       print(f"We have {duration_age} year difference ")
    else:
       print(f" You are {duration_age} year older than me.")
elif my_age==change_Age_to_Int:
     print('we have no age gap between us')
else:
   if duration_age==1:
      print(f"I am {duration_age} year older than you.")
   else:
      print(f"I am {duration_age} years older than you.")
      

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
def assign_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


scores = [90, 75, 63, 53, 34]
for score in scores:
    grade = assign_grade(score)
    print(f"Score: {score} Grade: {grade}")





# Check if the season is Autumn, Winter, Spring or Summer.
#  If the user input is: September, October or November, the season is Autumn.
#  December, January or February, the season is Winter. March, April or May, 
# the season is Spring June, July or August, the season is Summer
def get_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid input'

month = input("Enter a month: ")
season = get_season(month)
print(f"The season for {month} is {season}")





# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list 
# add the fruit to the list and print the modified list.
#  If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input('Enter fruit: ' )

if(fruit not in fruits):
   fruits.append(fruit)
   print(fruits)
else:
    print("That fruit already exist in the list")

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
#  * Check if the person dictionary has skills key, 
# if so print out the middle skill in the skills list.
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    skills_list=person['skills']
    if len(skills_list)%2==0:
        middle_skill_index=len(skills_list)//2-1
    else:
        middle_skill_index=len(skills_list)//2
        middle_skill = skills_list[middle_skill_index]
        print(f"The middle skill in the skills list is: {middle_skill}")
else:
    print("The person dictionary does not have a skills key")
        

#  * Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill
#  and print out the result.

if 'skills' in person:
  if 'Python' in person['skills']:
      print('Python exists')
  else:
      print('Not there')
else:
    print('Skills is not there')
      

#  * If a person skills has only JavaScript and React, 
# print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#  else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif set(skills) == {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print('No skills found')
 





#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if 'is_marred' in person:
    if ( person['is_marred'] and  (person['country']=='Finland')):
         print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

