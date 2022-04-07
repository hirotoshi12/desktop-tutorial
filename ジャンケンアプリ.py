import tkinter as tk
import random

def btn_click():
    
    num = random.randint(0, 2)
    
    # 最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()
    
    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('300x200')
    # GUIの画面タイトル
    baseGround_new_csv.title('結果')
    
    if i == num:
        lbl_filename = tk.Label(baseGround_new_csv, text='あいこ')
    elif i == 0 and num == 1 or i == 1 and num == 2 or i == 2 and num == 0:
        lbl_filename = tk.Label(baseGround_new_csv, text='勝利')
    else:
        lbl_filename = tk.Label(baseGround_new_csv, text='敗北')
        
    lbl_filename.pack()
    
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()

baseGrond = tk.Tk()
# GUIの画面サイズ
baseGrond.geometry('300x200')
# GUIの画面タイトル
baseGrond.title('最初の画面')
label1 = tk.Label(baseGrond, text='ジャンケンします')
label1.pack()
label2 = tk.Label(baseGrond, text='グーチョキパーのどれかを選択してください')
label2.pack()
# ボタン
btn = tk.Button(baseGrond, text='OK', command=btn_click)
btn.place(x=120, y=140)

# ラジオボタンに表示する文字列
item = ['グー', 'チョキ', 'パー']

# Intvarオブジェクトを作成して変数に代入
val = tk.IntVar()

# ラジオボタンの作成と配置
# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # 親要素を指定
    tk.Radiobutton(baseGrond,
                   # valueの値
                   value = i,
                   # variableにIntVarオブジェクトを指定
                   variable = val,
                   # textにリストitemのi番目の要素を指定
                   text = item[i]
                   # 左寄せで配置する
                   ).pack()

# 表示
baseGrond.mainloop()