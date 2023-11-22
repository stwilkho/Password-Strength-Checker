# Password Strength checker
# by Wilkho Tshink

import string
import getpass


def check_password_strength():
   pswd = getpass.getpass('Enter the password: ')
   pStrength = 0
   rmks = ''
   lower_c = upper_c = num_c = wspace_c = special_c = 0

   for char in list(pswd):
       if char in string.ascii_lowercase:
           lower_c += 1
       elif char in string.ascii_uppercase:
           upper_c += 1
       elif char in string.digits:
           num_c += 1
       elif char == ' ':
           wspace_c += 1
       else:
           special_c += 1

   if lower_c >= 1:
       pStrength += 1
   if upper_c >= 1:
       pStrength += 1
   if num_c >= 1:
       pStrength += 1
   if wspace_c >= 1:
       pStrength += 1
   if special_c >= 1:
       pStrength += 1

   if pStrength == 1:
       rmks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
   elif pStrength == 2:
       rmks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif pStrength == 3:
       rmks = 'Your password is okay, but it can be improved.'
   elif pStrength == 4:
       rmks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif pStrength == 5:
       rmks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

   print('Your password has:-')
   print(f'{lower_c} lowercase letters')
   print(f'{upper_c} uppercase letters')
   print(f'{num_c} digits')
   print(f'{wspace_c} whitespaces')
   print(f'{special_c} special characters')
   print(f'Password Score: {pStrength / 5}')
   print(f'Remarks: {rmks}')


def check_pwd(another_pswd=False):
   valid = False
   if another_pswd:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Thank You !')
           return False
       else:
           print('Invalid input...please try again. \n')


if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pswd = check_pwd()
   while check_pswd:
       check_password_strength()
       check_pswd = check_pwd(True)


