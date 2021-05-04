import datetime
import requests

class Centers:
    
    def __init__(self, state_code, search_n_days) -> None:
        self.state_code = state_code
        self.search_n_days = search_n_days


    def get_date_list(self):
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(self.search_n_days)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]

        return date_str


    def create_center_obj(self, center, session, input_date):
         
        obj = {}
        obj["date"] = input_date
        obj["district_name"] = center["district_name"]
        obj["center_name"] = center["name"]
        obj["block_name"] = center["block_name"]
        obj["pincode"] = center["pincode"]
        obj["fee_type"] = center["fee_type"]
        obj["available_capacity"] = session["available_capacity"]
        obj["min_age_limit"] = session["min_age_limit"]
        if(session["vaccine"] != ''):
            obj["vaccine"] = session["vaccine"]
        else:
            obj["vaccine"] = "NA"

        return obj


    def find_centers_by_district_id(self, district_id):
        date_list = self.get_date_list()
        centers = []
        
        for input_date in date_list:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, input_date)
            response = requests.get(URL)

            if response.ok:
                resp_json = response.json()
                if resp_json["centers"]:
                        for center in resp_json["centers"]:
                            for session in center["sessions"]:
                                available_capacity = session["available_capacity"]
                                if available_capacity > 0:
                                    centers.append(self.create_center_obj(center, session, input_date))

        return centers
                                    