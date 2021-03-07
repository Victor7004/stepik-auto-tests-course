import math

flou = input('Hello! What do you want to do  "+", "-", "*", "/", "**", "%", "round", "pi" :')
number1 = input('enter  number1 :')
number2 = input('enter number2 :')
number3 = 1
number4 = 1
if flou == ('+'):
    number3 = int(number1) + int(number2)
elif flou == '-':
    number3 = int(number1) - int(number2)
elif flou == '*':
    number3 = int(number1) * int(number2) 
elif flou == '/':
    number3 = int(number1) / int(number2) 
elif flou == '**':
    number3 = int(number1) ** int(number2)
elif flou == '%':
    number3 = int(number1) % int(number2) 
elif flou == 'round':
    number3 = float(number1) % 1
    number4 = float(number2) % 1
    if  number3 == 0:
        number2 =(math.floor(float(number2)))
    if  number4 == 0:
        number2 =(math.floor(float(number2)))
else:
    print(" You entered an invalid character!!! ")
        
print('Result :',number3)