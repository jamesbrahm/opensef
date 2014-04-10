import os
import datetime
import time
import subprocess

def current_time():
	return time.strftime("%H:%M:%S")

def ping_result():
        try:
                systemPing=str(subprocess.check_output(["ping", "-c 1", "www.google.com"]))
                startString=systemPing.index("time=")
                endString=systemPing.index("ms")
                ping_result=systemPing[startString+5:endString+2]
                print(ping_result)
                return "Success! ("+ping_result+")"
        except:
               return "FAILED" 
        

def time_elapsed():
        timeFile=open("timeFile", "r")
        oldTime=float(timeFile.read().strip())
        elapsed=(time.time()-oldTime)
        time_elapsed=str(datetime.timedelta(seconds=elapsed))
        return time_elapsed[:time_elapsed.index(".")]

def correct():
    num=str(subprocess.check_output(["wc", "-l", "scoringData/scoringResults"]))
    return num[2:3]

def total():
    return "TOTAL"

