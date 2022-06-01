import tkinter
from tkinter import ttk
import itertools
import configparser
import pyodbc
import configparser
import xmltodict
import requests as rq
import json

#JANだとセットが出ない
#サイズ違いの同じシリーズ
#調べるとしたら一個ずつなげる

class MakeWherePhraseQuery():
    def __init__(self):

        config = configparser.ConfigParser()
        config.read(r'c:\Projects\SystemTools/config.ini  ', encoding='utf-8')

        server = config['PRODUCTION']['db_server']
        database = config['PRODUCTION']['database']
        username = config['PRODUCTION']['db_user_name']
        password = config['PRODUCTION']['db_password']

        self.con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                        server+';DATABASE='+database+';UID='+username+';PWD=' + password)

        self.cursor = self.con.cursor()

    def main(self, where_phrase):

        try:
            #出力内容初期化
            message.delete("1.0", "end")

            #入力内容取得
            codes = input.get("1.0", "end -1c")
            codes_array = codes.splitlines()

            if not codes_array:
                self.outputItemInfo("該当商品が見つかりませんでした。")

            #print('foreach----------------------------------------------') #test
            code_query = '('
            count = 0
            for code in codes_array:
                if not count == 0:
                    code_query += ',' 
                code_query = code_query + "'" + str(code) + "'"
                count += 1
            code_query = code_query + ')'
            self.outputItemInfo(code_query)
        except Exception as error :
            self.outputItemInfo(f"エラーが発生しました。エラー内容: {error}")

    def outputItemInfo(self, text):
        #where_phrase.set(text)
        message.insert('end', text)

########################################################################
###########フロント
###########################################################################
price_checker = MakeWherePhraseQuery()

root = tkinter.Tk()
root.title("MakeWherePhraseQuery")
root.geometry("700x700")

where_phrase = tkinter.StringVar()
where_phrase.set("出力箇所")

title_label = tkinter.Label(root,text="Codes")
title_label.pack()

input = tkinter.Text(width="30", height="10")
input.pack()

button = tkinter.Button(root, text="Make", command=lambda:price_checker.main(where_phrase))
button.pack(pady=20)

where_phrase_label = tkinter.Label(root,text="Where Phrase")
where_phrase_label.pack()

message = tkinter.Text(root)
message.pack()

root.mainloop()