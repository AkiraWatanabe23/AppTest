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
entry_box.insert(tkinter.END, "ここに文字列入れてね")
entry_box.pack()

#ウィンドウ状態の維持
root.mainloop()
