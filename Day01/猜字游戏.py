import random
number1 = random.randint(1,100)
guess_count = 0
print("欢迎")
number2 = input ("在1-100之间输入一个数字")
number2 = int (number2)
while True :
    guess_count = guess_count + 1
    if number2 == number1 :
       print ("你花了" ,guess_count ,"次猜对了")
       break
    elif guess_count == 5 :
        print ("猜测次数已经达5次，游戏结束")
        break
    else :
        if number2 < number1 :
           print ("猜小了")
        else :
            print ("猜大了")
        number2 = input("请重新输入")
        number2 = int(number2)   
