import datetime


def prepare_message(obj):
    message = ""
    message += "\n"
    message += f"Available on: {obj['date']}\n"
    message += f"District name: {obj['district_name']}\n"
    message += f"Center name: {obj['center_name']}\n"
    message += f"Pin Code: {obj['pincode']}\n"
    message += f"Price: {obj['fee_type']}\n"
    message += f"Available Capacity: {obj['available_capacity']}\n"
    message += f"Minimum age limit: {obj['min_age_limit']}\n"
    message += f"Vaccine: {obj['vaccine']}\n"
    
    return message
    
def get_header():
    now = datetime.datetime.today()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    header	= f"- Updated at: {dt_string} -"
    return header