def rbCity():  #點選縣市選項按鈕後處理函式
    global sitelist, listradio
    sitelist.clear()  #清除原有測站串列
    for r in listradio:  #移除原有測站選項按鈕
        r.destroy()
    n=0
    for c1 in data["County"]:  #逐一取出選取縣市的測站
        if(c1 == city.get()):
            sitelist.append(data.iloc[n, 5])
        n += 1    
    sitemake()  #建立測站選項按鈕
    rbSite()  #顯示PM2.5訊息

def rbSite():  #點選測站選項按鈕後處理函式
    n = 0
    for s in data.iloc[:, 5]:  #逐一取得測站
        if(s == site.get()):  #取得點選的測站
            pm = data.iloc[n, 3]  #取得PM2.5的值
            if(pm=='' or pm=='ND'):  #如果沒有資料
                result1.set(s + "站的 PM2.5 值目前無資料！")
            else:  #如果有資料
                if(int(pm) <= 35):  #轉換為等級
                    grade1 = "低"
                elif(int(pm) <= 53):
                    grade1 = "中"
                elif(int(pm) <= 70):
                    grade1 = "高"
                else:
                    grade1 = "非常高"
                result1.set(s + "站的 PM2.5 值為「" + str(pm) + "」：「" + grade1 + "」等級")
            break  #找到點選測站就離開迴圈
        n += 1
    
def clickRefresh():  #重新讀取資料
    global data
    data = pd.read_json("https://ehappyapi.herokuapp.com/pm25/")
    rbSite()  #更新測站資料

def sitemake():  #建立測站選項按鈕
    global sitelist, listradio
    for c1 in sitelist:  #逐一建立選項按鈕
        rbtem = tk.Radiobutton(frame2, text=c1, variable=site, value=c1, command=rbSite)  #建立選項按鈕
        listradio.append(rbtem)  #加入選項按鈕串列
        if(c1==sitelist[0]):  #預設選取第1個項目         
            rbtem.select()
        rbtem.pack(side="left")  #靠左排列

import tkinter as tk #主程式
import pandas as pd

data = pd.read_json("https://ehappyapi.herokuapp.com/pm25/")

win=tk.Tk() #WINDOW的介面 第48行提供
win.geometry("640x270")
win.title("PM2.5 實時監測")

city = tk.StringVar()  #縣市文字變數
site = tk.StringVar()  #測站文字變數
result1 = tk.StringVar()  #訊息文字變數
citylist = []  #縣市串列
sitelist = []  #鄉鎮串列
listradio = []  #鄉鎮選項按鈕串列
#64到87看得懂
#建立縣市串列 
for c1 in data["County"]:  
    if(c1 not in citylist):  #如果串列中無該縣市就將其加入
        citylist.append(c1)
#建立第1個縣市的測站串列
count = 0
for c1 in data["County"]:  
    if(c1 ==  citylist[0]):  #是第1個縣市的測站
        sitelist.append(data.iloc[count, 5])
    count += 1

label1 = tk.Label(win, text="縣市：", pady=6, fg="blue", font=("新細明體", 12))
label1.pack()
frame1 = tk.Frame(win)  #縣市容器
frame1.pack()
for i in range(0,3):  #3列選項按鈕
    for j in range(0,8):  #每列8個選項按鈕
        n = i * 8 + j  #第n個選項按鈕
        if(n < len(citylist)):
            city1 = citylist[n]  #取得縣市名稱
            rbtem = tk.Radiobutton(frame1, text=city1, variable=city, value=city1, command=rbCity)  #建立選項按鈕
            rbtem.grid(row=i, column=j)  #設定選項按鈕位置
            if(n==0):  #選取第1個縣市
                rbtem.select()

label2 = tk.Label(win, text="測站：", pady=6, fg="blue", font=("新細明體", 12))
label2.pack()
frame2 = tk.Frame(win)  #測站容器
frame2.pack()
sitemake()

btnDown = tk.Button(win, text="更新資料", font=("新細明體", 12), command=clickRefresh)
btnDown.pack(pady=6)
lblResult1 = tk.Label(win, textvariable=result1, fg="red", font=("新細明體", 16))
lblResult1.pack(pady=6)
rbSite()  #顯示測站訊息

win.mainloop()