#!C:/Users/Tatum/AppData/Local/Programs/Python/Python37/python.exe
# print("Content-type: text/html")
# print()
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:04:11 2018

@author: Tatum

version 1.00
  -create bot for eyam
"""

from flask import Flask, request
import json
import requests
from eyam import eyam
from googlesheet import eyaminfo, modeupdate, ymodeupdate, highupdate, lowupdate, resetnewday

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer ni2OchQdVILm0CxVI4fUHmfMIzPaYMtxuHIpQoKH1BJLOlKzgoV3t/z9VQCH95N+Oawt40F4qVxbnovStWXBcZzH783TOAoB6I6k5d6t6qc/EiFukdIydJX4JL3xn3XZ6TXLV8uh3jgksHsh2rMvyQdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server for eyam.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    # msg_in_string = json.dumps(msg_in_json)
    # writeindb(msg_in_json)    
    # with open('datacollection.json', 'w') as writefile:
    #    json.dump(msg_in_json, writefile)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    # userID =  msg_in_json["events"][0]['source']['userId']
    # msgType =  msg_in_json["events"][0]['message']['type']
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    # if msgType != 'text':
    #    reply(replyToken, ['Only text is allowed.'])
    #    return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ 
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    textstart = text[0]
    
    if textstart == '/':
        if text[1] == 't':
            todaymode = text.split(",")[1]
            modeupdate(todaymode)
            replyQueue.append("tmode updated : {}".format(todaymode))
            reply(replyToken, replyQueue[:5])
        elif text[1] == 'y':
            yesterdaymode = text.split(",")[1]
            ymodeupdate(yesterdaymode)
            replyQueue.append("ymode updated : {}".format(yesterdaymode))
            reply(replyToken, replyQueue[:5])
        elif text[1] == 'h':
            todayHIGH = text.split(",")[1]
            highupdate(todayHIGH)
            replyQueue.append("HIGH updated : {}".format(todayHIGH))
            reply(replyToken, replyQueue[:5])
        elif text[1] == 'l':
            todayLOW = text.split(",")[1]
            lowupdate(todayLOW)
            replyQueue.append("LOW updated : {}".format(todayLOW))
            reply(replyToken, replyQueue[:5])
        elif text[1] == 'r':
            resetdone = resetnewday()
            if resetdone > 0:
                replyQueue.append("reset")
                reply(replyToken, replyQueue[:5])
            else:
                replyQueue.append("กด reset ไปแล้วครับ")
                reply(replyToken, replyQueue[:5])   
        return 'OK', 200
    elif textstart == '=':
        geteyaminfos = eyaminfo()
        """yesterdaymode,todaymode,todaytrend,
        todayLY,todayJP,todayNN1,todayNN2,
        todayKM1,todayKM2,todayLOW,todayHIGH,todaySet0,
        until,KT,resis,support"""
        info = "ymode = {}\ntmode = {}\ntrend = {}\nset0 = {}\n".format(geteyaminfos[0],geteyaminfos[1],geteyaminfos[2],geteyaminfos[11])
        info2 = "LY 50% = {}\nJP 127% = {}\nNN1 161.8% = {}\nNN2 261.8% = {}\n".format(geteyaminfos[3],geteyaminfos[4],geteyaminfos[5],geteyaminfos[6])
        info3 = "KM1 423.6% = {}\nKM2 685.4% = {}\nLOW = {}\nHIGH = {}\n".format(geteyaminfos[7],geteyaminfos[8],geteyaminfos[9],geteyaminfos[10])
        info4 = "Till = {}\nKT = {}\nแนวต้าน = {},{},{}\nแนวรับ = {},{},{}\n".format(geteyaminfos[11],geteyaminfos[12],geteyaminfos[13],geteyaminfos[14],geteyaminfos[15],geteyaminfos[16],geteyaminfos[17],geteyaminfos[18])
        replyQueue.append(info+info2+info3+info4)
        reply(replyToken, replyQueue[:5])
        return 'OK', 200
    # elif textstart == '.':
    #     currency = 0.0
    #     currency = float(getcurrency())
    #     currencytext = 'superrich rate = {}'.format(currency)
    #     replyQueue.append(currencytext)
    #     reply(replyToken, replyQueue[:5])
    #     return 'OK', 200
    else:
        # replyQueue.append('please start with / for asking bot')
        # reply(replyToken, replyQueue[:5]) 
        return 'OK', 200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
