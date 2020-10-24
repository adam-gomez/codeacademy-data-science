# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
    print(f"You need to lower your bmi by {round((bmi_value - 24.9), 1)} to reach a healthy weight")
  elif bmi_value >= 25:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
    print(f"You need to lower your bmi by {round((bmi_value - 24.9), 1)} to reach a healthy weight")
  elif bmi_value >= 18.5:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")
    print(f"You need to increase your bmi by {round((18.5-bmi_value), 1)} to reach a healthy weight.")
  

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

spongebobs_insurance_cost = estimate_insurance_cost(name = 'Spongebob', age = 34, sex = 1, bmi = 1, num_of_children = 0, smoker = 0)