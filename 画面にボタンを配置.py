import tkinter as tk

#　メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('タイトル')

buttan1 = tk.Button(
    baseGround, text = '1', foreground='red').pack()

buttan2 = tk.Button(
    baseGround, text = '2', foreground='blue').pack()

buttan3 = tk.Button(
    baseGround, text = '3', foreground='green').pack()


baseGround.mainloop()