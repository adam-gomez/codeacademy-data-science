my_name = "Adam"
print("Hello and welcome " + my_name + "!")

# Write a comment describing the first program you want to write: 
# A program that would make running Pathfinder 2e games a bit easier, specifically in quickly determining target DC and rule interactions. 

# Print the distinguished greeting “Hello world!”
print('Hello world!')

# Print your name using the print() command.
print("Adam")

# If your print statement uses double-quotes ", change them to single-quotes '. If it uses single-quotes ', change them to double-quotes ".
print('Adam')

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = 'Tofu salad'

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = 'Morningstar Buffalo Chicken Burger'
# Printing out dinner
print("Dinner:")
print(meal)

# Define the release and runtime integer variables below:
release_year = 2012
runtime = 123

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 9.2

print(25 * 68 + 13 / 28)

quilt_width = 8
quilt_length = 12

print(quilt_width * quilt_length)

quilt_length = 8

print(quilt_width * quilt_length)

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6**4)

my_team = 27 % 4
print(my_team)

left = 26 % 4
right = 28 % 4

for i in range(29):
  print(f'Person {i} is on team {i % 4}.')

team_snake = []
team_mouse = []
team_tiger = []
team_eagle = []

for i in range(29):
  if i % 4 == 0:
    team_snake.append(i)
  elif i % 4 == 1:
    team_mouse.append(i)
  elif i % 4 == 2:
    team_tiger.append(i)
  elif i % 4 == 3:
    team_eagle.append(i)

print('Team Snake is made of the following players: ', team_snake)
print('Team Mouse is made of the following players: ', team_mouse)
print('Team Tiger is made of the following players: ', team_tiger)
print('Team Eagle is made of the following players: ', team_eagle)

my_number = 27

if my_number in team_snake:
  print('I am on Team Snake. HISS!')
elif my_number in team_mouse:
  print('I am on Team Mouse. SQUEAK!')
elif my_number in team_tiger:
  print('I am on Team Tiger. ROAR!')
elif my_number in team_eagle:
  print('I am on Team Eagle. CAWCAW!')

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

print(message)

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater + fun_books

print("The total price is", total_price)

# Assign the string here
to_you = '''
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
'''

print(to_you)

my_age = 36
half_my_age = 36/2
greeting = "Hail and well met traveler!"
name = "Adam"
greeting_with_name = greeting + " My name is " + name + "."