import tkinter as tk
import item
import random
import home

# アイテムモジュールの読み込み
reiryoku = item.Reiryoku()
saisen = item.Saisen()
crystal = item.Crystal()

WIDTH = 960
HEIGHT = 540
BTN_W = 8
BTN_H = 1

facility_dict = {
    "back": "　↩　",
    "shrine": "おやしろ",
    "offertory_box": "賽銭箱",
    "temple_school": "寺子屋",
    "dojo": "道場",
}

def add_item():
    return random.randint(1, 10)

""" 施設管理クラス """
class FacilityManager:
    # コンストラクタ
    def __init__(self):
        self.reiryoku_count = 0
        self.saisen_count = 0
        self.dialog = tk.Frame(width=WIDTH, height=HEIGHT)
        self.dialog.place(x=0, y=0)
        # キャンバス作成
        self.canvas = tk.Canvas(self.dialog, width=WIDTH, height=HEIGHT)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="gray")
        # ボタン作成
        self.back_btn = tk.Button(self.dialog, width=BTN_W-2, height=BTN_H+1, text=facility_dict["back"])
        self.back_btn.place(x=WIDTH-WIDTH, y=HEIGHT-HEIGHT)
        self.back_btn.bind("<ButtonPress>", self.click_button)
        self.shrine_btn = tk.Button(self.dialog, width=BTN_W, height=BTN_H+5, text=facility_dict["shrine"])
        self.shrine_btn.place(x=WIDTH-800, y=0)
        self.shrine_btn.bind("<ButtonPress>", self.click_button)
        self.offertory_box_btn = tk.Button(self.dialog, width=BTN_W, height=BTN_H+5, text=facility_dict["offertory_box"])
        self.offertory_box_btn.place(x=WIDTH-600, y=0)
        self.offertory_box_btn.bind("<ButtonPress>", self.click_button)
        self.temple_school_btn = tk.Button(self.dialog, width=BTN_W, height=BTN_H+6, text=facility_dict["temple_school"])
        self.temple_school_btn.place(x=WIDTH-400, y=0)
        self.temple_school_btn.bind("<ButtonPress>", self.click_button)
        self.dojo_btn = tk.Button(self.dialog, width=BTN_W, height=BTN_H+6, text=facility_dict["dojo"])
        self.dojo_btn.place(x=WIDTH-200, y=0)
        self.dojo_btn.bind("<ButtonPress>", self.click_button)
        # ラベルテキスト作成
        self.shrine_lbl_txt = tk.StringVar(self.dialog)
        self.shrine_lbl_txt.set("+"+str(add_item()))
        self.offertory_box_lbl_txt = tk.StringVar(self.dialog)
        self.offertory_box_lbl_txt.set("+"+str(add_item()))
        # ラベル作成
        self.shrine_lbl= tk.Label(self.dialog, textvariable=self.shrine_lbl_txt, width=BTN_W, height=1)
        self.shrine_lbl.place(x=WIDTH-800, y=200)
        self.offertory_box_lbl= tk.Label(self.dialog, textvariable=self.offertory_box_lbl_txt, width=BTN_W, height=1)
        self.offertory_box_lbl.place(x=WIDTH-600, y=200)
        # 非表示
        self.dialog.place_forget()
        #アイテムの増加
        self.dialog.after(1000, self.increase_item)
        #self.dialog.after(1000, self.increase_item(saisen))

    # ウィンドウの表示
    def show_window(self):
        self.dialog.place(x=0, y=300)

    # ボタンが押された時に実行する処理
    def click_button(self, event):
        TEXT = event.widget.cget("text")
        if TEXT == facility_dict["back"]:
            self.dialog.place_forget()
        elif TEXT == facility_dict["shrine"]:
            reiryoku.transfer_item(self.reiryoku_count) # <--- アイテムの入手
            #print("+: ", self.reiryoku_count)
            #print("now_reiryoku: ", reiryoku.get_count())

            """ここで呼び出すと他の画面でも常に霊力ラベル（押せないボタン）が表示されてしまう"""
            home.reiryoku_label(reiryoku)
            
            self.reiryoku_count = 0
            self.shrine_lbl_txt.set("+"+str(self.reiryoku_count))
        elif TEXT == facility_dict["offertory_box"]:
            saisen.transfer_item(self.saisen_count) # <--- アイテムの入手
            #print("+: ", self.saisen_count)
            #print("now_saisen: ", saisen.get_count())
            home.saisen_label(saisen)
            self.saisen_count = 0
            self.offertory_box_lbl_txt.set("+"+str(self.saisen_count))
        else:
            pass

    def check_increase_limit(self, item_cnt):
        if item_cnt > 99:
            return False
        return True

    def increase_item(self):
        if self.check_increase_limit(self.reiryoku_count):
            self.reiryoku_count += 1
            self.shrine_lbl_txt.set("+"+str(self.reiryoku_count))
        if self.check_increase_limit(self.saisen_count):
            self.saisen_count += 2
            self.offertory_box_lbl_txt.set("+"+str(self.saisen_count))
        self.dialog.after(1000, self.increase_item)
