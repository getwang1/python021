a = float(input("请输入一个数"))
while ValueError:
   c, b = input("输入要运行的计算和数字").split()
   b = float(b)
   import gongshi
   if c == "+":
       result = f"{gongshi.add(a, b):.5f}"
   elif c == "-":
       result = f"{gongshi.substruct(a, b):.5f}"
   elif c == "*":
       result = f"{gongshi.multiply(a, b):.5f}"
   elif c == "/":
       result = f"{gongshi.divide(a, b):.5f}"
   s = result.rstrip('0').rstrip('.')
   print (s)
   a = float(result)