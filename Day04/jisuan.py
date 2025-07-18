def jisuanqi():
    import gongshi
    a = float(input("请输入一个数： "))
    while True:
       try:
          s = input("输入要运行的计算和数字,q退出： ")
          if s == "q":
             print("谢谢使用")
             break
          c, b = s.split()
          b = float(b)
          if c == "+":
             a = f"{gongshi.add(a, b):.5f}"
          elif c == "-":
             a = f"{gongshi.substruct(a, b):.5f}"
          elif c == "*":
             a = f"{gongshi.multiply(a, b):.5f}"
          elif c == "/":
             a = f"{gongshi.divide(a, b):.5f}"
          else:
             print("操作无效")
             continue
          s = a.rstrip('0').rstrip('.')
          print (s)
          a = float(a)
       
       except ValueError:
          print("输入个是错误")
          return None
       except ZeroDivisionError as e:
          print(e)
          return None
    return a
if __name__ == "__main__":
   jisuanqi()