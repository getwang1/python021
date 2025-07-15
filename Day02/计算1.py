a = float(input("请输入第一个数"))
b = float(input("请输入第二个数"))
c = input("请问你想进行哪种运算")
import gongshi
if c == "+":
    result = gongshi.add(a, b)
elif c == "-":
    result = gongshi.substruct(a, b)
elif c == "*":
    result = gongshi.multiply(a, b)
elif c == "/":
    result = gongshi.divide(a, b)
print (result)