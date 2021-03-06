#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install flask
"""

from flask import Flask
from flask import request
from flask import jsonify
from line_sdk import Linebot

from DrugBot import runLoki as drugbot

LINE_ACCESS_TOKEN   = " "
LINE_CHANNEL_SECRET = " "

app = Flask(__name__)

@app.route("/Lanlanlu/", methods=["GET", "POST"])
def webhook():
    # GET
    if request.method == "GET":
        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # POST
    elif request.method == "POST":
        body = request.get_data(as_text=True)
        signature = request.headers["X-Line-Signature"]

        # Line
        linebot = Linebot(LINE_ACCESS_TOKEN, LINE_CHANNEL_SECRET)

        # dataLIST = [{status, type, message, userID, replyToken, timestamp}]
        # replyToken=聊天室ID , message=送過來的內容
        
        dataLIST = linebot.parse(body, signature)
        for dataDICT in dataLIST:
            if dataDICT["status"]:
                if dataDICT["type"] == "message":
                    # Send Message

                    #dataDICT["message"]是input的string，用[]包起來變InputLIST傳給RunLoki
                    response = drugbot([dataDICT["message"]])
                    if response == "https://drugs.olc.tw/drugs/outward/":
                        linebot.respTexts(dataDICT["replyToken"], ["非藥物查詢的話我不會回答啦(╬☉д⊙)"])
                    else:
                        linebot.respTexts(dataDICT["replyToken"], ["以下為查詢結果：\n", response])
                    #linebot.respText(dataDICT["replyToken"], "咩噗") #回應到哪裡
                    #linebot.respText(dataDICT["replyToken"], dataDICT["message"]) #回應跟input一樣的回答

        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return jsonify({"status": False, "msg": "HTTP_405_METHOD_NOT_ALLOWED"})





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8006)