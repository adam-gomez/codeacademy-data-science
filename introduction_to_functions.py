def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
  
# call sing_song() below:
sing_song()
sing_song()

def loading_screen():
  print("This page is loading...")

loading_screen()

def about_this_computer():
  print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()

def mult_two_add_three(number):
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(1)
mult_two_add_three(5)
mult_two_add_three(-1)
mult_two_add_three(0)

def mult_x_add_y(number, x, y):
  print(number*x + y)

mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)

# Define create_spreadsheet():
def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called "+title + " with " + str(row_count) + " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Applications", 10)

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age (2049, 1993)
dads_age = calculate_age(2049, 1953)

print(f"I am {my_age} years old and my dad is {dads_age} years old")

def get_boundaries(target, margin):
  low_limit = target-margin
  high_limit = margin+target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age
  
print(current_year)
print(calculate_age(1970))

def repeat_stuff(stuff, num_repeats = 10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "

song = repeat_stuff(lyrics)

print(song)