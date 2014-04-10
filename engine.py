import time
import datetime
import os
import report
import scoring

def main():
	print("Unix scoring engine started...")
	startup()
	print("Startup completed.")	
	genReport()

def startup():
	if(checkStartup()):
		print("Engine resuming.")
	else:
		stampTime()

def checkStartup():
        return os.path.isfile("timeFile")

def stampTime():
	timeFile = open('timeFile', 'w+')
	currentTime = str(time.time())
	print("Stamping time: " + currentTime)
	timeFile.write(currentTime)
	timeFile.close()

def genReport():
        scoring.score()
        report.gen()

main()
