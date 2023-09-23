test_word =input('Enter any word or words to check if it is a palindrome:')
test_word1 = test_word.lower()
test_word1 = test_word1.strip()
back_test_word = test_word1[::-1]

if test_word1 == back_test_word:
    print(f'"{test_word.strip()}" is palindrome')

else: print(f'"{test_word.strip()}" is not palindrome')
