'''GUIアプリケーションのテスト'''
import tkinter

#ウィンドウの初期設定（ウィンドウ作成、タイトル、サイズ指定）
root = tkinter.Tk()
root.title("Test App")
root.geometry("500x500")

#ラベル「Label」
test_label = tkinter.Label(text='test', foreground='#0000ff')
test_label.pack()

#入力ボックス「Entry」
entry_box = tkinter.Entry(width=50)
entry_box.insert(tkinter.END, "ボタンを押すと消えます")
#↑入力ボックスの中に最初から文字列を入れておく場合
entry_box.pack()

#入力ボックスの中身の取得、削除
# print(entry_box.get())
# entry_box.delete(0, tkinter.END)

def delete_value(event):
    '''ボタンを押した時に実行される'''
    entry_box.delete(0, tkinter.END)

#ボタン「Button」
button = tkinter.Button(text="ボタンだよ", width=20)
#<Button-1>...左クリック
button.bind("<Button-1>", delete_value)
button.pack()

def check(event):
    '''チェックボックスの状態を取得する'''
    text = ""
    count = 0

    if val_one.get():
        text += "やること1は終わっています。\n"
        count += 1
    else:
        text += "やること1は終わっていません。やりましょう。\n"

    if val_two.get():
        text += "やること2は終わっています。\n"
        count += 1
    else:
        text += "やること2は終わっていません。やりましょう。\n"

    if val_three.get():
        text += "やること3は終わっています。\n"
        count += 1
    else:
        text += "やること3は終わっていません。やりましょう。\n"

    if count == 3:
        text += "やることは全て終わっています。お疲れ様でした。\n"

    print(text)


#チェックボックス「Checkbutton」
#チェックボックスの初期値を設定
val_one = tkinter.BooleanVar()
val_two = tkinter.BooleanVar()
val_three = tkinter.BooleanVar()

val_one.set(True)
val_two.set(False)
val_three.set(False)

check_box1 = tkinter.Checkbutton(text="やること1", variable=val_one)
check_box1.pack()

check_box2 = tkinter.Checkbutton(text="やること2", variable=val_two)
check_box2.pack()

check_box3 = tkinter.Checkbutton(text="やること3", variable=val_three)
check_box3.pack()

button_two = tkinter.Button(text="チェックボックスの取得", width=20)
button_two.bind("<Button-1>", check)
button_two.pack()

#ウィンドウ状態の維持
root.mainloop()
