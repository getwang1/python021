name = input("What is your name")
age  = input ("How old are you")
age  = int(age)
future_age = age + 10
print("Hi",name + "!", "In 10 years, you will be", age+10, "years old")
if age < 18:
    print ("你是青少年")
else:
    print ("你是成年人")
color = input("What is your favourite color")
print(f"Your favorite color is { color }. Mine too!")
"""修改程序，允许用户输入 两个数字，并计算这两个数字的和"""
number1 = input("The first number")
number1 = int (number1)
number2 = input("The second number")
number2 = int (number2)
print ("The sum is" ,number1 + number2)
