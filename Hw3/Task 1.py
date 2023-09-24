# Home task_1
test_word = str(input('Enter any word:'))
remove_letter = input('Specify some word\'s letter to be removed:')
corrected_sentence = (test_word.replace(remove_letter,''))
print(f'Check what is done: {corrected_sentence}')

#Home task_2
string_initial_state = input('Type some sentence:')
string_medium_state = string_initial_state.lower()
string_ready_state = string_medium_state.title()
print(f'Get the correct typed string: {string_ready_state}')

#Home task_3
initial_string = input('Type some sentence and wait for the magic:')
finished_string = initial_string[::-1]
print(f'Magic is done: {finished_string}')

#Home task_4
string_1 = input('Enter any sentence you want:')
string_2 = input('Enter one more sentence:')
print(f'These values are identical: {string_1 == string_2}')

#Home task_5
repeat_string = input('Enter some letters:')
numbers_amount = int(input('Enter how many times the letters should be repeated:'))
result = repeat_string * numbers_amount
print(f'Check that the letters are repeated {numbers_amount} times:{result}')

#Home task_6
uah_1 = float(input('Enter how many uah you want to exchange:'))
dollar_rate1 = float(input('Enter today\'s dollar rate:'))
gotten_money_1 = uah_1*dollar_rate1
print(f'You will receive {gotten_money_1} USD')
dollars_2 = float(input('Enter how many dollars you want to exchange:'))
uah_rate2 = float(input('Enter today\'s hrivna rate:'))
gotten_money_2 = dollars_2*uah_rate2
print(f'You will receive {gotten_money_2} hrivnas, congrats!')
uah_3 = float(input('Enter how many uah you want to exchange:'))
euro_rate3 = float(input('Enter today\'s euro rate:'))
gotten_money_3 = uah_3*euro_rate3
print(f'You will receive {gotten_money_3} USD')
euro_4 = float(input('Enter how many euros you want to exchange:'))
uah_rate4 = float(input('Enter today\'s hrivna rate:'))
gotten_money_4 = euro_4*uah_rate4
print(f'You will receive {gotten_money_4} hrivnas, congrats!')

