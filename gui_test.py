'''GUIアプリケーションのテスト'''
import tkinter

#ウィンドウの初期設定（ウィンドウ作成、タイトル、サイズ指定）
root = tkinter.Tk()
root.title("Test App")
root.geometry("500x500")

#ラベル
test_label = tkinter.Label(text='test', foreground='#0000ff')
test_label.pack()

#入力ボックス
entry_box = tkinter.Entry(width=50)
entry_box.insert(tkinter.END, "ここに入力してね")
#↑入力ボックスの中に最初から文字列を入れておく場合
entry_box.pack()

#入力ボックスの中身の取得、削除
# print(entry_box.get())
# entry_box.delete(0, tkinter.END)

def delete_value(event):
    '''ボタンを押した時に実行される'''
    entry_box.delete(0, tkinter.END)

button = tkinter.Button(text="ボタンだよ", width=20)
#<Button-1>...左クリック
button.bind("<Button-1>", delete_value)
button.pack()

#ウィンドウ状態の維持
root.mainloop()
