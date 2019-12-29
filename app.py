def calculator():

	operation = input('What do you want to do? ')
	num1 = float(input('Enter first number: '))
	num2 = float(input('Enter second number: '))
	
	
	if operation == '+':
		result = num1 + num2
	elif operation == '-':
		result = num1 - num2
	elif operation == '*':
		result = num1 * num2
	else:
		result = num1 / num2
		
	return result
	
print('The result is ' + str(calculator()))
		
		


