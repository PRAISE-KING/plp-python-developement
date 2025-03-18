
# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.





user_input_1 = float(input('Enter your first number : '))
user_input_2 = float(input('Enter your second number : '))

operation = input('Choose an operation (-,+,/,*) : ')

if operation == '+':
    output = user_input_1 + user_input_2
    print(f'{user_input_1} + {user_input_2} = {output}')
    
elif operation == '-':
    output = user_input_1 - user_input_2
    print(f'{user_input_1} - {user_input_2} = {output}')
    
elif operation == '*':
    output = user_input_1 * user_input_2
    print(f'{user_input_1} * {user_input_2} = {output}')
    
elif operation == '/':
    if user_input_2 != 0:
        output = user_input_1 / user_input_2
        print(f'{user_input_1} / {user_input_2} = {output}')
    else:
        print('Cannot divide number by 0')   

else:
    print('Invalid Operation ........ please enter a valid operation')       
        