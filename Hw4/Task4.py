# Solution_1: with changing the list

test_data = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
test_data.sort(key=str.lower)

print(f'The list was sorted and updated: {test_data}')


# Solution_2: with no changing the list

test_data = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
print(f'The list was sorted but wasn\'t changed:{sorted(test_data, key= str.lower)}')
