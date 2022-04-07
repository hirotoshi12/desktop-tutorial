import tkinter as tk

# チェックボタンに表示する文字列を用意
item = ["印鑑", "口座手帳", "キャッシュカード", "住民票"]

check = {}

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('タイトル')

# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # BooleanVarオブジェクトを作成しリストのcheck要素に追加
    check[i] = tk.BooleanVar()
    # チェックボタンの作成と配置
    tk.Checkbutton(baseGround,
                   variable = check[i],
                   text = item[i]
                   ).pack(anchor= tk.W)

# チェックボタンの状態を通知する関数
def select():
    # 辞書cheak要素の数だけ繰り返す
    for i in check:
        if check[i].get() == True:
            print(item[i] + "チェックしました")

# ボタンの作成と配置
button = tk.Button(baseGround,
                   text = '必需品',
                   # クリックしたときにselect()関数を呼ぶ
                   command = select
                   ).pack(anchor = tk.W)  

baseGround.mainloop()