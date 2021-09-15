from rivescript import RiveScript
import os.path

file = os.path.dirname(__file__)
brain = os.path.join(file,'brain')
bot = RiveScript(utf8=True)
bot.load_directory(brain)
bot.sort_replies()

#used to test the bot separately
'''
while True:
    msg = str(input("User: "))
    reply = str(bot.reply("localhost",msg))
    if msg == "quit":
        break
    else:
        print("Bot: "+ reply)
'''
