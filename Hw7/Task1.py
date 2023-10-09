list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_1 = set(list_a)
set_2 = set(list_b)

initial_answer = set_1.intersection(set_2)
answer = sorted(initial_answer)

print(f'The common unique numbers in lists are: {answer}')
