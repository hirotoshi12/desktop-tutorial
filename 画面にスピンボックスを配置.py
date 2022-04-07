import tkinter as tk

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウをサイズを設定
baseGround.geometry('500x300')

# GUIの画面タイトル
baseGround.title('スピンボックスを配置')

spinbox = tk.Spinbox(baseGround, value = ("ボックス１", "ボックス２", "ボックス３", "ボックス４"))
spinbox.pack()

baseGround.mainloop()
