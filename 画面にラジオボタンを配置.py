import tkinter as tk

#　メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('ラジオボタン配置')

# ラジオボタンに表示する文字列
item = ["A", "B", "C", "D"]

# Intvarオブジェクトを作成して変数に代入
val = tk.IntVar()

# ラジオボタンの作成と配置
# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # 親要素を指定
    tk.Radiobutton(baseGround,
                   # valueの値を1にする
                   value = i,
                   # variableにIntVarオブジェクトを指定
                   variable = val,
                   # textにリストitemのi番目の要素を指定
                   text = item[i]
                   # 左寄せで配置する
                   ).pack(anchor=tk.W)
    
# ラジオボタンの状態を通知する関数
def choice():
    # Intvarオブジェクトの値を取得
    ch = val.get()
    # リストitemのインデックスをchに指定して要素を出力
    print(item[ch] + "を選択しました。")

# ボタンの作成と配置
button = tk.Button(baseGround,
                   text = 'OK',
                   # クリック時にchoice()関数を呼ぶ
                   command= choice
                   ).pack(side = tk.LEFT)

baseGround.mainloop()