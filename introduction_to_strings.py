favorite_word = 'Remi'

print(favorite_word)

my_name = 'Adam'

first_initial = my_name[0]

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]

temp_password = last_name[2:6]

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)

print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)

print(temp_password)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

final_word = company_motto[-4:]

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]

password = "theycallme\"crazy\"91"

def get_length(string):
  length = 0
  for letter in string:
    length += 1
  return length

def letter_check(word, letter):
  return letter in word

def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common_letter_list = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common_letter_list):
      common_letter_list.append(letter)
  return common_letter_list

def username_generator(first_name, last_name):
  return first_name[:3] + last_name[:4]

def password_generator(username):
  return username[-1] + username[:-1]