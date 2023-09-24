# Solution_1
number_1 = float(input('Enter number #1:'))
number_2 = float(input('Enter number #2:'))

plus = number_1 + number_2
minus = number_1 - number_2
multiple = number_1 * number_2
divide = number_1 / number_2

print(f'Result of plus: {plus}')
print(f'Result of minus: {minus}')
print(f'Result of multiple: {multiple}')
print(f'Result of plus: {divide}')


# Solution_2
number_1 = float(input('Enter number #1:'))
number_2 = float(input('Enter number #2:'))
action = input("Choose action: 'plus', 'minus', 'multiple', 'divide': ")

if action == 'plus':
    result_1 = number_1 + number_2
    print(f'Result is: {result_1}')

elif action == 'minus':
    result_2 = number_1 - number_2
    print(f'Result is: {result_2}')

elif action == 'multiple':
    result_3 = number_1 * number_2
    print(f'Result is: {result_3}')

elif action == 'divide':
    result_4 = number_1 / number_2
    print(f'Result is: {result_4}')

else: print('You didn\'t specified possible action')

