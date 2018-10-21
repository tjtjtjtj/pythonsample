import tkinter as tk

root = tk.Tk()
# ここにでウィンドウタイトルを設定する
root.title(u"ウインドウのタイトルを")

# ラベル
Static1 = tk.Label(text=u'test')
Static1.pack()
root.mainloop()
