medical_costs ={}

medical_costs['Marina'] = 6607.0

medical_costs['Vinay'] = 3325.0

medical_costs.update({'Connie': 8886.0, 'Issac': 16444.0, 'Valentina': 6420.0})

print(medical_costs)

medical_costs['Vinay'] = 3325.0

print(medical_costs)

total_cost = 0

for value in medical_costs.values():
  total_cost += value

average_cost = total_cost / len(medical_costs)

print(f"Average Insurance Cost: {average_cost}")

names = ['Marina', 'Vinay', 'Connie', 'Issac', 'Valentina']

ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {key:value for key, value in zipped_ages}

print(names_to_ages)

marina_age = names_to_ages.get('Marina', 'None')

print(f"Marina's age is {marina_age}")

medical_records = {}

medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records.update(
  {'Vinay': 
  {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3325.0}, 
  'Connie': 
  {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0},
  'Issac': 
  {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0},
  'Valentina':
  {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})

print(medical_records)

print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")

medical_records.pop('Vinay')

for name, record in medical_records.items():
  print(f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}")

def update_medical_records(name, age, sex, smoker, bmi, insurance_cost):
  medical_records.update({name:{'Age': age, 'Sex': sex, 'Smoker': smoker, 'BMI': bmi, 'Insurance_cost': insurance_cost}})

update_medical_records('Spongebob', 23, 'Non-binary', 'Non-smoker', 5, 5000.0)

print(medical_records)
