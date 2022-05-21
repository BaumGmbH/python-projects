from OwnModules.cmd_args import *


def getTime(time_in, longVariant, reversed):
    timeSuffix = []
    time = []
    timeList = []
    timeString = ""
    

    if longVariant:
        timeSuffix = ["Eine Sekunde", " Sekunden", "Eine Minute", " Minuten", "Eine Stunde", " Stunden", "Ein Tag", " Tage", "Ein Jahr", " Jahre"]
    else:
        timeSuffix = ["1s", "s", "1m", "m", "1h", "h", "1d", "d", "1y", "y"]
    

    if seconds == 1:
        time[0] = timeSuffix[0]
    elif seconds != 0:
        time[0] = str(time_in[0]) + timeSuffix[1]
    

    if minutes == 1:
        time[1] = timeSuffix[2]
    elif minutes != 0:
        time[1] = str(time_in[1]) + timeSuffix[3]
    

    if hours == 1:
        time[2] = timeSuffix[4]
    elif hours != 0:
        time[2] = str(time_in[2]) + timeSuffix[5]
    

    if days == 1:
        time[3] = timeSuffix[6]
    elif days != 0:
        time[3] = str(time_in[3]) + timeSuffix[7]
    

    if years == 1:
        time[4] = timeSuffix[8]
    elif years != 0:
        time[4] = str(time_in[4]) + timeSuffix[9]
    

    for unit in time:
        if unit != null and len(unit) != 0:
            timeList.append(unit)
        
    

    if reversed:
    
        reversed = list(range(0, len(timeList)))
        reversed.reverse()
    
        for i in reversed:
            timeString += timeList[i]

            if i == 1:
                timeString += " und "
            elif i != 0:
                timeString += ", "
            
        
    else:
        for i in range(0, len(timeList)):
            timeString += timeList[i]

            if i == timeList.size() - 2:
                timeString += " und "
            elif i != timeList.size() - 1:
                timeString += ", "

    return timeString


secs = extract_info('-sec').replace('.', '')
long = extract_info('-lon')
reve = extract_info('-rev')

secs = int(secs)

seconds = secs % 60
minutes = (secs / 60) % 60
hours = (secs / 3600) % 24
days = (secs / 86400) % 365
years = secs / 31536000

#print(type(bool(long)))
#print(bool(int(long)))

print(getTime([seconds, minutes, hours, days, years], long, reve))

# seconds % 60, (seconds / 60) % 60, (seconds / 3600) % 24, (seconds / 86400) % 365, seconds / 31536000
