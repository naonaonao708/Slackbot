from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

@respond_to('mention')
def mention_func(message):
    message.reply('How dare you call me a mention')

@listen_to('listen')
def listen_func(message):
    message.send('Looks like someone posted a listen')
    message.reply('Are you?')

@respond_to('cool')
def cool_func(message):
    message.reply('Thank you, put stamp')
    message.react('+1')
