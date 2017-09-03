mystring = input("Please enter word: ")

def is_palindrome(mystring):
    mystring = mystring.lower().replace(' ', '')
    rev_string = ''.join(reversed(mystring))
    return mystring == rev_string
print('YES' if is_palindrome(mystring) else 'NO')