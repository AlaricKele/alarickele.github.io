# Python 控制台计算器
def calculator():
    print("===== Python 简易计算器 =====")
    print("支持运算：+ - * /")
    print("输入 'exit' 退出程序\n")

    while True:
        num1 = input("请输入第一个数字：")
        if num1.lower() == "exit":
            print("程序已退出")
            break
        
        op = input("请输入运算符(+ - * /)：")
        if op.lower() == "exit":
            print("程序已退出")
            break

        num2 = input("请输入第二个数字：")
        if num2.lower() == "exit":
            print("程序已退出")
            break

        # 类型转换
        try:
            n1 = float(num1)
            n2 = float(num2)
        except:
            print("❌ 输入格式错误，请输入数字！\n")
            continue

        # 运算逻辑
        if op == "+":
            res = n1 + n2
        elif op == "-":
            res = n1 - n2
        elif op == "*":
            res = n1 * n2
        elif op == "/":
            if n2 == 0:
                print("❌ 除数不能为0！\n")
                continue
            res = n1 / n2
        else:
            print("❌ 未知运算符！\n")
            continue
        
        print(f"计算结果：{n1} {op} {n2} = {res}\n")

if __name__ == "__main__":
    calculator()
