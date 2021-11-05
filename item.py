import tkinter as tk

# アイテムの親クラス
class Item:
    # コンストラクタ
    def __new__(cls):
        obj = super().__new__(cls)
        return obj
    # アイテム名の取得
    def get_name(self):
        return self.name
    # アイテム数の取得
    def get_count(self):
        return self.count
    # valueの数だけitemのcountを増減
    def transfer_item(self, value):
        self.count += value
        return
    def show_item(self):
        txt = str(self.get_name())+"："+str(self.get_count())
        return txt

# 霊力クラス
class Reiryoku(Item):
    def __init__(self):
        self.name = "霊力"
        self.count = 10000

# 賽銭クラス
class Saisen(Item):
    def __init__(self):
        self.name = "賽銭"
        self.count = 30000

# 封結晶クラス
class Crystal(Item):
    def __init__(self):
        self.name = "封結晶"
        self.count = 100
