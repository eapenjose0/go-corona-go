import telegram
import requests

TOKEN = "1701837126:AAHDVQgMp03OqhzlbI9X150pretamiCrJ2o"
bot = telegram.Bot(token=TOKEN)

def send_alert(message, district_id):
    test_channel_id = "@testvaccinate"
    thrissur_channel_id = "@tcrvaccine"
    bot_token_id = "1701837126:AAHDVQgMp03OqhzlbI9X150pretamiCrJ2o"

    url = ""
    if district_id == 303:
        url = "https://api.telegram.org/bot" + bot_token_id + "/sendMessage?chat_id=" + thrissur_channel_id + "&text=" + message
    else:
        url = "https://api.telegram.org/bot" + bot_token_id + "/sendMessage?chat_id=" + test_channel_id + "&text=" + message
    
    res = requests.post(url)
    res_json = res.json()
    message_details = {
        "message_id": res_json["result"]["message_id"],
        "chat_id": res_json["result"]["chat"]["id"]
    }
    return message_details