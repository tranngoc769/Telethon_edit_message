from signal import pause
from telethon.tl.types import InputPeerChat,InputPeerChannel

import requests,json
from pathlib import Path
import time
import mysql.connector

mydb = mysql.connector.connect(
  host: "localhost",
  port: '3306',
  user: "remoteapi",
  password: "Quang7699@",
  database: 'bot_users'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

from telethon import TelegramClient, events
config_path = Path("config.json")
config = json.loads(config_path.read_text())
client = TelegramClient("forward_bot", config["api_id"], config["api_hash"]).start()
@client.on(events.NewMessage(func=lambda e: e.is_channel))
async def handle_new_message(message):
    print(message.message.message)
    update_msg = "\nLike và subcribe"
    msg = message.message.message;
    chatid =  message.chat_id
    # chat = InputPeerChannel(chatid,)
    channle = message._entities[chatid]
    # time.sleep(5)
    await client.edit_message(channle, message, msg+update_msg)
    # sub 3374092470 | contr 666680316 | hash 911152699675979161
    # if (event.chat_id in config["target_list"]):
    #   res= requests.request("POST", config["host"]+"/send_msg", headers={'Content-Type': 'application/json'}, data=json.dumps({"message": event.message.message}))
    #   print(res)
client.start()
client.run_until_disconnected()