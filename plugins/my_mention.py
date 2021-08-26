from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random

@respond_to('今週')
def mention_func(message):
    name = ["小原","梶野","金森"]
    name_num = random.randrange(len(name)-1)
    message.reply(name[name_num]+"さんです")

@listen_to('listen')
def listen_func(message):
    message.send('Looks like someone posted a listen')
    message.reply('Are you?')

@respond_to('cool')
def cool_func(message):
    message.reply('Thank you, put stamp')
    message.react('+1')
