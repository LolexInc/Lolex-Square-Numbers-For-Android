import sys,os,subprocess,io,time
sys.path.insert(0,"/sdcard/")
try:
    import squarenumber
except(ImportError):
    with open ("/sdcard/squarenumber.py","a") as f: f.write("squarenumbers = 2\noriginsquare = 2")
import squarenumber
squarenumbers = squarenumber.squarenumbers
originsquare = squarenumber.originsquare
gone = 0
while True:
    squarenumbers = originsquare*originsquare
    originsquare = originsquare + 1
    print(squarenumbers)
    gone = gone + 1
    if gone == 1000 or gone>1000:
        try:
            os.remove("/sdcard/squarenumber.py")
        except(FileNotFoundError):
           pass
        with open ("/sdcard/squarenumber.py","a") as f: f.write("\nsquarenumbers = ")
        with open ("/sdcard/squarenumber.py","a") as outf: outf.write(str(squarenumbers))
        with open ("/sdcard/squarenumber.py","a") as f: f.write("\noriginsquare = ")
        with open ("/sdcard/squarenumber.py","a") as outf: outf.write(str(originsquare))
        gone = 0

