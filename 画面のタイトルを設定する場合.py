import tkinter as tk

#　メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('タイトル')

# pack()メソッドで配置場所を指定する
# buttonA = tk.Button(
#     baseGround, text = 'ボタンA').pack()

# buttonB = tk.Button(
#     baseGround, text = 'ボタンB').pack(side = tk.LEFT)

# buttonC = tk.Button(
#     baseGround, text = 'ボタンC').pack(side = tk.RIGHT)

# grid()メソッドで配置場所を指定
# buttan1 = tk.Button(
#     baseGround, text = '1').grid(row=0, column=1)

# buttan2 = tk.Button(
#     baseGround, text = '2').grid(row=0, column=2)

# buttan3 = tk.Button(
#     baseGround, text = '3').grid(row=0, column=3) 

# place()メソッドで配置場所を指定
buttan1 = tk.Button(
    baseGround, text = '1').place(x=50, y=100)

buttan2 = tk.Button(
    baseGround, text = '2').place(x=100, y=150)

buttan3 = tk.Button(
    baseGround, text = '3').place(x=150, y=200) 


baseGround.mainloop()