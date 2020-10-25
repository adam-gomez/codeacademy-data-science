names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append('Priscilla')
insurance_costs.append(8320.0)

medical_records = list(zip(names, insurance_costs))

#print(medical_records) 

num_medical_records = len(medical_records)

print(f'There are {num_medical_records} medical records.', '\n')

first_medical_record = medical_records[0]

print(f'Here is the first medical record: {first_medical_record}', '\n')

def sort_medical(lst):
  return (sorted(lst, key = lambda x: x[1]))

sorted_medical_records = sort_medical(medical_records)

print(f'Here are the medical records sorted by insurance cost: {sorted_medical_records}', '\n')

cheapest_three = sorted_medical_records[:3]

print(f'Here are the three cheapest insurance costs in our medical records: {cheapest_three}', '\n')

priciest_three = sorted_medical_records[-3:]

print(f'Here are the three most expensive insurance costs in our medical records: {priciest_three}', '\n')

occurrences_paul = names.count('Paul')

print(f'There are {occurrences_paul} individuals with the name Paul in our medical records.', '\n')

def sort_medical_alpha(lst):
  return (sorted(lst, key = lambda x: x[0]))

sorted_medical_records_alpha = sort_medical_alpha(medical_records)

print(sorted_medical_records_alpha, '\n')

middle_five_records = medical_records[3:8]

print(middle_five_records)