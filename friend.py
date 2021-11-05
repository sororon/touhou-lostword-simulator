import tkinter as tk
import character

WIDTH = 960
HEIGHT = 540
CARD_W = 290
CARD_H = 290
BTN_W = 8
BTN_H = 1
LBL_W = 6

# キャラクタークラスの読み込み
defalut = character.Defalut()
reimu = character.Reimu()
marisa = character.Marisa()
rumia = character.Rumia()
cirno = character.Cirno()
patchouli = character.Patchouli()
sakuya = character.Sakuya()
remiria = character.Remiria()
fran = character.Fran()
tyen = character.Tyen()
arice = character.Arice()
yomu = character.Yomu()
yuyuko = character.Yuyuko()
ran = character.Ran()
yukari = character.Yukari()
keine = character.Keine()
tei = character.Tei()
udonge = character.Udonge()
eirin = character.Eirin()
kaguya = character.Kaguya()
mokou = character.Mokou()
minoriko = character.Minoriko()
sizuha = character.Sizuha()
hina = character.Hina()
nitori = character.Nitori()
sanae = character.Sanae()
suwako = character.Suwako()
yamame = character.Yamame()
#print(minoriko.get_name())
#print(character.Minoriko().name)

def show_status(chara):
    return "HP: "+str(chara.culc_hp(0, 0))+"\natk: "+str(chara.get_atk())+"\ndfs: "+str(chara.get_dfs())+"\nspd: "+str(chara.get_spd())

friend_dict = {
    "back": "　↩　",
    "reimu": reimu.get_name(),
    "marisa": marisa.get_name(),
    "sizuha": sizuha.get_name(),
    "minoriko": minoriko.get_name(),
}

""" 仲間管理クラス """
class FriendManager:
    # コンストラクタ
    def __init__(self):
        self.dialog = tk.Frame(width=WIDTH, height=HEIGHT)
        self.dialog.place(x=0, y=0)
        # キャンバス作成
        self.canvas = tk.Canvas(self.dialog, width=WIDTH, height=HEIGHT)
        #, scrollregion=(-1200, -1100, 1800, 1600)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")
        # キャラクター表示用キャンバス
        self.img_canvas = tk.Canvas(self.dialog, width=CARD_W, height=CARD_H)
        self.img_canvas.place(x=660, y=50)
        # ボタン作成
        self.back_btn = tk.Button(self.dialog, width=BTN_W-2, height=BTN_H+1, text=friend_dict["back"])
        self.back_btn.place(x=WIDTH-WIDTH, y=HEIGHT-HEIGHT)
        self.back_btn.bind("<ButtonPress>", self.click_button)
        # ラベルテキスト作成
        self.fullname_lbl_txt = tk.StringVar(self.dialog)
        self.fullname_lbl_txt.set(reimu.get_fullname())
        self.status_lbl_txt = tk.StringVar(self.dialog)
        self.status_lbl_txt.set("HP:\n攻撃:\n防御:\n速さ:")
        self.avility_lbl_txt = tk.StringVar(self.dialog)
        self.avility_lbl_txt.set("card1:\ncard2:")
        # フルネーム表示ラベル
        self.fullname_lbl= tk.Label(self.dialog, textvariable=self.fullname_lbl_txt, width=18, height=1)
        self.fullname_lbl.place(x=660, y=350)
        # ステータス表示ラベル
        self.status_lbl = tk.Label(self.dialog, textvariable=self.status_lbl_txt, width=10, height=5)
        self.status_lbl.place(x=660, y=380)
        # スペカ表示ラベル
        self.avility_lbl = tk.Label(self.dialog, textvariable=self.avility_lbl_txt, width=10, height=5)
        self.avility_lbl.place(x=810, y=380)
        # キャラクター選択ボタン
        self.ab_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=reimu.get_name())
        self.ab_btn.place(x=110, y=30)
        self.ab_btn.bind("<ButtonPress>", self.click_button)
        self.ac_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=marisa.get_name())
        self.ac_btn.place(x=220, y=30)
        self.ac_btn.bind("<ButtonPress>", self.click_button)
        self.ba_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=rumia.get_name())
        self.ba_btn.place(x=0, y=90)
        self.ba_btn.bind("<ButtonPress>", self.click_button)
        self.bb_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=cirno.get_name())
        self.bb_btn.place(x=110, y=90)
        self.bb_btn.bind("<ButtonPress>", self.click_button)
        self.bc_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=patchouli.get_name())
        self.bc_btn.place(x=220, y=90)
        self.bc_btn.bind("<ButtonPress>", self.click_button)
        self.bd_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=sakuya.get_name())
        self.bd_btn.place(x=330, y=90)
        self.bd_btn.bind("<ButtonPress>", self.click_button)
        self.be_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=remiria.get_name())
        self.be_btn.place(x=440, y=90)
        self.be_btn.bind("<ButtonPress>", self.click_button)
        self.bf_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=fran.get_name())
        self.bf_btn.place(x=550, y=90)
        self.bf_btn.bind("<ButtonPress>", self.click_button)
        self.ca_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=tyen.get_name())
        self.ca_btn.place(x=0, y=150)
        self.ca_btn.bind("<ButtonPress>", self.click_button)
        self.cb_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=arice.get_name())
        self.cb_btn.place(x=110, y=150)
        self.cb_btn.bind("<ButtonPress>", self.click_button)
        self.cc_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=yomu.get_name())
        self.cc_btn.place(x=220, y=150)
        self.cc_btn.bind("<ButtonPress>", self.click_button)
        self.cd_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=yuyuko.get_name())
        self.cd_btn.place(x=330, y=150)
        self.cd_btn.bind("<ButtonPress>", self.click_button)
        self.ce_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=ran.get_name())
        self.ce_btn.place(x=440, y=150)
        self.ce_btn.bind("<ButtonPress>", self.click_button)
        self.cf_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=yukari.get_name())
        self.cf_btn.place(x=550, y=150)
        self.cf_btn.bind("<ButtonPress>", self.click_button)
        self.da_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=keine.get_name())
        self.da_btn.place(x=0, y=210)
        self.da_btn.bind("<ButtonPress>", self.click_button)
        self.db_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=tei.get_name())
        self.db_btn.place(x=110, y=210)
        self.db_btn.bind("<ButtonPress>", self.click_button)
        self.dc_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=udonge.get_name())
        self.dc_btn.place(x=220, y=210)
        self.dc_btn.bind("<ButtonPress>", self.click_button)
        self.dd_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=eirin.get_name())
        self.dd_btn.place(x=330, y=210)
        self.dd_btn.bind("<ButtonPress>", self.click_button)
        self.de_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=kaguya.get_name())
        self.de_btn.place(x=440, y=210)
        self.de_btn.bind("<ButtonPress>", self.click_button)
        self.df_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=mokou.get_name())
        self.df_btn.place(x=550, y=210)
        self.df_btn.bind("<ButtonPress>", self.click_button)
        self.ea_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=sizuha.get_name())
        self.ea_btn.place(x=0, y=270)
        self.ea_btn.bind("<ButtonPress>", self.click_button)
        self.eb_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=minoriko.get_name())
        self.eb_btn.place(x=110, y=270)
        self.eb_btn.bind("<ButtonPress>", self.click_button)
        self.ec_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=hina.get_name())
        self.ec_btn.place(x=220, y=270)
        self.ec_btn.bind("<ButtonPress>", self.click_button)
        self.ed_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=nitori.get_name())
        self.ed_btn.place(x=330, y=270)
        self.ed_btn.bind("<ButtonPress>", self.click_button)
        self.ee_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=sanae.get_name())
        self.ee_btn.place(x=440, y=270)
        self.ee_btn.bind("<ButtonPress>", self.click_button)
        self.ef_btn = tk.Button(self.dialog, width=LBL_W, height=BTN_H, text=suwako.get_name())
        self.ef_btn.place(x=550, y=270)
        self.ef_btn.bind("<ButtonPress>", self.click_button)
        # 非表示
        self.dialog.place_forget()

    # ウィンドウの表示
    def show_window(self):
        self.dialog.place(x=0, y=0)

    # ボタンが押された時に実行する処理
    def click_button(self, event):
        #前にクリックされた画像の上に上書きする白いダミー画像
        img_chara = defalut.get_face_image("defalut")
        self.img_canvas.create_image(160, 160, image=img_chara)
        TEXT = event.widget.cget("text")
        if TEXT == friend_dict["back"]:
            self.dialog.place_forget()
        elif TEXT == reimu.get_name():
            img_chara = reimu.get_face_image("reimu")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(reimu.get_fullname())
            self.status_lbl_txt.set(show_status(reimu))
            #self.avility_lbl_txt.set(reimu.get_fullname())
        elif TEXT == marisa.get_name():
            img_chara = marisa.get_face_image("marisa")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(marisa.get_fullname())
            self.status_lbl_txt.set(show_status(marisa))
            #self.avility_lbl_txt.set(marisa.get_fullname())
        elif TEXT == rumia.get_name():
            img_chara = rumia.get_face_image("rumia")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(rumia.get_fullname())
            self.status_lbl_txt.set(show_status(rumia))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == cirno.get_name():
            img_chara = cirno.get_face_image("cirno")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(cirno.get_fullname())
            self.status_lbl_txt.set(show_status(cirno))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == patchouli.get_name():
            img_chara = patchouli.get_face_image("patchouli")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(patchouli.get_fullname())
            self.status_lbl_txt.set(show_status(patchouli))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == sakuya.get_name():
            img_chara = sakuya.get_face_image("sakuya")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(sakuya.get_fullname())
            self.status_lbl_txt.set(show_status(sakuya))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == remiria.get_name():
            img_chara = remiria.get_face_image("remiria")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(remiria.get_fullname())
            self.status_lbl_txt.set(show_status(remiria))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == fran.get_name():
            img_chara = fran.get_face_image("fran")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(fran.get_fullname())
            self.status_lbl_txt.set(show_status(fran))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == tyen.get_name():
            img_chara = tyen.get_face_image("tyen")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(tyen.get_fullname())
            self.status_lbl_txt.set(show_status(tyen))
            #self.avility_lbl_txt.set(tyen.get_fullname())
        elif TEXT == arice.get_name():
            img_chara = arice.get_face_image("arice")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(arice.get_fullname())
            self.status_lbl_txt.set(show_status(arice))
            #self.avility_lbl_txt.set(arice.get_fullname())
        elif TEXT == yomu.get_name():
            img_chara = yomu.get_face_image("yomu")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(yomu.get_fullname())
            self.status_lbl_txt.set(show_status(yomu))
            #self.avility_lbl_txt.set(yomu.get_fullname())
        elif TEXT == yuyuko.get_name():
            img_chara = yuyuko.get_face_image("yuyuko")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(yuyuko.get_fullname())
            self.status_lbl_txt.set(show_status(yuyuko))
            #self.avility_lbl_txt.set(yuyuko.get_fullname())
        elif TEXT == ran.get_name():
            img_chara = ran.get_face_image("ran")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(ran.get_fullname())
            self.status_lbl_txt.set(show_status(ran))
            #self.avility_lbl_txt.set(ran.get_fullname())
        elif TEXT == yukari.get_name():
            img_chara = yukari.get_face_image("yukari")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(yukari.get_fullname())
            self.status_lbl_txt.set(show_status(yukari))
            #self.avility_lbl_txt.set(yukari.get_fullname())
        elif TEXT == tei.get_name():
            img_chara = tei.get_face_image("tei")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(tei.get_fullname())
            self.status_lbl_txt.set(show_status(tei))
            #self.avility_lbl_txt.set(tei.get_fullname())
        elif TEXT == keine.get_name():
            img_chara = keine.get_face_image("keine")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(keine.get_fullname())
            self.status_lbl_txt.set(show_status(keine))
            #self.avility_lbl_txt.set(keine.get_fullname())
        elif TEXT == udonge.get_name():
            img_chara = udonge.get_face_image("udonge")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(udonge.get_fullname())
            self.status_lbl_txt.set(show_status(udonge))
            #self.avility_lbl_txt.set(udonge.get_fullname())
        elif TEXT == eirin.get_name():
            img_chara = eirin.get_face_image("eirin")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(eirin.get_fullname())
            self.status_lbl_txt.set(show_status(eirin))
            #self.avility_lbl_txt.set(eirin.get_fullname())
        elif TEXT == kaguya.get_name():
            img_chara = kaguya.get_face_image("kaguya")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(kaguya.get_fullname())
            self.status_lbl_txt.set(show_status(kaguya))
            #self.avility_lbl_txt.set(kaguya.get_fullname())
        elif TEXT == mokou.get_name():
            img_chara = mokou.get_face_image("mokou")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(mokou.get_fullname())
            self.status_lbl_txt.set(show_status(mokou))
            #self.avility_lbl_txt.set(mokou.get_fullname())
        elif TEXT == sizuha.get_name():
            img_chara = sizuha.get_face_image("sizuha")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(sizuha.get_fullname())
            self.status_lbl_txt.set(show_status(sizuha))
            #self.avility_lbl_txt.set(sizuha.get_fullname())
        elif TEXT == minoriko.get_name():
            img_chara = minoriko.get_face_image("minoriko")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(minoriko.get_fullname())
            self.status_lbl_txt.set(show_status(minoriko))
            #self.avility_lbl_txt.set(minoriko.get_fullname())
        elif TEXT == hina.get_name():
            img_chara = hina.get_face_image("hina")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(hina.get_fullname())
            self.status_lbl_txt.set(show_status(hina))
            #self.avility_lbl_txt.set(hina.get_fullname())
        elif TEXT == nitori.get_name():
            img_chara = nitori.get_face_image("nitori")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(nitori.get_fullname())
            self.status_lbl_txt.set(show_status(nitori))
            #self.avility_lbl_txt.set(nitori.get_fullname())
        elif TEXT == sanae.get_name():
            img_chara = sanae.get_face_image("sanae")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(sanae.get_fullname())
            self.status_lbl_txt.set(show_status(sanae))
            #self.avility_lbl_txt.set(sanae.get_fullname())
        elif TEXT == suwako.get_name():
            img_chara = suwako.get_face_image("suwako")
            self.img_canvas.create_image(160, 160, image=img_chara)
            self.fullname_lbl_txt.set(suwako.get_fullname())
            self.status_lbl_txt.set(show_status(suwako))
            #self.avility_lbl_txt.set(suwako.get_fullname())
        else:
            pass
