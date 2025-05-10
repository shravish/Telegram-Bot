from apscheduler.schedulers.background import BackgroundScheduler
from flight_tracker import get_flight_price
from db import get_all_users
from bot import alert_user

scheduler = BackgroundScheduler()

def check_prices():
    for user in get_all_users():
        price = get_flight_price(user["origin"], user["destination"], str(user["date"]))
        if price and price < user["threshold"]:
            alert_user(user["chat_id"], price, user)

def start():
    scheduler.add_job(check_prices, 'interval', minutes=60)
    scheduler.start()
