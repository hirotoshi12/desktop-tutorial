import tkinter as tk

# メインウィンドウを作成
baseGrond = tk.Tk()

# ウィンドウのサイズを設定
baseGrond.geometry('500x300')

# ウィンドウのタイトルを設定
baseGrond.title('Python-tkinter:ラベル')

# ラベル
label1 = tk.Label(text='ここにラベル表示', foreground='orange', background='black')
label1.pack()

baseGrond.mainloop()