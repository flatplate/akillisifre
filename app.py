from flask import Flask
from flask import render_template
import json
import random
import os

WORDLIST_ENV_VARIABLE = "AS_WORDLIST"
WORDLIST_PATH = os.environ[WORDLIST_ENV_VARIABLE]
DEFAULT_PASSWORD_LENGTH = 4

def capitalize(word):
    if word[0] == "i":
        return "İ" + word[1:]
    return word.capitalize()

def getRandomCombination(wordList, length=DEFAULT_PASSWORD_LENGTH):
    combination = ""
    for i in range(length):
        combination += random.choice(wordList)
    return combination

jsonfile = open(WORDLIST_PATH, "r", encoding="utf-16")
dic = json.loads(jsonfile.read())
wordList = [capitalize(word) for word in list(dic.keys())[:300000]]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/getPassword")
def getPassword():
    return json.dumps({"password": getRandomCombination(wordList)}, ensure_ascii=False)

if __name__ == "__main__":
    app.run()