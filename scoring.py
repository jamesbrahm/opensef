from lib import *  # import everything in lib

results=[]  # this is the list that the results will go in
newScore=0

def score():  # called by engine to score vulnerabilities
    scoreFile=open("scoringData/scoreFile", "r")
    for line in scoreFile:
        if(line[:1]!="#"): #see if file does not start with a comment
            end=line.find("#") # see if there is a comment elsewhere
            if(end>0):
                submit(line[:end]) #only submit stuff before the hash
            else:
                submit(line) # submit the entire thing if there is no hash
        else:
            ()  # convention?
    writeData()
def submit(line):  # do the actual scoring for a given vulnerability
	
	parts=parse(line)
	# submit to score function
	check_results=["This is a success message", 5]
	results.append(check_results[0])
	newScore+=check_results[1]

def parse(v): # parse a string to return three parts
    parts=v.split(" ")
    return parts

def writeData():  # turn write results[] to scoringResults on disk
	scoringResults = open("scoringData/scoringResults", "w")
	for line in results:
		scoringResults.write(line+"\n")
	scoringResults.close()
	newScore = open("scoringData/Score", "w")
	newScore.write(str(newScore))
