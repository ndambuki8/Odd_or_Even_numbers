number = input("Enter a number and I will tell you if it is Even or Odd: \n")
number = int(number)

if (number % 2 == 0):
	print("\nThe number " + str(number)+ " is even.")
else:
	print('\nThe number ' + str(number) + ' is Odd.')
