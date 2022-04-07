import tkinter as tk

# メインウィンドウを作成
baseGrond = tk.Tk()

# ウィンドウのサイズを設定
baseGrond.geometry('500x300')

# ウィンドウのタイトルを設定
baseGrond.title('テキストボックス')

# ラベル
label = tk.Label(text='テキストボックス')
# label.place(x=30, y=70)

# テキストボックス
txtBox = tk.Text(width=20, height= 15)
txtBox.pack()

baseGrond.mainloop()