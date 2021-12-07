import json
import sys

def main(jsonfilename):
    dfp = open(jsonfilename)

    data = json.load(dfp)    
    for i in data['Events']:
        print i
        print 
        print 
        print
        print
    

if __name__ == '__main__':
    main(sys.argv[1])
