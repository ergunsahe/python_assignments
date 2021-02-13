# First Sample to check phone number that is desired

''' import re
def check_phone(phone_number):
    pattern = re.compile(r'^\d{3} \d{2}-\d{2}$')
    result = pattern.search(phone_number)
    if result:
        return result.group()
    return 'Please write phone number that it is desired'

print(check_phone('123 44-55'))
print(check_phone('X123 44-55'))
print(check_phone('123 44-551'))
print(check_phone('1234 44-55'))
print(check_phone('1234 44-55adfgfa')) '''


# Second Sample to find all numbers in a given string

''' import re

test_string = 'haf3dh45 sfd234dsgfs4b 34 dgsf'
pattern = r'\d+'
result = re.findall(pattern, test_string)
print(result)
print(result[0]) '''


#-----------
import re

pattern = re.compile(r'''
    (^[a-zA-Z0-9_.+-]+ ) # 1.group
    @                  # @ symbol
    ([a-zA-Z0-9-]+  )    # 2. group
    \.                 # dot
    ([a-zA-Z0-9-.]+$)    # 3. group


''', re.VERBOSE)

result = pattern.search('arinyazilim@gmail.com')


print(result.group())
print(result.groups())
print(result.groups()[0])
    