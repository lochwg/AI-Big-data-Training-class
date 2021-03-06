import os,ast

def menu():
    os.system("cls")
    print("帳號、密碼管理系統")
    print("-------------------")
    print("1. 輸入帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("0. 結  束  程  式")
    print("-------------------")

#
def ReadData():
    with open('password.txt', 'r', encoding = 'UTF-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else: return dict()
        
def disp_data():
    print("帳號\t密碼")
    print("=================")
    for key in data:
        print("{}\t{}".format(key,data[key]))
    input("按任意鑑返回主選單")
    
    
#
def input_data():
    while True:
        name = input("請輸入帳號(Enter==>停止輸入)")
        if name == "": break
        if name in data:
            print("{}帳號已存在!".format(name))
            continue
        password = input("請輸入密碼: ")
        data[name] = password
        with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:
            f.write(str(data))
        print("{}已被儲存完畢".format(name))
        
data = dict()
data = ReadData()
while True:
    menu()
    choice = int(input("請輸入您的選擇: "))
    print()
    if choice ==1:
        input_data()
    elif choice ==2:
        disp_data()
    else:
        break

print("程式執行完畢！")
