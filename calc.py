import tkinter as tk

# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('500x600')
# 画面タイトル
baseGround.title('割り勘アプリ')

# ラベルやボタンの作成と配置
label1 = tk.Label(baseGround, text='合計金額を設定して下さい', font=("MSゴシック", "20"))
label1.place(x=50, y=10, width=400, height=50)

txtField = tk.Entry()
txtField.place(x=150, y=60)

button1 = tk.Button(baseGround, text='OK', font=("MSゴシック", "10"))
button1.place(x=350, y=60, width=30, height=30)

selectedTax = '0'
label2 = tk.Label(baseGround, text= selectedTax + '円', font=("MSゴシック", "35", "bold"), background="lightgray")
label2.place(x=50, y=100, width=400, height=50)

label3 = tk.Label(baseGround, text='人数を設定してください', font=("MSゴシック", "20"))
label3.place(x=50, y=230, width=400, height=50)

label4 = tk.Label(baseGround, text = '1', font=("MSゴシック", "35", "bold"), background='lightgray')
label4.place(x=220, y=300, width=50, height=50)

button1 = tk.Button(baseGround, text= '-', font=("MSゴシック", "35"))
button1.place(x=100, y=300, width=50, height=50)

button2 = tk.Button(baseGround, text= '+', font=("MSゴシック", "35"))
button2.place(x=350, y=300, width=50, height=50)

label5 = tk.Label(baseGround, text = '1人当たり', font=("MSゴシック", "20"))
label5.place(x=50, y=450, width=400, height=50)

tax = '0'
label = tk.Label(baseGround, text = tax + '円', font=("MSゴシック", "35", "bold"), background="lightgray")

baseGround.mainloop()
