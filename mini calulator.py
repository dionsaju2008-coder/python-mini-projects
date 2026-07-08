print('Enter the three numbers')
num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
num3=int(input('enter the third number:'))
print('*\n*\n*\n*\nwhat do you want to do next:\nAddition(Type +)\nsubtraction(Type -)\nMultiply(Type *)\nDivide(Type /)\n*\n*\n*')
word=input()
print('your result is:')
if (word == '+'):
    print(num1+num2+num3)
elif(word=='-'):
    print(num1-num2-num3)
elif(word=='*'):
    print(num1*num2*num3)
elif(word=='/'):
    print(num1/num2/num3)
else:
    print('not the action you want')
