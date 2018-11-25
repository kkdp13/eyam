import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("eyamproject-9cf040e3da1c.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("EYAMFORMAT").sheet1
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
    Till1 = 8
    Till2 = 10
    kt1 = 10
    kt2 = 10
    resis11 = 16
    resis12 = 11
    resis21 = 16
    resis22 = 12
    resis31 = 16
    resis32 = 13
    support11 = 18
    support12 = 11
    support21 = 18
    support22 = 12
    support31 = 18
    support32 = 13
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
    until = wks.cell(Till1,Till2).value
    kt = wks.cell(kt1,kt2).value
    resis = wks.cell(resis11,resis12).value
    resis1 = wks.cell(resis21,resis22).value
    resis2 = wks.cell(resis31,resis32).value
    support = wks.cell(support11,support12).value
    support1 = wks.cell(support21,support22).value
    support2 = wks.cell(support31,support32).value
    return [yesterdaymode,todaymode,todaytrend,todayLY,todayJP,
    todayNN1,todayNN2,todayKM1,todayKM2,todayLOW,todayHIGH,
    todaySet0,until,kt,resis,resis1,resis2,support,support1,support2]

def modeupdate(todaymode):
    tmode1 = 4
    tmode2 = 3
    wks.update_cell(tmode1,tmode2,todaymode)

def ymodeupdate(yesterdaymode):
    ymode1 = 3
    ymode2 = 3
    wks.update_cell(ymode1,ymode2,yesterdaymode)

def highupdate(todayhigh):
    tHIGH1 = 12
    tHIGH2 = 5
    wks.update_cell(tHIGH1,tHIGH2,todayhigh)

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
    samemode1 = 2
    samemdoe2 = 7
    tmode1 = 4
    tmode2 = 3
    newset1 = 14
    newset2 = 5
    tmode = wks.cell(tmode1,tmode2).value
    tmode = float(tmode)
    if tmode > 0:
        wks.update_cell(ymode1,ymode2,tmode)
        wks.update_cell(tHIGH1,tHIGH2,0)
        wks.update_cell(tLOW1,tLOW2,0)
        wks.update_cell(tmode1,tmode2,0)
        wks.update_cell(samemode1,samemdoe2,0)
        wks.update_cell(newset1,newset2,0)   
        return tmode
    else:
        return tmode

# Till1 = 8
# Till2 = 10
# kt1 = 10
# kt2 = 10
# resis11 = 16
# resis12 = 11
# resis21 = 16
# resis22 = 12
# resis31 = 16
# resis32 = 13
# support11 = 18
# support12 = 11
# support21 = 18
# support22 = 12
# support31 = 18
# support32 = 13
# until = wks.cell(Till1,Till2).value
# kt = wks.cell(kt1,kt2).value
# resis = wks.cell(resis11,resis12).value
# resis1 = wks.cell(resis21,resis22).value
# resis2 = wks.cell(resis31,resis32).value
# support = wks.cell(support11,support12).value
# support1 = wks.cell(support21,support22).value
# support2 = wks.cell(support31,support32).value
# print(until)
# print(kt)
# print(resis)
# print(resis1)
# print(resis2)
# print(support)
# print(support1)
# print(support2)
