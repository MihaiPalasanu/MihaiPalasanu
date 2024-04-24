# Active variable to control loop
keep_going = True

while keep_going:
  
  try:
    age = int(input("Enter your age (or 'quit' to exit): "))
  except ValueError:
    print("Please enter a valid age (number).")
    continue

  
  if age < 3:
    print("Your ticket is free!")
  elif 3 <= age <= 12:
    print("Your ticket costs $10.")
  elif age > 12:
    print("Your ticket costs $15.")
  else:
    print("Invalid age entered. Please try again.") 

  
  user_choice = input("Do you want to check another age (yes/no)? ").lower()
  if user_choice == 'no':
    keep_going = False  

print("Thank you!")
