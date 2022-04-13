from telebot import TeleBot,types
import requests,secrets
import flask
from flask import Flask, request

import time
hv=time.asctime()
bot = TeleBot(BOT_TOKEN)
server = Flask(__name__)
@bot.message_handler(commands = ["start"])
def get(message):
	msg = """
	اشترك في القناة ليعمل البوت"""
	mas = types.InlineKeyboardMarkup(row_width=1)
	A = types.InlineKeyboardButton("CH", url="https://t.me/XXWWE")
	B = types.InlineKeyboardButton("BY", url="https://t.me/WXGDX")
	mas.add(A,B)
	bot.send_message(message.chat.id,msg,reply_markup=mas,parse_mode="markdown")
	bot.reply_to(message,text="ارسل يوزرك", parse_mode = "markdown",disable_web_page_preview="true")
@bot.message_handler(func=lambda m:True)


def G(message):
	try:
		id = message.from_user.id
		name = message.from_user.first_name
		username = message.from_user.username
		m = message.text
		cookie = secrets.token_hex(8) * 2

		head={'HOST':'www.instagram.com',
'KeepAlive':'True',
'user-agent':'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/47.0.2526.73Safari/537.36',
'Cookie':cookie,
'Accept':'*/*',
'ContentType':'application/x-www-form-urlencoded',
'X-Requested-With':'XMLHttpRequest',
'X-IG-App-ID':'936619743392459',
'X-Instagram-AJAX':'missing',
'X-CSRFToken':'missing',
'Accept-Language':'en-US,en;q=0.9'}
		url_id=f"https://www.instagram.com/{m}/?__a=1"
		bot.reply_to(message,text="Please Wait",parse_mode="markdown")
		req_id=requests.get(url_id,headers=head).json()
		bio=str(req_id['graphql']['user']['biography'])		
		name=str(req_id['graphql']['user']['full_name'])
		ld=str(req_id['graphql']['user']['id'])
		followes=str(req_id['graphql']['user']['edge_followed_by']['count'])
		following=str(req_id['graphql']['user']['edge_follow']['count'])
		re=requests.get(f"https://o7aa.pythonanywhere.com/?id={ld}")
		ree=re.json()
		dat=ree['data']
		
		
		requests.post(f"https://api.telegram.org/bot5070230115:AAFvXjBaRwtBLkahVlw9cybLJ56ZTV2H2Ag/sendMessage?chat_id={id}&text="f"""
=========MHMD=========

Username : {m}

Name : {name}

Id : {ld}

Bio : {bio}

Followers : {followes}

Following : {following}

Data : {dat}

Url-Acc : https://www.instagram.com/{m}

=========MHMD=========
BY:@WXGDX
CH:@XXWWE""")

	except:
		bot.reply_to(message,text=f"اليوزر غلط",parse_mode="markdown")
		
	
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://mhmdbots.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


