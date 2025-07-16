def jisuanqi():
    import gongshi
    a = float(input("请输入一个数"))
    while True:
       try:
          c, b = input("输入要运行的计算和数字").split()
          b = float(b)
          if c == "+":
             result = f"{gongshi.add(a, b):.5f}"
          elif c == "-":
             result = f"{gongshi.substruct(a, b):.5f}"
          elif c == "*":
             result = f"{gongshi.multiply(a, b):.5f}"
          elif c == "/":
             result = f"{gongshi.divide(a, b):.5f}"
          else:
             print("操作无效")
             continue
          s = result.rstrip('0').rstrip('.')
          print (s)
          a = float(result)
       
       except ValueError:
          print("输入个是错误")
       except ZeroDivisionError as e:
          print(e)
if __name__ == "__main__":
   jisuanqi()