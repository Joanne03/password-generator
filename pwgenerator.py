import string
import random

#data base
low = string.ascii_lowercase
up = string.ascii_uppercase
num = string.digits
special = string.punctuation
easydata = string.hexdigits
harddata = low + up + num + special

#generate / print hard pw
def hardpw():
	hardsample = random.sample(harddata, 12)
	h_result = ''.join(hardsample)
	print('This is your password:   ' + h_result)

#generate / print easy pw
def easypw():
	easysample = random.sample(easydata, 8)
	e_result = ''.join(easysample)
	print('This is your password:   ' + e_result)

#main program
def main():
	while True:
		print('Welcome to password generator!')
		user_input = input('Please choose password security level\n 1: high\n 2: normal\n Enter here: ')

		if user_input == 'q':
			print('Program ended')
			break
		elif user_input == '1':
			hardpw()
		elif user_input == '2':
			easypw()
		else:
			print('Input error, please try again')
		print('==========================================')

main()