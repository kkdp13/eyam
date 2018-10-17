import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("testeyam-37ea015cf1ac.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("test").sheet1
pp = pprint.PrettyPrinter()
glist = wks.get_all_values()
# pp.pprint(glist) #print all list in ggsheet
def eyaminfo():
    ymode1 = 3
    ymode2 = 3
    tmode1 = 4
    tmode2 = 3
    ttrend1 = 3
    ttrend2 = 5
    tLY1 = 5
    tLY2 = 4
    tJP1 = 6
    tJP2 = 4
    tNN11 = 7
    tNN12 = 4
    tNN21 = 8
    tNN22 = 4
    tKM11 = 9
    tKM12 = 4
    tKM21 = 10
    tKM22 = 4
    tLOW1 = 12
    tLOW2 = 2
    tHIGH1 = 12
    tHIGH2 = 5
    tSet1 = 13
    tSet2 = 3
    yesterdaymode = wks.cell(ymode1,ymode2).value
    todaymode = wks.cell(tmode1,tmode2).value
    todaytrend = wks.cell(ttrend1,ttrend2).value
    todayLY = wks.cell(tLY1,tLY2).value
    todayJP = wks.cell(tJP1,tJP2).value
    todayNN1 = wks.cell(tNN11,tNN12).value
    todayNN2 = wks.cell(tNN21,tNN22).value
    todayKM1 = wks.cell(tKM11,tKM12).value
    todayKM2 = wks.cell(tKM21,tKM22).value
    todayLOW = wks.cell(tLOW1,tLOW2).value
    todayHIGH = wks.cell(tHIGH1,tHIGH2).value
    todaySet0 = wks.cell(tSet1,tSet2).value
    # print("yesterdaymode = {}".format(yesterdaymode))
    # print("todaymode = {}".format(todaymode))
    # print("todaytrend = {}".format(todaytrend))
    # print("todayLY 50% = {}".format(todayLY))
    # print("todayJP 127% = {}".format(todayJP))
    # print("todayNN1 161.8% = {}".format(todayNN1))
    # print("todayNN2 261.8% = {}".format(todayNN2))
    # print("todayKM1 423.6% = {}".format(todayKM1))
    # print("todayKM2 685.4% = {}".format(todayKM2))
    # print("todayLOW = {}".format(todayLOW))
    # print("todayHIGH = {}".format(todayHIGH))
    # print("todaySet0 = {}".format(todaySet0))
    # print("--------"*10)
    return [yesterdaymode,todaymode,todaytrend,todayLY,todayJP,todayNN1,todayNN2,todayKM1,todayKM2,todayLOW,todayHIGH,todaySet0]

def modeupdate(todaymode):
    tmode1 = 4
    tmode2 = 3
    wks.update_cell(tmode1,tmode2,todaymode)
    # set11 = 14
    # set12 = 5
    # mode1 = 2
    # mode2 = 7
    # tmode = wks.cell(tmode1,tmode2).value
    # if tmode == 0:
    #     wks.update_cell(tmode1,tmode2,todaymode)
    #     wks.update_cell(mode1,mode2,todaymode)
    #     wks.update_cell(set11,set12,1)
    # else:
    #     wks.update_cell(tmode1,tmode2,todaymode)
    #     mode = wks.cell(mode1,mode2).value
    #     if mode != todaymode:
    #         wks.update_cell(mode1,mode2,todaymode)
    #         wks.update_cell(set11,set12,1)

def ymodeupdate(yesterdaymode):
    ymode1 = 3
    ymode2 = 3
    wks.update_cell(ymode1,ymode2,yesterdaymode)

def highupdate(todayhigh):
    tHIGH1 = 12
    tHIGH2 = 5
    wks.update_cell(tHIGH1,tHIGH2,todayhigh)
    # oldhigh = wks.cell(tHIGH1,tHIGH2).value
    # if oldhigh == 0:
    #     wks.update_cell(tHIGH1,tHIGH2,todayhigh)
    # else:
    #     wks.update_cell(tHIGH1,tHIGH2,todayhigh)

def lowupdate(todaylow):
    tLOW1 = 12
    tLOW2 = 2
    wks.update_cell(tLOW1,tLOW2,todaylow)

def resetnewday():
    tLOW1 = 12
    tLOW2 = 2
    tHIGH1 = 12
    tHIGH2 = 5
    ymode1 = 3
    ymode2 = 3
    tmode1 = 4
    tmode2 = 3
    samemode1 = 2
    samemdoe2 = 7
    tmode1 = 4
    tmode2 = 3
    newset1 = 14
    newset2 = 5
    tmode = wks.cell(tmode1,tmode2).value
    if tmode == 0:
        return 1
    else:
        wks.update_cell(ymode1,ymode2,tmode)
        wks.update_cell(tHIGH1,tHIGH2,0)
        wks.update_cell(tLOW1,tLOW2,0)
        wks.update_cell(tmode1,tmode2,0)
        wks.update_cell(samemode1,samemdoe2,0)
        wks.update_cell(newset1,newset2,0)
        return 0

# eyaminfo()
# yesmode1 = 3
# yesmode2 = 3
# wks.update_cell(yesmode1,yesmode2,'1234')
# eyaminfo()