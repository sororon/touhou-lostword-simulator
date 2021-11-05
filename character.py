import tkinter as tk
import random
import time

face_dict = {
    "defalut": "img/dummy-face.png",
    "reimu": "img/reimu-face.png",
    "marisa": "img/marisa-face.png",
    "rumia": "img/rumia-face.png",
    "cirno": "img/cirno-face.png",
    "patchouli": "img/patchouli-face.png",
    "sakuya": "img/sakuya-face.png",
    "remiria": "img/remiria-face.png",
    "fran": "img/fran-face.png",
    "sizuha": "img/sizuha-face.png",
    "minoriko": "img/minoriko-face.png",
    "hina": "img/hina-face.png",
    "nitori": "img/nitori-face.png",
    "sanae": "img/sanae-face.png",
    "suwako": "img/suwako-face.png",
    "tyen": "img/tyen-face.png",
    "arice": "img/arice-face.png",
    "yomu": "img/yomu-face.png",
    "yuyuko": "img/yuyuko-face.png",
    "ran": "img/ran-face.png",
    "yukari": "img/yukari-face.png",
    "keine": "img/keine-face.png",
    "tei": "img/tei-face.png",
    "udonge": "img/udonge-face.png",
    "eirin": "img/eirin-face.png",
    "kaguya": "img/kaguya-face.png",
    "mokou": "img/mokou-face.png",
}

# キャラクターの親クラス
class Character:
    # コンストラクタ
    def __new__(cls):
        obj = super().__new__(cls)
        obj.rsv = 1
        return obj

    # 画像の読み込み
    def get_face_image(self, name):
        self.image = tk.PhotoImage(width=300, height=300, file=face_dict[name])
        #print(self.image.width(), self.image.height())
        return self.image

    # 力をためる
    def reserve(self):
        self.rsv = self.rsv + 1

    # 名前を求める
    def get_name(self):
        return self.name

    # フルネームを求める
    def get_fullname(self):
        return self.fullname

    # 攻撃力を求める
    def get_atk(self):
        r = self.rsv
        self.rsv = 1
        atk_t_e = random.randint(1, self.atk * r)
        #return atk_t_e
        return self.atk

    # 防御力を求める
    def get_dfs(self):
        dmg_from_e = random.randint(0, self.dfs)
        #return dmg_from_e
        return self.dfs

    # 素早さを求める
    def get_spd(self):
        return self.spd

    # 体力計算
    def culc_hp(self, atk, dfs):
        dmg = atk - dfs
        # ダメージなし
        if dmg < 1:
            return self.hp
        # 体力を減らす
        self.hp = self.hp - dmg
        if self.hp < 1:
            self.hp = 0
        return self.hp

class Defalut(Character):
    def __init__(self):
        pass

# 霊夢クラス
class Reimu(Character):
    def __init__(self):
        self.name = "霊夢"
        self.fullname = "博麗霊夢"
        self.img_nomal = "img/reimu/reimu_nomal.png"
        self.hp = 6650
        self.atk = (930+855)//2
        self.dfs = (1235+1190)//2
        self.spd = 910

# 魔理沙クラス
class Marisa(Character):
    def __init__(self):
        self.name = "魔理沙"
        self.fullname = "霧雨魔理沙"
        self.img_nomal = "img/marisa/marisa_nomal.png"
        self.hp = 5500
        self.atk = (1290+1200)//2
        self.dfs = (1010+930)//2
        self.spd = 920

# ルーミアクラス
class Rumia(Character):
    def __init__(self):
        self.name = "ルーミア"
        self.fullname = "ルーミア"
        self.hp = 4900
        self.atk = (670+1340)//2
        self.dfs = (620+1390)//2
        self.spd = 1000

# チルノクラス
class Cirno(Character):
    def __init__(self):
        self.name = "チルノ"
        self.fullname = "チルノ"
        self.hp = 5200
        self.atk = (1120+1170)//2
        self.dfs = (800+860)//2
        self.spd = 1010

# パチュリークラス
class Patchouli(Character):
    def __init__(self):
        self.name = "パチェ"
        self.fullname = "パチュリー・ノーレッジ"
        self.hp = 4200
        self.atk = (850+1380)//2
        self.dfs = (1280+900)//2
        self.spd = 1200

# 咲夜クラス
class Sakuya(Character):
    def __init__(self):
        self.name = "咲夜"
        self.fullname = "十六夜咲夜"
        self.hp = 4550
        self.atk = (1195+1105)//2
        self.dfs = (925+915)//2
        self.spd = 1400

# レミリアクラス
class Remiria(Character):
    def __init__(self):
        self.name = "レミリア"
        self.fullname = "レミリア・スカーレット"
        self.hp = 5000
        self.atk = (1000+1300)//2
        self.dfs = (880+1050)//2
        self.spd = 1220

# フランクラス
class Fran(Character):
    def __init__(self):
        self.name = "フラン"
        self.fullname = "フランドール・スカーレット"
        self.hp = 4850
        self.atk = (1180+1380)//2
        self.dfs = (890+950)//2
        self.spd = 1080

# 橙クラス
class Tyen(Character):
    def __init__(self):
        self.name = "橙"
        self.fullname = "橙"
        self.hp = 4500
        self.atk = (1220+880)//2
        self.dfs = (985+815)//2
        self.spd = 1200

# アリスクラス
class Arice(Character):
    def __init__(self):
        self.name = "アリス"
        self.fullname = "アリス・マーガトロイド"
        self.hp = 5350
        self.atk = (890+1080)//2
        self.dfs = (910+1220)//2
        self.spd = 1280

# 妖夢クラス
class Yomu(Character):
    def __init__(self):
        self.name = "妖夢"
        self.fullname = "魂魄妖夢"
        self.hp = 5050
        self.atk = (1160+1160)//2
        self.dfs = (940+940)//2
        self.spd = 1240

# 幽々子クラス
class Yuyuko(Character):
    def __init__(self):
        self.name = "幽々子"
        self.fullname = "西行寺幽々子"
        self.hp = 5350
        self.atk = (1380+1010)//2
        self.dfs = (1280+990)//2
        self.spd = 1170

# 藍クラス
class Ran(Character):
    def __init__(self):
        self.name = "藍"
        self.fullname = "八雲藍"
        self.hp = 5400
        self.atk = (1330+980)//2
        self.dfs = (1180+890)//2
        self.spd = 990

# 紫クラス
class Yukari(Character):
    def __init__(self):
        self.name = "紫"
        self.fullname = "八雲紫"
        self.hp = 7850
        self.atk = (930+840)//2
        self.dfs = (1390+1320)//2
        self.spd = 850

# 慧音クラス
class Keine(Character):
    def __init__(self):
        self.name = "慧音"
        self.fullname = "上白沢慧音"
        self.hp = 5500
        self.atk = (1200+800)//2
        self.dfs = (1425+1225)//2
        self.spd = 700

# てゐクラス
class Tei(Character):
    def __init__(self):
        self.name = "てゐ"
        self.fullname = "因幡てゐ"
        self.hp = 5150
        self.atk = (1210+1080)//2
        self.dfs = (965+1025)//2
        self.spd = 1140

# うどんげクラス
class Udonge(Character):
    def __init__(self):
        self.name = "うどんげ"
        self.fullname = "鈴仙・優曇華院・イナバ"
        self.hp = 5150
        self.atk = (1210+1080)//2
        self.dfs = (1025+965)//2
        self.spd = 1140

# 永琳クラス
class Eirin(Character):
    def __init__(self):
        self.name = "永琳"
        self.fullname = "八意永琳"
        self.hp = 8400
        self.atk = (1500+1220)//2
        self.dfs = (850+800)//2
        self.spd = 850

# 輝夜クラス
class Kaguya(Character):
    def __init__(self):
        self.name = "輝夜"
        self.fullname = "蓬莱山輝夜"
        self.hp = 5400
        self.atk = (1480+1390)//2
        self.dfs = (1010+950)//2
        self.spd = 990

# 妹紅クラス
class Mokou(Character):
    def __init__(self):
        self.name = "妹紅"
        self.fullname = "藤原妹紅"
        self.hp = 5800
        self.atk = (1310+820)//2
        self.dfs = (1050+1020)//2
        self.spd = 1090

# 静葉クラス
class Sizuha(Character):
    def __init__(self):
        self.name = "静葉"
        self.fullname = "秋静葉"
        self.img_nomal = "img/sizuha/sizuha-nomal.png"
        self.hp = 5500
        self.atk = (1050+1300)//2
        self.dfs = (1000+1150)//2
        self.spd = 850

# 穣子クラス
class Minoriko(Character):
    def __init__(self):
        self.name = "穣子"
        self.fullname = "秋穣子"
        self.img_nomal = "img/minoriko/minoriko-nomal.png"
        self.hp = 8100
        self.atk = (1100+1250)//2
        self.dfs = (750+900)//2
        self.spd = 830

# 雛クラス
class Hina(Character):
    def __init__(self):
        self.name = "雛"
        self.fullname = "鍵山雛"
        self.hp = 5800
        self.atk = (1300+1200)//2
        self.dfs = (900+1000)//2
        self.spd = 890

# にとりクラス
class Nitori(Character):
    def __init__(self):
        self.name = "にとり"
        self.fullname = "河城にとり"
        self.hp = 5300
        self.atk = (960+1120)//2
        self.dfs = (950+1030)//2
        self.spd = 1330

# 早苗クラス
class Sanae(Character):
    def __init__(self):
        self.name = "早苗"
        self.fullname = "東風谷早苗"
        self.hp = 8000
        self.atk = (1000+940)//2
        self.dfs = (985+945)//2
        self.spd = 980

# 諏訪子クラス
class Suwako(Character):
    def __init__(self):
        self.name = "諏訪子"
        self.fullname = "洩矢諏訪子"
        self.hp = 6150
        self.atk = (1200+1400)//2
        self.dfs = (1090+980)//2
        self.spd = 1000

# ヤマメクラス
class Yamame(Character):
    def __init__(self):
        self.name = "ヤマメ"
        self.fullname = "黒谷ヤマメ"
        self.img_nomal = "img/yamame/yamame-nomal.png"
        self.hp = 80
        self.atk = 120
        self.dfs = 40
        self.spd = 100

