'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

string1 = '()()(())'
string2 = ')()'
string3 = '([])[]({})'
string4 = '([)]'
string5 = '((()'

def well_balance(string):
	brackets = {'{': '}', '(': ')', '[' : ']'}
	saved_brackets = []

	for bracket in string:
		if bracket in brackets:
			saved_brackets.append(bracket)
		else:
			if not saved_brackets:
				return False

			last_bracket = saved_brackets.pop()
			
			if brackets[last_bracket] != bracket:
				return False


	if saved_brackets:
		return False
	return True

print(well_balance(string1)) #--> True
print(well_balance(string2)) #--> False
print(well_balance(string3)) #--> True
print(well_balance(string4)) #--> False
print(well_balance(string5)) #--> False
