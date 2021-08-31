from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
import json

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
