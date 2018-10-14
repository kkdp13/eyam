#eyam files for eyam group

def eyam(t_mode, y_mode, t_high, t_low):
    todaymode = t_mode #get info from user line
    yesterdaymode = y_mode #y_mode #get info from googlesheet
    if(todaymode <= yesterdaymode): #trend down
        todayly = (yesterdaymode+todaymode)/2
        todayset0 = findset0(float(t_mode), float(t_high), float(t_low))
        todaytrend = "down trend"
        return (todayly, todayset0, todaytrend)
    if(todaymode >= yesterdaymode): #trend up
        todayly = (yesterdaymode+todaymode)/2
        todayset0 = findset0(float(t_mode), float(t_high), float(t_low))
        todaytrend = "up trend"
        return (todayly, todayset0, todaytrend)
    if(todaymode == yesterdaymode): #no trend
        todayly = 0
        todayset0 = 0
        todaytrend = "no trend"
        return (todayly, todayset0, todaytrend)

def findset0(t_mode, y_mode, t_high, t_low):
    if(t_high-t_mode < t_mode-t_low):
        todayset0 = (t_mode-t_high+t_mode) #get high from streaming
        return todayset0
    elif(t_high-t_mode > t_mode-t_low):
        todayset0 = (t_mode-t_low+t_mode) #get low from streaming
        return todayset0
    else:
        todayset0 = 0
        return todayset0

# textfromuser = "/1114,1120,1113"
# todaymode = textfromuser.split(",")[0]
# todaymode = todaymode[1:]
# print(todaymode) # check today mode
# todayhigh = textfromuser.split(",")[1]
# print(todayhigh) # check today high
# todaylow = textfromuser.split(",")[2]
# print(todaylow) # check today low
# todaymode = float(todaymode)
# todayhigh = float(todayhigh)
# todaylow = float(todaylow)
# todaymode = 1114
# yesterdaymode = 1113
# todayhigh = 1120
# todaylow = 1113

# getinfo = eyam(todaymode, todayhigh, todaylow)
# print("today ly = {}".format(getinfo[0]))
# print("today set 0 = {}".format(getinfo[1]))
# print("today trend = {}".format(getinfo[2]))