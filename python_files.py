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
