import tkinter as tk
import character

# モジュールの読み込み（画面を表示しないもの）
reimu = character.Reimu()
marisa = character.Marisa()
sizuha = character.Sizuha()
minoriko = character.Minoriko()
yamame = character.Yamame()

# 定数
WIDTH = 960
HEIGHT = 540
BTN_W = 8
BTN_H = 1

def player_label():
	player_lbl = tk.Button(width=16, height=1, text="プレイヤー　Lv."+str(100))
	player_lbl.place(x=WIDTH-950, y=HEIGHT-530)
	player_lbl["state"] = "disabled"

def reiryoku_label(item):
	reiryoku_lbl = tk.Button(width=10, height=1, text=item.show_item())
	reiryoku_lbl.place(x=WIDTH-510, y=HEIGHT-530)
	reiryoku_lbl["state"] = "disabled"

def saisen_label(item):
	saisen_lbl = tk.Button(width=10, height=1, text=item.show_item())
	saisen_lbl.place(x=WIDTH-340, y=HEIGHT-530)
	saisen_lbl["state"] = "disabled"

def crystal_label(item):
	crystal_lbl = tk.Button(width=10, height=1, text=item.show_item())
	crystal_lbl.place(x=WIDTH-170, y=HEIGHT-530)
	crystal_lbl["state"] = "disabled"

# キャラクター変更時、変数reimuを変更
def character_area(name_lbl):
	name_lbl["text"] = reimu.get_name()
	return tk.PhotoImage(width=600, height=600, file=reimu.img_nomal)
