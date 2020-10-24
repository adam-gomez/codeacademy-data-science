example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "Yes"

statement_one = True

statement_two = False

statement_three = True

my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))

def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"
  
# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))

user_name = "angela_catlady_87"

print(dave_check(user_name))

def greater_than(x, y):
  if x > y:
    return x
  elif y > x:
    return y
  else:
    return "These numbers are the same"

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

print(graduation_reqs(120))

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

print(statement_one, statement_two)

def graduation_reqs(gpa, credits):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

print(statement_one, statement_two)

def graduation_mailer(gpa, credits):
  return gpa >= 2.0 or credits >= 120

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

print(statement_one, statement_two)

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  else:
    return "F"

def raises_value_error():
  try:
    raise ValueError
  except ValueError:
    print ("You raised a ValueError!")

raises_value_error()

def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >=3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."