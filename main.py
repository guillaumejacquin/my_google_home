from jarvis import *


def main():
    presentation()
    pause = 0
    while True:
        if (pause == 0):
            query = myspeech()
            query = query.lower()
            cmd(query)


            if (query == "mets-toi en pause"):
                pause = 1
 
        
        if(pause == 1):
            pause = myspeech_pause()


            
            
        
main()