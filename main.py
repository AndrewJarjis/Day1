user_input = input("Enter a string: ")
print("You entered:", user_input)

user_input = int(input('Enter a number: '))
output_number = user_input + 1
print('The result is:', output_number)

user_input = float(input('Enter a number: '))
user_input += 0.5
print('The updated number is ', user_input)

num1 = float(input('Please enter the first number: '))
num2 = float(input('Please enter the second number: '))
sum = num1 + num2
print('The sum of', num1, "and", num2, "is", sum)

num1 = float(input('Please enter the first number: '))
num2 = float(input('Please enter the second number: '))
sum = num1 * num2
print('The product of', num1, "and", num2, "is", sum)

num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
sum = num1 / num2
print('The quotient of', num1, "and", num2, "is", sum)


user_input = input("Enter a boolean (True or False): ")
user_boolean = user_input == "true"
print("You entered:", user_boolean)
print("The opposite is:", not user_boolean)


