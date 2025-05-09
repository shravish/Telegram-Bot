# Telegram-Bot

## Structure Overview
This project consists of the following main components:

### File  - 	Purpose
#### 1.```bot.py``` - Handles Telegram messages, commands, and alerts
#### 2.```flight_tracker.py```	-  Fetches flight price data from the Kiwi Tequila API
#### 3.```db.py```	-  Stores user tracking preferences in memory
#### 4.```scheduler.py```	- Periodically checks prices and triggers alerts
#### 5.```config.py```	-  Stores API keys and configuration values
#### 6.```requirements.txt```	- Required libraries for the bot to run

### Code Breakdown (Step-by-Step)

### 1. ```bot.py``` — Bot Logic
/start command: Sends a welcome message explaining how to use the bot.

/track command:

Expects: ```/track <FROM> <TO> <YYYY-MM-DD> <MAX_PRICE>```

Example: ```/track JFK LAX 2025-07-10 250```

Stores this info in memory using ```add_user()``` from db.py.

```alert_user(chat_id, price, user):```

Called by the scheduler when a flight price drops.

Sends a Telegram message to that user.

```app.run_polling():```

Starts the bot and listens for user messages.

### 2. ```db.py``` — In-Memory Storage
Keeps user flight tracking preferences in a Python list:

```user_preferences = []```

```add_user(...)```: Adds a user's preferences to that list.

```get_all_users()```: Returns the list to be used by the scheduler.

✅ Simpler than using a real database, but doesn't persist between restarts.

### 3. ```flight_tracker.py``` — Flight Price API
Connects to Kiwi.com Tequila API to fetch flight prices.

Constructs a search with:

i.Origin

ii.Destination

iii.Travel date

iv.Sorted by lowest price

v.Returns the cheapest price (or ```None``` if nothing found).

### 4. ```scheduler.py``` — Periodic Price Checking
Uses ```APScheduler``` to check prices every 60 minutes.

For every user in ```user_preferences```:

Calls ```get_flight_price()```

If the price is BELOW THE THRESHOLD → calls ```alert_user()```

Starts running when you launch the bot (```scheduler.start()``` in ```bot.py```).

### 5. ```config.py``` — Config/Secrets
Stores:

i.Telegram Bot Token
ii.Kiwi API Key

```
TELEGRAM_TOKEN = "your_telegram_token"
FLIGHT_API_KEY = "your_kiwi_api_key"
```
You'll need to fill in your actual tokens here.

### 🔁 Example Flow
User runs ```/track JFK LAX 2025-07-10 250```

✅ Bot stores this preference in memory.

🕐 Every 60 minutes:

Bot checks flight prices via the API

If price ```< $250``` → Sends a Telegram alert to that user.








