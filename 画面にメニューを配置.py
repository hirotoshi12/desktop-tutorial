import tkinter as tk

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウをサイズを設定
baseGround.geometry('800x500')
# ウィンドウのタイトルを設定
baseGround.title('タイトル')

def callback():
    print("プログラムを閉じる")
    
menubar = tk.Menu(baseGround)

baseGround.config(menu = menubar)

file = tk.Menu(menubar)
menubar.add_cascade(label = 'ファイル', menu = file)

file.add_cascade(label = '閉じる', command = callback)

edit = tk.Menu(menubar)
menubar.add_cascade(label = 'エディット', menu = edit)

baseGround.mainloop()