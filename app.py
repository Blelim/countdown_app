import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    today = datetime.now()
    days_until_saturday = (5 - today.weekday() + 7) % 7
    if days_until_saturday == 0:
        days_until_saturday = 7
    return f"<h1>Залишилось {days_until_saturday} днів до наступної суботи</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
