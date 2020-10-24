# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  message = f"The estimated insurance cost for {name} is {estimated_cost} dollars."
  print(message)
  return message, estimated_cost

# Estimate Maria's insurance cost
maria_message, maria_insurance_cost = calculate_insurance_cost('Maria', 28, 0, 26.2, 3, 0)

# Estimate Omar's insurance cost 
omar_message, omar_insurance_cost = calculate_insurance_cost('Omar', 35, 1, 22.2, 0, 1)

def insurance_cost_difference(name1, age1, sex1, bmi1, num_of_children1, smoker1, name2, age2, sex2, bmi2, num_of_children2, smoker2):
  message1, cost1 = calculate_insurance_cost(name1, age1, sex1, bmi1, num_of_children1, smoker1)
  message2, cost2 = calculate_insurance_cost(name2, age2, sex2, bmi2, num_of_children2, smoker2)
  difference = cost1 - cost2
  print(f"The difference in insurance cost between {name1} and {name2} is {difference} dollars.")
  if cost1 > cost2:
    print(f"{name1} is estimated to cost more than {name2}")
  elif cost1 < cost2:
    print(f"{name2} is estimated to cost more than {name1}")
  else:
    print(f"The estimated cost for both people are equal.")

insurance_cost_difference('Maria', 28, 0, 26.2, 3, 0, 'Omar', 35, 1, 22.2, 0, 1)