import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def _make_key(chat_id):
    return f"user:{chat_id}"

def add_user(chat_id, origin, destination, date, threshold):
    key = _make_key(chat_id)
    data = {
        "chat_id": chat_id,
        "origin": origin,
        "destination": destination,
        "date": date,
        "threshold": threshold
    }
    r.set(key, json.dumps(data))

def get_all_users():
    users = []
    for key in r.scan_iter("user:*"):
        data = r.get(key)
        if data:
            users.append(json.loads(data))
    return users
