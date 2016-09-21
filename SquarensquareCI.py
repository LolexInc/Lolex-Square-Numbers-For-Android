import sys,os,subprocess,io,time
squarenumbers = 2
originsquare = 2
gone = 0
while gone != 1000:
    squarenumbers = originsquare*originsquare
    originsquare = originsquare + 1
    print(squarenumbers)
    gone = gone + 1
