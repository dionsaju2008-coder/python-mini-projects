import random
print ('how many letters do you want:')
number=int(input())
letter = ("abcdefghijlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$*&%?~")
result=(random.sample(letter,k=number))
password=''.join(result)
print('your password will be: ' + password)

