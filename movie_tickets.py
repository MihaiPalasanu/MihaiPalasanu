# Active variable to control loop
keep_going = True

while keep_going:
  # Get user's age
  try:
    age = int(input("Enter your age (or 'quit' to exit): "))
  except ValueError:
    print("Please enter a valid age (number).")
    continue  # Skip to the next iteration of the loop

  # Check age and display ticket price
  if age < 3:
    print("Your ticket is free!")
  elif 3 <= age <= 12:
    print("Your ticket costs $10.")
  elif age > 12:
    print("Your ticket costs $15.")
  else:
    print("Invalid age entered. Please try again.")  # Handle unexpected input

  # Check for user's exit choice
  user_choice = input("Do you want to check another age (yes/no)? ").lower()
  if user_choice == 'no':
    keep_going = False  # Stop the loop if user chooses no

print("Thank you!")
