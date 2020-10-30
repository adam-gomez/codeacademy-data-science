zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])

print(zodiac_elements['fire'])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements['energy'] = 'Not a Zodiac element'

print(zodiac_elements["energy"])

# USING TRY/EXCEPT TO GET A KEY

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print('Unknown Caffeine Level')

'''
Dictionaries have a .get() method to search for a value instead of the my_dict[key]
notation we have been using. If the key you are trying to .get() does not exist, 
it will return None by default

You can also specify a value to return if the key doesn’t exist.
'''

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder', 100000)

print(tc_id)

stack_id = user_ids.get('superStackSmash', 100000)

print(stack_id)

# DELETE A KEY USING .pop()
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop('stamina grains', 0)

health_points += available_items.pop('power stew', 0)

health_points += available_items.pop('mystic bread', 0)

print(available_items, '\n', health_points)

# USING list() to obtain keys
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

list(test_scores)

# USING .keys()
'''
Dictionaries also have a .keys() method that returns a dict_keys object. 
A dict_keys object is a view object, which provides a look at the current state 
of the dicitonary, without the user being able to modify anything. 
The dict_keys object returned by .keys() is a set of the keys in the dictionary. 
You cannot add or remove elements from a dict_keys object, but it can be used 
in the place of a list for iteration
'''
for student in test_scores.keys():
  print(student)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)

print(lessons)

# USING .values() to obtain values
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for value in num_exercises.values():
  total_exercises += value

print(total_exercises)

# Get both keys and values using .items() -- returns a tuple (key, value)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for job, percent in pct_women_in_occupation.items():
  print(f"Women make up {percent} percent of {job}s.")

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread['past'] = tarot.pop(13)
spread['present'] = tarot.pop(22)
spread['future'] = tarot.pop(10)

for key, value in spread.items():
  print(f"Your {key} is the {value} card.")