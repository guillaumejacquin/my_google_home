from jarvis import *


def main():
    presentation()
    while True:
        query = myspeech()
        query = query.lower()
        print(query)
        
        cmd(query)
main()