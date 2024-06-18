import datetime
# Function to get current date and time
def get_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("Current date and time: %Y-%m-%d %H:%M:%S")
