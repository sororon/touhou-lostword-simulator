import tkinter as tk

WIDTH = 960
HEIGHT = 540
BTN_W = 8
BTN_H = 1

card_dict = {
    "back": "　↩　",
}

""" 絵札管理クラス """
class CardManager:
    # コンストラクタ
    def __init__(self):
        self.dialog = tk.Frame(width=WIDTH, height=HEIGHT)
        self.dialog.place(x=0, y=0)
        # キャンバス作成
        self.canvas = tk.Canvas(self.dialog, width=WIDTH, height=HEIGHT)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="orange")
        # ボタン作成
        self.back_btn = tk.Button(self.dialog, width=BTN_W-2, height=BTN_H+1, text=card_dict["back"])
        self.back_btn.place(x=WIDTH-WIDTH, y=HEIGHT-HEIGHT)
        self.back_btn.bind("<ButtonPress>", self.click_button)
        # 非表示
        self.dialog.place_forget()

    # ウィンドウの表示
    def show_window(self):
        self.dialog.place(x=0, y=0)

    # ボタンが押された時に実行する処理
    def click_button(self, event):
        TEXT = event.widget.cget("text")
        if TEXT == card_dict["back"]:
            self.dialog.place_forget()
        else:
            pass
