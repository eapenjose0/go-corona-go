import time
from utils import telegram_utils, message_utils
from Centers import Centers
import requests, json
import pickle

# TODO: Accept values as arguements
STATE_CODE = 17 # Kerala
SEARCH_N_DAYS = 5 # 

def get_district_list():
    distric_list = {}
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(STATE_CODE))
    json_data = json.loads(response.text)
    for district in json_data["districts"]:
        distric_list[district["district_id"]] = district["district_name"]

    return distric_list


def main():
    try:
        district_list = get_district_list()
        district_ids = district_list.keys()

        message_details_file = open("data/message_details.pkl", "rb")
        prev_message_details = pickle.load(message_details_file)
        
        for district_id in district_ids:
            # State code: 17 - Kerala
            kerala_centers = Centers(state_code=STATE_CODE, search_n_days=SEARCH_N_DAYS).find_centers_by_district_id(district_id=district_id)
            
            DISTRICT_NAME = district_list[district_id]
            final_message = ""
            final_message += message_utils.get_header()
            final_message  += f"\n\n"

            # Delete previous message
            if prev_message_details.get(district_id):
                message_id = prev_message_details[district_id]["message_id"]
                chat_id = prev_message_details[district_id]["chat_id"]

                print(message_id, chat_id)
                try:
                    telegram_utils.bot.delete_message(chat_id=chat_id,
                    message_id=message_id)
                except Exception as e:
                    pass


            if len(kerala_centers) == 0: 
                continue         
            
            for center in kerala_centers:
                message = message_utils.prepare_message(center)
                final_message += message
                
            prev_message_details[district_id] = telegram_utils.send_alert(final_message, district_id)

        message_details_file = open("data/message_details.pkl", "wb")
        pickle.dump(prev_message_details, message_details_file)
        message_details_file.close()
    except Exception as e:
        print(f"Exception: {e}")
        pass        
   

if __name__ == '__main__':
    while True:
        main()
        time.sleep(30)
    



    