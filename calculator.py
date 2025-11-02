num1 = int(input('enter your first number'))
num2 = int(input('enter your second number'))
sign = str(input("type the function you want to do(e.g +, -)"))
if sign is '+':
  ans = num1 + num2 
elif sign is '-':
  ans = num1 - num2 
elif sign is '/':
  ans = num1/num2 
elif sign is '*':
  ans = num1*num2 
elif sign is '**':
  ans = num1 ** num2
exit 
print ('the answer is', ans)
  
