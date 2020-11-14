# Reads a .txt file as a single string and stores it to a variable
with open('welcome.txt') as text_file:
  text_data = text_file.read()

print(text_data)

# .readlines() creates a list consisting of each 'line' in the document
# a for loop can iterate through the list to further separate the elements
# Note: The entire lines_doc list is collectively stored in memory, so for large documents,
# this could slow things down
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# .readline() (singular) will return a single line in the document at a time. As it is subsquently
# called, it will move to the next line until it has exhausted the document and returns ""
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()

print(first_line)

# Writing a file
'''
By adding the argument 'w' to our open() function, we indicate to open the file in write-mode
instead of the default 'r' read-mode
If the file name doesn't exist, the file will be created
If the file name exists, the file will be completely overwritten
'''
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('Dave Matthews Band')

# Appending a file
''' 
Adding the argument 'a' opens the file in append-mode. Anything added will be appended as a new 
line in the selected file.
'''
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')

with open('cool_dogs.txt') as cool_dogs_file:
  print(cool_dogs_file.read())

# What's the deal with 'with'
'''
with allows us to use the open() function without explicitly having to call to close() the file later.
We could still just use open() without 'with', but we would need to be sure to use the close() 
function or the file may remain open indefinitely.
'''
#close_this_file = open('fun_file.txt')
#setup = close_this_file.readline()
#punchline = close_this_file.readline()
#print(setup, punchline)

# VS

with open('fun_file.txt') as close_this_file: 
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup, punchline)

# Printing the contents of a .csv file using open() and .read()

with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())

# Using the csv library to create a dictionary from the .csv file

import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact']) # prints the value for the 'Cool Fact' keys

# Using the delimiter parameter to handle a .csv file that uses '@' instead of a comma
import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]

# Writing a .csv file using the csv library
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for line in access_log:
    log_writer.writerow(line)

# Using the json library to read a json file
import json

with open('message.json') as message_json:
  message = json.load(message_json)

print(message['text'])

# Using the json library to write a json file from a dictionary
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)