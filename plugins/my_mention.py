from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import json
import pandas as pd
import datetime

@respond_to('今週')
def mention_func(message):
    name = ["小原","梶野","金森"]
    name_num = random.randrange(len(name)-1)
    message.reply(name[name_num]+"さんです")

@listen_to('Slackbot')
def listen_func(message):
    message.send('こんにちは！')
    message.reply('どうしたに？')

#ユーザーIDでメンション
@respond_to('大谷')
def otani_func(message):
    user = 'U029PMBLVE3'

#json形式のメッセージ
@respond_to('朝掃除')
def reply_hello(message):
    attachments = [
        {
            'color': "#FF8000",
            'fields': [
                {'title': "時間", 'value': "10:30", 'short': True},
                {'title': "担当", 'value': "金曜担当", 'short': True},
            ]
        }
    ]
    message.send_webapi('朝掃除', json.dumps(attachments))

#現在の当番の人をプリントする
@respond_to('今'+'当番')
def toban_func(message):
    #Excelのシートをインポート
    df_sheet2 = pd.read_excel('excel_file/test.xlsx', sheet_name='Sheet2')
    #今日の日付をシリアル値に変える
    dt = datetime.date.today() - datetime.date(1899, 12, 31)
    today_serial = dt.days + 1
    #当番の日付が今日に合致したら、当番の人をプリントする
    for n in range(0, len(df_sheet2['name'])-1):
        start = df_sheet2['start'][n]
        end = df_sheet2['end'][n]
        if start <= today_serial <= end:
            message.send(df_sheet2['name'][n])
        else:
            pass
            
