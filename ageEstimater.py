# 1: Upon program initiationm, asks user for name and notifies user.
# 2: Next, program asks for user age, 
#    - checks for correct input
#    - calculates when user will turn 100
#    - returns output of when user will turn 100
#
#
###


# Function asks user for name and returns the string
def getName():
  while True:
    try:
      IO_name = input('Please enter your first name: ')
      break
    except NameError:
      print("Whoops! Please enter your name again using \"Quotations\"!")
  return IO_name

# Function asks user to enter "y" or "no" to verify the name entered, and returns the confirmation value
def verifyName():
  while True:
    try:
      confirmName = input('Please confirm your name (y/n): ')
      break
    except NameError:
      print("Whoops! Remember those \"Quotations\"!")
  return confirmName

# Function asks user for their age and returns the integer value
def getAge():
  while True:
    try:
      IO_age = input('Please enter your current age (as an integer): ')
      break
    except NameError:
      print("Whoops! Remember those \"Quotations\"!")
    # Need to get a handler to deal with when user enters a digit without quotes  
  return IO_age


#########

# Backbone of the program
def main():
  print "Welcome to the Centurion Calculator!" 
  
  # Flags to run the getName and verifyName functions. Flags will turn false when the question has been satisfied 
  # which means the user is ok with the input.
  nameFlag = True
  confirmFlag = True

  # Loop to run getName method to grab name from user.
  while nameFlag:
    name = getName()
    print('Hello, the name you have entered is: ' + name)
    confirmFlag = True

    # Loop to run verifyName method to confirm from user name is correct
    while confirmFlag:
      verifName = verifyName()
      if verifName == "y":
        confirmFlag = False
        nameFlag = False
      elif verifName == "n":
        confirmFlag = False
      else: 
        print("Invalid input. Please confirm again.")
  
  # Flags to run the getAge function 
  ageFlag = True

  while ageFlag:
    age = getAge()

    if age.isdigit():
      howManyMoreYrs = 100 - int(age)
      yearTo100 = 2018 + howManyMoreYrs
      print(name + ", you will turn 100 years old in " + str(yearTo100) + ".")
      print("(Just survive " + str(howManyMoreYrs) + " more years!)")
      ageFlag = False
    else:
      print("Invalid input. Please enter your age again as an integer.")
  return

###

if __name__ == '__main__':
  main()