from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Invite ZeroMusic, a verified music bot. https://bit.ly/InviteZeroMusic"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
