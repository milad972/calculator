from pymsgbox import alert

def again(func):
   def cal():
     func()
     cal_again = input("""
    do you want to calculator again ?
    please type yes or no ? Y/N
   """)
     if cal_again.upper() == 'Y':
          calculator()
     elif cal_again.upper() == 'N':
         print('see you')
     else:
          print(cal_again)
          cal()
   return cal



@again
def calculator():
   number1 = int(input('please enter your number 1 :'))
   number2 = int(input('please enter your number 2 :'))
   operator = input('''please enter operator :
- for subtract
+ for plus
* for Multiply
/ for division
    ''')
   if operator == "+":
       print(f"{number1} + {number2} = {number1 + number2}")
   elif operator == "-":
       print(f"{number1} - {number2} = {number1 - number2}")
   elif operator == '*':
       print(f"{number1} * {number2} = {number1 * number2}")    
   elif operator == '/':
      try:
       print(f"{number1} / {number2} = {number1 / number2}")
      except:
       alert(text = "ZeroDivisionError" , title = "Error Type" ) 
   else:
       print('not found')

calculator()