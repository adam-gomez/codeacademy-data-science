medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""


print(medical_data, "\n")

updated_medical_data = medical_data.replace("#", "$")

num_records = 0

for char in updated_medical_data:
  if char == "$":
    num_records += 1

print(f"There are {num_records} medical records in the data.")

# SPLITTING STRINGS
medical_data_split =  updated_medical_data.split(";")

print(medical_data_split)
print("\n")
medical_records = []

for records in medical_data_split:
  medical_records.append(records.split(','))

print(medical_records)

medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean, "\n")

for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print(names, ages, bmis, insurance_costs)

total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)

print(f"Average BMI: {average_bmi}")

insurance_costs_nums = []
for amount in insurance_costs:
  insurance_costs_nums.append(amount.replace("$", ""))

total_insurance_cost = 0
for cost in insurance_costs_nums:
  total_insurance_cost += float(cost)

average_insurance_cost = total_insurance_cost / len(insurance_costs)

print(f"Average Cost: {average_insurance_cost}", "\n")

first_names = []

for name in names:
  first_names.append(name.split(" ")[0].title())

for i in range(len(first_names)):
  print(f"{first_names[i]} is {ages[i]} years old with a BMI of {bmis[i]} and an insurance cost of ${insurance_costs_nums[i]}.", "\n")