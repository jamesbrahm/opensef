import os
import utils

def gen():
        makePage()
        print("Report finished.")
        
def makePage():
        if(not(os.path.isfile("doc/template.html"))):
                exit(1)
        template = open("doc/template.html", "r")
        scoringResults = open("scoringData/scoringResults", "r")
        report = open("doc/report.html", "w")
        for line in template:
                if(line[:1]!="%"):
                        report.write(line)
                line=line.strip()
                if(line=="%CURRENTTIME%"):
                        report.write(utils.current_time())
                if(line=="%PINGRESULT%"):
                        report.write(utils.ping_result())
                if(line=="%TIMEELAPSED%"):
                        report.write(utils.time_elapsed())
                if(line=="%CORRECT%"):
                        report.write(utils.correct())
                if(line=="%TOTAL%"):
                        report.write(utils.total())
        for line in scoringResults:
            report.write(line + "\n <br>")
        
            
        
                
        
