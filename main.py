import tkinter as tk
import random
import time
import shop
import friend
import card
import facility
import task
import pray
import quest
import mission
import formation
import tower
import item
import character
import home

# アイテムモジュールの読み込み
reiryoku = item.Reiryoku()
saisen = item.Saisen()
crystal = item.Crystal()

# ボタンが押された時に実行する処理
def click_button(event):
    #! 引数eventにはクリックされたボタンの情報が入っている
    TEXT = event.widget.cget("text")
    if TEXT == scene_dict["shop"]:
        shopmanager.show_window()
    elif TEXT == scene_dict["friend"]:
        friendmanager.show_window()
    elif TEXT == scene_dict["card"]:
        cardmanager.show_window()
    elif TEXT == scene_dict["facility"]:
        facilitymanager.show_window()
    else:
        pass

# メッセージをランダムで表示(別ファイルへ移動予定)
def show_message():
    _x = random.randint(1, 6)
    if _x == 1:
        message["text"] = message_dict["hello1"]
    elif _x == 2:
        message["text"] = message_dict["intro1"]
    elif _x == 3:
        message["text"] = message_dict["intro2"]
    elif _x == 4:
        message["text"] = message_dict["intro3"]
    elif _x == 5:
        message["text"] = message_dict["intro4"]
    else:
        message["text"] = message_dict["hello2"]
    #! 5000ms = 5sに第二引数の関数を実行
    window.after(5000, show_message)

# シーンの辞書
scene_dict = {
    "shop": "ショップ",
    "friend": "仲間",
    "card": "絵札",
    "facility": "施設",
    "task": "課題",
    "pray": "おいのり",
    "quest": "探索",
    "mission": "おつかい",
    "formation": "編成",
    "tower": "紅魔塔",
    "config": "設定"
}

# セリフの辞書(別ファイルへ移動予定)
message_dict = {
    "hello1": "おはよう！今日も一日頑張ろう！",
    "hello2": "来たね！今日は何からしよっか？",
    "intro1": "ショップモードでは賽銭を使って買い物ができるよ！",
    "intro2": "仲間モードではあなたの仲間が確認できるよ！",
    "intro3": "絵札モードではあなたが持っている絵札を確認できるよ！",
    "intro4": "施設モードでは育成に役立つ施設を利用することができるよ！",
}

# 定数
WIDTH = 960
HEIGHT = 540
BTN_W = 8
BTN_H = 1

# ウィンドウ作成
window = tk.Tk()
window.title("東方LW")
#window.geometry("960*540+200+100") #! ウィンドウの初期幅高さ、位置
window.minsize(WIDTH, HEIGHT)
window.maxsize(WIDTH*2, HEIGHT*2)
#window.resizable(True, False)      #! ウィンドウの幅高さ変更可能か否か
window.option_add("*font", ["MS Pゴシック", 22])

# キャンバス作成
canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.place(x=0, y=0)
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="gray")

# ボタン作成
shop_btn = tk.Button(width=BTN_W, height=BTN_H, text=scene_dict["shop"])
shop_btn.place(x=WIDTH-WIDTH, y=HEIGHT-60)
shop_btn.bind("<ButtonPress>", click_button)
friend_btn = tk.Button(width=BTN_W, height=BTN_H, text=scene_dict["friend"])
friend_btn.place(x=WIDTH-820, y=HEIGHT-60)
friend_btn.bind("<ButtonPress>", click_button)
card_btn = tk.Button(width=BTN_W, height=BTN_H, text=scene_dict["card"])
card_btn.place(x=WIDTH-680, y=HEIGHT-60)
card_btn.bind("<ButtonPress>", click_button)
facility_btn = tk.Button(width=BTN_W, height=BTN_H, text=scene_dict["facility"])
facility_btn.place(x=WIDTH-540, y=HEIGHT-60)
facility_btn.bind("<ButtonPress>", click_button)
task_btn = tk.Button(width=BTN_W, height=BTN_H, text=scene_dict["task"])
task_btn.place(x=WIDTH-400, y=HEIGHT-60)
task_btn.bind("<ButtonPress>", click_button)
pray_btn = tk.Button(width=BTN_W, height=BTN_H, text=scene_dict["pray"])
pray_btn.place(x=WIDTH-260, y=HEIGHT-60)
pray_btn.bind("<ButtonPress>", click_button)
quest_btn = tk.Button(width=BTN_W-1, height=BTN_H+2, text=scene_dict["quest"])
quest_btn.place(x=WIDTH-120, y=HEIGHT-120)
quest_btn.bind("<ButtonPress>", click_button)
mission_btn = tk.Button(width=BTN_W-1, height=BTN_H+1, text=scene_dict["mission"])
mission_btn.place(x=WIDTH-120, y=HEIGHT-220)
mission_btn.bind("<ButtonPress>", click_button)
formation_btn = tk.Button(width=BTN_W-1, height=BTN_H+1, text=scene_dict["formation"])
formation_btn.place(x=WIDTH-250, y=HEIGHT-150)
formation_btn.bind("<ButtonPress>", click_button)
tower_btn = tk.Button(width=BTN_W-1, height=BTN_H+1, text=scene_dict["tower"])
tower_btn.place(x=WIDTH-250, y=HEIGHT-240)
tower_btn.bind("<ButtonPress>", click_button)
config_btn = tk.Button(width=BTN_W-1, height=BTN_H+1, text=scene_dict["config"])
config_btn.place(x=WIDTH-WIDTH, y=HEIGHT-460)
config_btn.bind("<ButtonPress>", click_button)

# ラベル作成
home.player_label()
home.reiryoku_label(reiryoku)
home.saisen_label(saisen)
home.crystal_label(crystal)
# ホーム画面のキャラクターの名前
name_lbl = tk.Label(width=10, height=1)
name_lbl.place(x=10, y=300)
# ホーム画面の画像読み込み
home_image = home.character_area(name_lbl)
canvas.create_image(400, HEIGHT//2, image=home_image)

# メッセージエリア
message = tk.Label(width=43, height=4, wraplength=700,
    bg="white", justify="left", anchor="nw")
message.place(x=10, y=340)
message["text"] = "おはよう！今日も一日頑張ろう！"
window.after(5000, show_message)

# 画面表示を伴うモジュールの読み込み
shopmanager = shop.ShopManager()
friendmanager = friend.FriendManager()
cardmanager = card.CardManager()
facilitymanager = facility.FacilityManager()

# メインループ（ウィンドウ表示）
window.mainloop()
