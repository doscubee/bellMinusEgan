import os
import datetime
import time

# MADE BY JONATHAN

bellSchedule = [
  ["monday", "08:25:00", "08:30:00", "09:16:00", "09:19:00", "10:05:00", "10:08:00", "10:57:00", "11:11:00", "11:14:00", "12:00:00", "12:03:00", "12:49:00", "13:25:00", "13:28:00", "14:14:00", "14:17:00", "15:03:00"],
    
  ["tuesday", "08:25:00", "08:30:00", "09:12:00", "09:15:00", "09:57:00", "10:00:00", "10:42:00", "10:56:00", "10:59:00", "11:27:00", "11:30:00", "12:12:00", "12:15:00", "12:57:00", "13:33:00", "13:36:00", "14:18:00", "14:21:00", "15:03:00"],
    
  ["wednesday", "09:12:00", "09:17:00", "10:39:00", "10:53:00", "10:56:00", "12:18:00", "12:54:00", "12:57:00", "14:19:00", "14:22:00", "15:03:00"],
    
  ["thursday", "08:25:00", "08:30:00", "09:52:00", "09:58:00", "10:01:00", "11:23:00", "11:37:00", "11:40:00", "13:02:00", "13:38:00", "13:41:00", "15:03:00"],
    
  ["friday", "08:25:00", "08:30:00", "09:12:00", "09:15:00", "09:57:00", "10:00:00", "10:42:00", "10:56:00", "10:59:00", "11:27:00", "11:30:00", "12:12:00", "12:15:00", "12:57:00", "13:33:00", "13:36:00", "14:18:00", "14:21:00", "15:03:00"],
    
  ["minimum", "08:25:00", "08:30:00", "09:00:00", "09:03:00", "09:33:00", "09:36:00", "10:06:00", "10:09:00", "10:39:00", "10:51:00", "10:54:00", "11:24:00", "11:27:00", "11:57:00", "12:00:00", "12:30:00"],
  
  ["assembly", "08:25:00", "08:30:00", "09:10:00", "09:13:00", "09:53:00", "09:56:00", "10:37:00", "10:51:00", "10:54:00", "11:34:00", "11:37:00", "12:17:00", "12:54:00", "12:57:00", "12:37:00", "13:40:00", "14:20:00", "14:23:00", "15:03:00"]
]

now = datetime.datetime.now()
dayNum = now.weekday()
timeRn = now.strftime("%H:%M:%S")
timeRn = str(int(timeRn[0:2]) - 7) + ":" + timeRn[3:]

def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

def updateTime():
  global timeRn
  if int(timeRn[0:2]) == 7:
    timeRn = "24" + timeRn[2:]
  if int(timeRn[0:2]) == 6:
    timeRn = "23" + timeRn[2:]
  if int(timeRn[0:2]) == 5:
    timeRn = "22" + timeRn[2:]
  if int(timeRn[0:2]) == 4:
    timeRn = "21" + timeRn[2:]
  if int(timeRn[0:2]) == 3:
    timeRn = "20" + timeRn[2:]
  if int(timeRn[0:2]) == 2:
    timeRn = "19" + timeRn[2:]
  if int(timeRn[0:2]) == 1:
    timeRn = "18" + timeRn[2:]

def timeToSeconds(timeRn):
  return int(timeRn[0:2]) * 3600 + int(timeRn[3:5]) * 60 + int(timeRn[6:8])

def secondsToTime(secondsRn):
  hours = str(secondsRn//3600)
  minutes = str((secondsRn%3600)//60)
  seconds = str((secondsRn%3600)%60)
  if len(hours) == 1:
    hours = "0" + hours
  if len(minutes) == 1:
    minutes = "0" + minutes
  if len(seconds) == 1:
    seconds = "0" + seconds
  return hours + ":" + minutes + ":" + seconds

def printTimeLeft():

  if dayNum == 5 or dayNum == 6:
    return "no school today"
  else:
    for i in range(1, len(bellSchedule[dayNum])):
      if timeToSeconds(timeRn) > timeToSeconds(bellSchedule[dayNum][i]):
        continue
      else:
        return secondsToTime( timeToSeconds(bellSchedule[dayNum][i]) - timeToSeconds(timeRn) )
    return "no school :)))))))"
  
# MAIN LOOPPPPPPPP


while True:

  clearScreen()
  
  now = datetime.datetime.now()
  dayNum = now.weekday()
  timeRn = now.strftime("%H:%M:%S")
  timeRn = str(int(timeRn[0:2]) - 7) + ":" + timeRn[3:]

  print("bell.minus by jl")
  print("\n")

  print(bellSchedule[dayNum][0])
  print(printTimeLeft())
  print("btw theres sometimes a 1-2 second delay and i dont feel like fixing it")
  print("also there arent any minimum day / assembly schedules")

  time.sleep(1)
