'''
Author : Jitendra Kumar Mohapatra
Description : This python script generates the complex password by using the user input preferance  
'''
import random
import string
import secrets
'''The secrets module is design for cryptography - it generates robust random numbers 
which almost certainly do not use the 'mersene twister' generator that the random module 
uses by default. Also the functions in the secrets module are design for generation of 
secret keys, urls etc, whereas the functions in the random module are designed for shuffling data etc.'''

lower_case= string.ascii_lowercase # It will give the lowercase letters
upper_case= string.ascii_uppercase # # It will give the uppercase letters
digits= string.digits # It will give the digits 
special_char=string.punctuation # It will give all the special char 

allChars = lower_case + upper_case + digits + special_char
password = ""
# Take input from the user 
while True:
 pwLen = int(input("Give the length of the password: "))
 minUpper = int(input("Minimum Upper Case: "))
 minLower = int(input("Minimum Lower Case: "))
 minDigits = int(input("Minimum Numbers: "))
 minSpec = int(input("Minimum Special: "))
# check & validate the user inputs
 if pwLen >= minUpper+minLower+minDigits+minSpec:
     break
 else:
     print("***********************************************************************") 
     print("Sorry! Given password preference is not match with the legth of the password") 
     print("***********************************************************************")
# "join function" used to takes all items in an iterable and joins them into one string.
# "choice function" used to returns a randomly selected element from the specified sequence.
for j in range(minUpper):
    password += "".join(random.choice(secrets.choice(upper_case)))

for j in range(minLower):
    password += "".join(random.choice(secrets.choice(lower_case)))

for j in range(minDigits):
    password += "".join(random.choice(secrets.choice(digits)))

for j in range(minSpec):
    password += "".join(random.choice(secrets.choice(special_char)))

remaining = pwLen - minLower - minUpper - minDigits - minSpec

for j in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))

# Combine password and suffle it 
password = list(password)
random.shuffle(password)
print("Your Generated Password is:","".join(password)) 
 
