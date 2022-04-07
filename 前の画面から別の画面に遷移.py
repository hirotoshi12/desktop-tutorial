import tkinter as tk

def btn_click():
    
    # 最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()
        
    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('300x200')
    # GUIの画面タイトル
    baseGround_new_csv.title('次の画面')
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text = '前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()

baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('300x200')
# GUIの画面タイトル
baseGround.title('最初の画面')

# ボタン
btn = tk.Button(baseGround, text='次の画面に移動', command=btn_click)
btn.place(x=120, y=140)

# 表示
baseGround.mainloop()