import tkinter as tk

def btn_click():
    
    # 最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()
        
    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('500x300')
    # GUIの画面タイトル
    baseGround_new_csv.title('結果')
    
    height = text1.get()
    height_f = float(height) # stringからfloatに
    weight = text2.get()
    weight_f = float(weight) # stringからfloatに
    
    height_m = height_f / 100
    result = weight_f / (height_m * height_m)
    result_str = str(round(result, 2))
    
    # BMI計算
    if result < 18.5:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str + "は痩せています")
    elif result >= 18.5 and result < 25:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str + "標準です")
    elif result >= 25 and result < 30:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str + "肥満(1度)です")
    elif result >= 30 and result < 35:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str + "肥満(2度)です")
    elif result >= 35 and result < 40:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str + "肥満(3度)です")
    elif result >= 40:
        lbl_result = tk.Label(baseGround_new_csv, text='BMIは' + result_str + "肥満(4度)です")
    else:
        lbl_result = tk.Label(baseGround_new_csv, text='エラー')
    
    lbl_result.pack()
    
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()

baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('500x300')
# GUIの画面タイトル
baseGround.title('BMI計算')
label1 = tk.Label(baseGround, text='BMIの計算')
label1.pack()
label2 = tk.Label(baseGround, text='身長(cm)')
label2.pack()
text1 = tk.Entry(width=30)
text1.pack()
label3 = tk.Label(baseGround, text='体重(kg)')
label3.pack()
text2 = tk.Entry(width=30)
text2.pack()
# ボタン
btn = tk.Button(baseGround, text='OK', command=btn_click)
btn.pack()

# 表示
baseGround.mainloop()