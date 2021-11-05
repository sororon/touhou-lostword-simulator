import tkinter as tk

WIDTH = 960
HEIGHT = 540
BTN_W = 8
BTN_H = 1

shop_dict = {
    "back": "　↩　",
    "saisen": "賽銭交換",
    "tally": "割符交換",
}

""" ショップ管理クラス """
class ShopManager:
    # コンストラクタ
    def __init__(self):
        # ウィンドウの上に被せてる？
        self.dialog = tk.Frame(width=WIDTH, height=HEIGHT)
        self.dialog.place(x=0, y=0)
        # キャンバス作成
        self.canvas = tk.Canvas(self.dialog, width=WIDTH, height=HEIGHT)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")
        # ボタン作成
        self.saisen_btn = tk.Button(self.dialog, width=BTN_W, height=BTN_H, text=shop_dict["saisen"])
        self.saisen_btn.place(x=WIDTH-840, y=HEIGHT-120)
        self.saisen_btn.bind("<ButtonPress>", self.click_button)
        self.tally_btn = tk.Button(self.dialog, width=BTN_W, height=BTN_H, text=shop_dict["tally"])
        self.tally_btn.place(x=WIDTH-700, y=HEIGHT-120)
        self.tally_btn.bind("<ButtonPress>", self.click_button)
        self.back_btn = tk.Button(self.dialog, width=BTN_W-2, height=BTN_H+1, text=shop_dict["back"])
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
        if TEXT == shop_dict["back"]:
            self.dialog.place_forget()
        elif TEXT == shop_dict["saisen"]:
            self.back_btn["state"] = "normal"
            self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="brown")
        elif TEXT == shop_dict["tally"]:
            self.back_btn["state"] = "normal"
            self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="blue")
