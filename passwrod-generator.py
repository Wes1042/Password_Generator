import random
import string


print(' Welcome to a password generator\n')
print('     It is reccomended that you have at least a 8 length password or more with at least one Upper ,one lower , one symbol , and one number\n')
print(' You have 2 options!!: ')
print('     1.Input a word/passphrase and the program will generate a password (It is less secure but easy to remember)')
print('     2.Program will create a complex password based on your lenght provided (Hard to crack yet more secure!)')
print(' Choose your option: ')
user = str(input())
if user !=  "1" and "2":
    print('Please enter one of the following options provided!!!')
    user = str(input())





lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = "!@#$%^&*"
all_characters  = num + lower + upper + symbols


def password():
    print('Please input the lenght of your password you wish to create: ')
    user_input = int(input())
    combo = random.sample(all_characters, user_input)
    password = "".join(combo) #string 
    return password



if (user == '1'):
    print('Please enter your word/passphrase: ')
    word = str(input())
    print('You will be asked to input the number of randomized characters you want. (This does not include your word)')
    final = str(word) + str(password())
    print('Your password is >>>> ' + final)
    
    
    
if (user == '2'):
    
    print( "Your password is >>>    " + password())
    