# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:35:21 2018

@author: Chenlu Wu
"""

import cv2
import os
import numpy as np
import serial
import win32com.client
import math
import time
import serial.tools.list_ports
import speech_recognition as sr
import winsound
import random
import re 
import pytesseract
from ar_markers import detect_markers
from typing import NamedTuple

code=-1
coden=-1
codea=-1
codeready=-1
nonrec=0
card=[]
cardz=[]
class Pal(NamedTuple):
    ID: int
    Num: int
    Cen: int
    colz: str

def talk(con):
    say="media//"+con
    winsound.PlaySound(say, winsound.SND_FILENAME)

def seri(ardu):
    drawing=0
    try:
        ser.write(str(ardu).encode())
        print(ardu+"input success")        
    except:
        pass
    while True:
        try:
             drawing= int(ser.read())
        except:
            pass
        #drawing=1
        print(ardu)
        if drawing==1:
            drawing=0
            break

def scan(img,mnum,ccol):
    global card
    global cardz
    markers = detect_markers(img)
    for marker in markers:
        marker.highlite_marker(img)
        #print(marker.id)
        if marker.id>=10:
            colz="black"
            num=int(str(marker.id)[1])
        else:
            colz="white"
            num=int(str(marker.id))
        palo=Pal(marker.id,num,marker.center,colz)
        paloz=Pal(marker.id,0,0,0)
        #if not (palo in card ):
        if not paloz in cardz:
            card.append(palo)
            cardz.append(paloz)
    #cv2.imshow('AR', img)
    card = sorted(card, key=lambda x:x.Cen[0], reverse=False)
    lens=len(cardz)    
    print(lens)
    if lens==4:
        for i in range(len(card)):
            #if not card[i].Num in mnum:
            mnum.append(card[i].Num)
            ccol.append(card[i].colz)
            if len(mnum)==4:
                break
    return mnum,ccol,lens

def ss1(event,x,y,flags,param):
    global code
    if event == cv2.EVENT_LBUTTONDOWN:   
        #cv2.circle(img,(x,y),4,(255,0,0),-1)
        if y>230 and y<386:
            if x>150 and x<275:
                #print("first")
                code=1
            if x>275 and x<400:
                #print("second")
                code=2
            if x>400 and x<525:
                #print("third")
                code=3
            if x>525 and x<640:
                #print("fourth")
                code=4

def ss2(event,x,y,flags,param):
    global coden
    if event == cv2.EVENT_LBUTTONDOWN:   
        #cv2.circle(img,(x,y),4,(255,0,0),-1)
        if y>110 and y<220:
            if x>32 and x<120:
                #print(1)
                coden=0
            if x>130 and x<218:
                #print(2)
                coden=1
            if x>228 and x<312:
                #print(3)
                coden=2
            if x>328 and x<414:
                #print(4)
                coden=3
            if x>426 and x<512:
                #print(4)
                coden=4
            if x>522 and x<610:
                #print(5)
                coden=5

def ss3(event,x,y,flags,param):
    global codea
    if event == cv2.EVENT_LBUTTONDOWN:   
        #cv2.circle(imgui,(x,y),4,(255,0,0),-1)
        if y>231 and y<363:
            if x>58 and x<187:
                #print(1)
                codea=0
            if x>454 and x<585:
                #print(2)
                codea=3

def ss4(event,x,y,flags,param):
    global codeready
    if event == cv2.EVENT_LBUTTONDOWN:   
        #cv2.circle(imgui,(x,y),4,(255,0,0),-1)
        if y>142 and y<292:
            if x>271 and x<564:
                #print(1)
                codeready=0


       
def PGUI(guistep):
    cv2.namedWindow('GUI')
    if guistep==0:        
        imgui = cv2.imread("start.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
    if guistep==20:
        imgui = cv2.imread("s0.jpg")
        cv2.setMouseCallback('GUI',ss1)
        while 1:
            cv2.imshow('GUI',imgui)
            if code>-1:
                print(code)
                #cv2.destroyWindow('GUI')
                break               
            if cv2.waitKey(1) &0xFF == 27:
                break
            
    if guistep==21:        
        imgui = cv2.imread("s1.jpg")
        cv2.setMouseCallback('GUI',ss2)
        while 1:
            cv2.imshow('GUI',imgui)
            if coden>-1:
                print(coden)
                #cv2.destroyWindow('GUI')
                break
            if cv2.waitKey(1) &0xFF == 27:
                break
    if guistep==22:        
        imgui = cv2.imread("s2.jpg")
        cv2.setMouseCallback('GUI',ss3)
        while 1:
            cv2.imshow('GUI',imgui)
            if codea>-1:
                print(codea)
                if codea==0:
                    PGUI(10)
                if codea==3:
                    PGUI(11)
                #cv2.destroyWindow('GUI')
                break
            if cv2.waitKey(1) &0xFF == 27:
                break
    if guistep==23:        
        imgui = cv2.imread("s3.jpg")
        cv2.setMouseCallback('GUI',ss4)
        while 1:
            cv2.imshow('GUI',imgui)
            if codeready>-1:
                print(codeready)
                break
            if cv2.waitKey(1) &0xFF == 27:
                break
    if guistep==10:        
        imgui = cv2.imread("happy.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
    if guistep==11:        
        imgui = cv2.imread("sad.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
    if guistep==12:        
        imgui = cv2.imread("excited.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
    if guistep==13:        
        imgui = cv2.imread("lose.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
    if guistep==99: 
        imgui = cv2.imread("i1.jpg")
        cv2.imshow('GUI',imgui)
        print("99")
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i1.wav")
        cv2.waitKey (0)
        imgui = cv2.imread("i10.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i10.wav")
        time.sleep(1)
        imgui = cv2.imread("i2.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i2.wav")
        time.sleep(1)
        imgui = cv2.imread("i3.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i3.wav")
        time.sleep(1)
        imgui = cv2.imread("i4.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i4.wav")
        time.sleep(1)
        imgui = cv2.imread("i5.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i5.wav")
        time.sleep(1)
        imgui = cv2.imread("i6.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i6.wav")
        time.sleep(1)
        imgui = cv2.imread("i7.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i7.wav")
        time.sleep(1)
        imgui = cv2.imread("i8.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i8.wav")
        time.sleep(1)
        imgui = cv2.imread("i9.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i9.wav")
        time.sleep(1)
        imgui = cv2.imread("i91.jpg")
        cv2.imshow('GUI',imgui)
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i91.wav")
        time.sleep(1)
        imgui = cv2.imread("i92.jpg")
        cv2.imshow('GUI',imgui)       
        if cv2.waitKey(1) &0xFF == 27:
            cv2.destroyWindow('GUI')
        talk("i92.wav")
#bubble sort the panels
def bubble_sort(lis,col):
    n=len(lis)
    print(n)
    for i in range(n):
        wordsold[i]=lis[i]
    
    for j in range(0,n-1):
        bcount=0
        for i in range (0,n-1-j):
            if lis[i]>lis[i+1]:
                lis[i],lis[i+1]=lis[i+1],lis[i]
                col[i],col[i+1]=col[i+1],col[i]                
                bcount=bcount+1
            elif lis[i]==lis[i+1]:
                if col[i]>col[i+1]:
                    lis[i],lis[i+1]=lis[i+1],lis[i]
                    col[i],col[i+1]=col[i+1],col[i]                
                    bcount=bcount+1
                    
        if bcount==0:
            break
    return lis,col
#When the robot obtain the original panel color and panel number, after bubble sort, find out the correspond
#address, send code to serial port to let the robot know move which panel to the first position, so that to 
#put the panel in numerical order
def find_address(newwords,colnew):
    l=len(newwords)
    print(l)
    print("newwords[l-i-1]=" +str(newwords[l-1]))
    print("wordsold.index="+str(wordsold.index(newwords[l-1])))
    lcount=0   
    for i in range (l):
        
        d1=wordsold.index(newwords[l-i-1])
        '''
        print("newword="+str(newwords))
        
        print("colnew=" +str(colnew))
        print("wordold="+str(wordsold))
        print("colold=" +str(colold))
        print("newwords[l-i-1]=" +str(newwords[l-i-1]))
        print("wordsold[d1]="+str(wordsold[d1]))        
        print("colnew[l-i-1]=" +str(colnew[l-i-1]))
        print("colold[d1]"+str(colold[d1]))
        '''
        #Send info to serial port
        #.........................................
        if colnew[l-i-1]==colold1[d1]:
            #print("the number is"+ str(newwords[l-i-1]))
            #print("The "+str(i)+"th address is "+str(d1)+" ," "move "+ str(d1+1)+"th panel")
            del wordsold[d1]
            del colold1[d1]            
            print("del neww"+str(wordsold))
            print("del coln="+str(colold1))            
            d1=d1+lcount
            lcount=lcount+1
            print("The "+str(i)+"th address is "+str(d1)+" ," "move "+ str(d1+1)+"th panel")
            ardmov="mo"+str(d1+1)
            seri(ardmov)
        else:
            wordsold[d1]=10
            print("wordsold111= "+str(wordsold))
            d2=wordsold.index(newwords[l-i-1])
            del wordsold[d2]
            del colold1[d2]            
            print("del neww"+str(wordsold))
            print("del coln="+str(colold1))             
            d2=d2+lcount
            lcount=lcount+1
            wordsold[d1]=newwords[l-i-1]
            print("The "+str(i)+"th address is "+str(d2)+" ," "move "+ str(d2+1)+"th panel")
            ardmov="mo"+str(d2+1)
            seri(ardmov)
        #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#convert the word from picture
def imgtoword(img):
    text = pytesseract.image_to_string(img)
    return text

def thre(gray):
    ret,imgt=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    imgt = cv2.bitwise_not(imgt)
    imgt = cv2.erode(imgt, None, iterations=1)
    imgt = cv2.dilate(imgt, None, iterations=1)
    #cv2.imshow("Threshold", imgt)
    return imgt

# identify the panel color
def color(img):
    co=cv2.mean(img)
    print("b="+str(co[0])+" g="+str(co[1])+" r="+str(co[2]))
    if co[0]>190 and co[1]>190:
# 1 represent white
        return 1
    else:
    #elif co[0]<50 and co[1]<50 and co[2]<50:
# 0 represent black
        return 0
    #else:
        
        #return 2

def nothing(x):
    pass
#say "I don't understand"
def xund():
    #speaker.Speak("I don't understand, please say it again")
    talk("xund.wav")

#say "" I got it    
def conf():
    #speaker.Speak("Okay, got it")
    talk("got it.wav")

# find word from vlist, if any, return the first word's address, if not, return 10    
def findv(stc,vlist):
    for i in range(len(vlist)):
        m=re.findall(str(vlist[i]),str(stc))
        if m:
            return i
    return 10


#find exposed color number, return white array and black array
# new add
def finda(new,c1,c2,assu):   
    whi =[]
    blk =[]
    for i in range(len(c1)):
        if c1[i]==1:
            whi.append(new[i])
        elif c1[i]==0:
            blk.append(new[i])
    for i in range(len(c2)):
        if assu[i] != -1:
            if c2[i]==1:
                whi.append(assu[i])
            elif c2[i]==0:
                blk.append(assu[i])
                   
    return whi,blk

#listen to kid choose the panel, return the panel serial number        
def panel_choosing():
    global nonrec
    stc=" "
    plist=[r"zero",r"first",r"second",r"third",r"fourth"]
    plistn=[r"0",r"1st",r"2nd",r"3rd",r"4th"]
    with mic as source:    
        print("Please select the panel you want to guess, 1st,2nd,3rd or 4th?")
        r.adjust_for_ambient_noise(source)
        print("0")
        audio = r.record(source,duration=7)
        print("finish")
    try:
        stc=str.lower(r.recognize_google(audio))
        print("You said " + stc) 
    except sr.UnknownValueError:
        #xund()
        print("xund")
        #nonrec=nonrec+1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    pc=findv(stc,plist)
    if pc==10:
        pc=findv(stc,plistn)
    print("panel choose is "+str(pc))
    return pc

#listen to kid guessing the panel number, return the number 
def guessing():
    global nonrec
    stc=" "
    glist=[r"zero",r"one",r"two",r"three",r"fo",r"five"]
    glistn=[r"0",r"1",r"2",r"3",r"4",r"5"]
    with mic as source:    
        print("Please tell me your assumption, the number should be ranged from zero to five")
        r.adjust_for_ambient_noise(source)
        print("1")
        audio = r.record(source,duration=7)
        print("finish")
    try:
        stc=r.recognize_google(audio)
        print("You said " + stc) 
    except sr.UnknownValueError:
        #xund()
        print("xund")
        #nonrec=nonrec+1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    sj=findv(stc,glist)
    if sj==10:
        sj=findv(stc,glistn)
    return sj

#Since the kid's guessing is wrong, tell the robot the panel serial number he will flip
def flip_panel_serial():
    stc=" "
    plist=[r"zero",r"first",r"second",r"third",r"fourth"]
    plistn=[r"0",r"1st",r"2nd",r"3rd",r"4th"]
    with mic as source:    
        print("Please tell me which panel you will flip")
        r.adjust_for_ambient_noise(source)
        print("0")
        audio = r.record(source,duration=4)
        print("finish")
    try:
        stc=r.recognize_google(audio)
        print("You said " + stc) 
    except sr.UnknownValueError:
        #xund()
        print("xund")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    pc=findv(stc,plist)
    if pc==10:
        pc=findv(stc,plistn)
    print("panel choose is "+str(pc))
    return pc

#Since the kid's guessing is wrong, tell the robot the number of the fliped panel
def flip_panel_number():
    stc=" "
    glist=[r"zero",r"one",r"two",r"three",r"fo",r"five"]
    glistn=[r"0",r"1",r"2",r"3",r"4",r"5"]
    with mic as source:    
        print("Please tell me the number on the panel")
        r.adjust_for_ambient_noise(source)
        print("1")
        audio = r.record(source,duration=4)
        print("finish")
    try:
        stc=r.recognize_google(audio)
        print("You said " + stc) 
    except sr.UnknownValueError:
        #xund()
        print("xund")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    sj=findv(stc,glist)
    if sj==10:
        sj=findv(stc,glistn)
    return sj

    

#input mcount and kcount, after the kid plays one turn, return the new mcount and kcount
def kid_turn(md,kd):
    global nonrec
    global code
    global coden
    #speaker.Speak("Please select the panel you want to guess")
    talk("selectpanel.wav")    
    #time.sleep(1)
    # choosing the panel he wants to guess
    p=panel_choosing()
    while True:
        if p==10 or p==0 :            #if the robot hasn't understanded it, rechoose it
            xund()
            nonrec=nonrec+1
            print(nonrec)
            if nonrec>=2:
                PGUI(20)
                while True:
                    if code>-1:
                        p=code
                        code=-1
                        break
                nonrec=0
                PGUI(0)
            else:
                p=panel_choosing()
        else:
            break                    #if understand, go to guessing
    nonrec=0
    #speakof="Please tell me your assumption"
    #PGUI(21)
    #speaker.Speak(speakof)
    talk("assumque.wav")
    #time.sleep(1)
    g=guessing()                    #g is the guessing result
    print ("the guessing number is "+str(g))
    print(" the corresponding panel number is "+ str(newwords[p-1]))
    while True:
        if g==10:                       #if the robot hasn't understanded it, reguesse it
            xund()
            nonrec=nonrec+1
            print(nonrec)
            if nonrec>=2:
                PGUI(21)
                while True:
                    if coden>-1:
                        g=coden
                        coden=-1
                        break
                nonrec=0
                PGUI(0)
                #g=coden
            else:
                g=guessing()
        else:
            break                      #if understand, go to comparing
    nonrec=0
    if str(newwords[p-1])==str(g):     #if the guessing is right, robot says "yes, you are right", mcount+1
        print("panel number is "+ str(g))
        #speaker.Speak("Yes, you are right")
        talk("yes.wav")
        seri("tic"+str(p))
        print("Yes, kid is right, m+1")
        #time.sleep(1)
        #speaker.Speak("Now it's my turn")
        talk("itsmyturn.wav")
        md=md+1
        kd=kd
        print("True")
        print("Mcount="+ str(md))
        print("Kcount="+ str(kd))
    else:
        #speaker.Speak("Oopus, you are wrong, please flip one of your unrevealed panel")  #if the guessing is wrong, robot says "no, you are wrong", kcount+1
        talk("youarewrong.wav")
        print("No, kid is wrong, k+1")
        #time.sleep(1)
        kd=kd+1
        md=md
        #print("False")
        print("Mcount="+ str(md))
        print("Kcount="+ str(kd))
 

#Asking kid which panel to flip       
        #speaker.Speak("Please tell me which panel you will flip")
        talk("wrongflip.wav")
        #PGUI(20)
        #time.sleep(1)
        ps=flip_panel_serial()
        while True:
            if ps==10 or ps==0 :            #if the robot hasn't understanded it, rechoose it
                xund()
                nonrec=nonrec+1
                print(nonrec)
                if nonrec>=2:
                    PGUI(20)
                    while True:
                        if code>-1:
                            ps=code
                            code=-1
                            break
                    nonrec=0
                    PGUI(0)
                else:
                    ps=panel_choosing()
                #ps=panel_choosing()
            else:
                break
        nonrec=0
#Asking kid the panel number
        #speakof="Please tell me the number on the panel"
        #PGUI(21)
        #speaker.Speak(speakof)
        talk("wrongnumonthep.wav")
        #time.sleep(1)
        pn=flip_panel_number()                    #pn represents for flipped panel number 
        print ("the flipped panel number is "+str(pn))
        #print(" the corresponding panel number is "+ str(newwords[p-1]))
        while True:
            if pn==10:                       #if the robot hasn't understanded it, reguesse it
                xund()
                nonrec=nonrec+1
                print(nonrec)
                if nonrec>=2:
                    PGUI(21)
                    while True:
                        if coden>-1:
                            pn=coden
                            coden=-1
                            break
                    nonrec=0
                    PGUI(0)
                else:
                    pn=flip_panel_number() 
            else:
                #speaker.Speak("Okay, got it. Now it's my turn")
                talk("wrongmyturn.wav")
                #time.sleep(1)
                break  
        assume[ps-1]=pn
        nonrec=0
    print("assume= "+ str(assume))
        
       # tell robot panel and  number
        

    return md,kd

#After the robot makes assumption, identify if right or wrong according to kid's answer, if right, return 0,1,2,
# if wrong, return 3,4,5, if not understand, return 10 (using findv())
def ans():
    stc=" "
    plist=[r"yes",r"true",r"right",r"no",r"false",r"wrong"]
    with mic as source:
        print("Please tell me if I am right or wrong")
        r.adjust_for_ambient_noise(source)
        print("0")
        audio = r.record(source,duration=4)
        print("finish")
    try:
        stc=str.lower(r.recognize_google(audio))
        print("You said " + stc) 
    except sr.UnknownValueError:
        #xund()
        print()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    sj=findv(stc,plist)
    print(sj)
    return sj

# generate which the kid's panel the robot wants to choose, the panel cannot be exposed , this is done by seeing if 
# assume[i]=-1, if -1, then return n, this is used for machine turn, for the robot to choose panel
def ran(assume):
    while True:
        n=random.choice([1,2,3,4])
        if assume[n-1]==-1:
            break
    print("n=" +str(n))
    return n

#generate the robot's assumption,the guessing can't be the number that already exposed
def rannum(assume):
    while True:
        m=random.choice([0,1,2,3,4,5])        
        b=findv(m,assume)
        if b==10:
            return m

#When robot made wrong assumption, expose one panel
#Asking the kid which panel he want to know
#flip it
def robot_wrong():
    global code
    global nonrec
    print("robot wrong")
    rw=flip_panel_serial()
    while True:
        if rw==10 or rw==0 :            #if the robot hasn't understanded it, rechoose it
            xund()
            #rw=panel_choosing()
            nonrec=nonrec+1
            print(nonrec)
            if nonrec>=2:
                PGUI(20)
                while True:
                    if code>-1:
                        rw=code
                        code=-1
                        break
                nonrec=0
                PGUI(0)
            else:
                rw=panel_choosing()
        else:
            conf()
            time.sleep(1)
            #speaker.Speak("Now it's your turn")
            talk("yourturn")
            break   
    print("Flip "+str(rw)+ "th panel")
    nonrec=0
    ardtic="tic"+str(rw)
    seri(ardtic)
    
            

def machine_turn(mt,kt):
    global nonrec
    global codea
    #find black and white array
    white,black=finda(newwords,colold,col2,assume)
    print("white="+str(white))
    print("black=" +str(black))
    #....................................
    
    n=ran(assume)
    if n==1:
        select="first"
        print(select)
    if n==2:
        select="second"
        print(select)
    if n==3:
        select="third"
        print(select)
    if n==4:
        select="fourth"
        print(select)
    #speaker.Speak("I choose"+ str(select)+ " panel")
    talk("ichoose.wav")
    talk(str(n)+"st.wav")
    talk("panel.wav")
    print("I choose "+ str(select)+ " panel")
    
    #find out the color of the correspond panel, if col2[n-1]=1, then that is a white panel, 
    # if col2[n-1]=0, then that is a black panel
    if col2[n-1]==1:
        m=rannum(white)
        print("white")
    elif col2[n-1]==0:
        m=rannum(black)
        print("black")
    
    #m=rannum(assume)
    print("m=" +str(m))
    if m==0:
        num="zero"
    if m==1:
        num="one"
    if m==2:
        num="two"
    if m==3:
        num="three"
    if m==4:
        num="four"
    if m==5:
        num="five"    
    #speaker.Speak("I am guessing the number is "+ str(num))
    talk("iguessthenumis.wav")
    talk(str(m)+".wav")
    print("I am guessing the number is "+ str(num))
    #speaker.Speak("Please tell me if I am right or wrong")
    talk("imiright.wav")
    #PGUI(22)
    #time.sleep(1)
    a=ans()
    while True:
        if a==10:
            xund()
            nonrec=nonrec+1
            print(nonrec)
            if nonrec>=2:
                PGUI(22)
                while True:
                    if codea>-1:
                        a=codea
                        codea=-1
                        break
                nonrec=0
            else:
                a=ans()
        else:
            break
    nonrec=0
    if a==0 or a==1 or a==2:
        #speaker.Speak("Haha, got you")
        talk("gotyou.wav")
        #time.sleep(1)
        #speaker.Speak("Now it's your turn")
        talk("yourturn.wav")
        #time.sleep(1)
        kt=kt+1
        assume[n-1]=m       #update the exposed kid's code
        print ("kcount=" +str(kt))
        print("assume=" +str(assume))
        PGUI(10)
        #speaker.Speak("Great!")
        #time.sleep(2)        
    if a==3 or a==4 or a==5:       
        mt=mt+1
        print ("mcount=" +str(mt))
        print("assume=" +str(assume))
        PGUI(11)
        #speaker.Speak("Oops, please tell me which panel of mine do you want to flip")
        talk("whichpanelofmineflip.wav")        
        #time.sleep(1)
        robot_wrong()
    return mt,kt


#The camera turn to robot's panel and capture the picture named as "screenshot.jpg"
# Send code to serial port, and receiving code from serial port
def turn_to_robot(count):
    print("read robot's own panels")
    #seri("rec")
    while cap.isOpened():
        count=count+1
        ret,img = cap.read()
        #cv2.imshow('Test',img)
        if count==100:  
            cv2.imwrite("screenshot.jpg", img)
            break
 # obtain col1 array, return status       
def read_robot_color(sta):
    print("read robot's panels color")
    img = cv2.imread("screenshot.jpg")  
    #using pan.jpg to obtain the color, should be replaced later
    #gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray", gray)
    imga=img[186:208, 208:230]  
    #cv2.imshow("imga",imga)
    co=color(imga)
    print("r1=" +str(co))
    colold[0]=co
    colold1[0]=co
    print("color1 array="+ str(colold))
    imgb=img[156:180, 260:285]    
    co=color(imgb)
    print("r2=" +str(co))
    colold[1]=co
    colold1[1]=co
    print("color1 array="+ str(colold))
    imgc=img[110:122, 378:391]    
    co=color(imgc)
    print("r=" +str(co))
    colold[2]=co
    colold1[2]=co
    print("color1 array="+ str(colold))
    imgd=img[82:93, 462:473]    
    co=color(imgd)
    print("r=" +str(co))
    colold[3]=co
    colold1[3]=co
    print("color1 array="+ str(colold))
    sta=1
    return sta

#analyze the captured picture, img to word, obtain newwords array
def read_robot_number(sta):
    #speaker.Speak("read robot panel number")
    print("read robot panel number")
    mnum=[]
    ccol=[]
    scani=0
    #iread = cv2.imread("shift2.jpg")
    while cap.isOpened():
        ret,iread = cap.read()
        scani=scani+1
    #imgf=iread[450:900,400:700]
    #gray= cv2.cvtColor(iread,cv2.COLOR_BGR2GRAY)
    #imgt=thre(gray)
    #cropImg = imgt[134:242,180:275] 
    #if imgt.any():
        #cv2.imshow("screenshot",imgt )
    #cv2.imshow("s",iread )
    #cv2.imshow("card",cropImg)
    #words=imgtoword(imgt)
        mnum,ccol,lens=scan(iread,mnum,ccol)
        print(len(mnum))
        print(scani)
        if scani==500:
            words=[1,2,4,5]
            break  
        if len(mnum)==4:
            words=mnum
            break
    #speaker.Speak("Obtaining infomation successfully")
    time.sleep(1)
    print(words)
    #speaker.Speak("Please wait for me to place panels in order ")
    
    #colnew is the sorted robot color array
    if words[0]<words[1] and words[1]<words[2] and words[2]<words[3]:
        print("no need to sort")
        newwords=words
    else:
        newwords,colnew =bubble_sort(list(words),colold)
        print("11111111111colnew="+str(colnew))
        print("wordsold= "+str(list(wordsold)))
        print("colnew=" +str(colnew))
        print("newwords= "+str(newwords))
        print("colnew= "+str(colnew))        
        find_address(newwords,colnew)
        
    #step=2
    sta=2
    print("step 2")
    return sta, newwords

# Send code to serial port to move the camera to kid version
#capture the picture of kid's panel
#Obtainning col2
def read_kid_color(count1,sta):
    print("turn to kid's panel")
    #seri("reck")
    while cap.isOpened():
        count1=count1+1
        #print(count1)
        ret,img = cap.read()
        #cv2.imshow('Test',img)
        if count1==100:  
            cv2.imwrite("kid.jpg", img)
            break            
    #speaker.Speak("read kid's panels color")
    print("read kid's panels color")
    imgg = cv2.imread("kid.jpg")  #using pan.jpg to obtain the color, should be replaced later
    #gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray", gray)
    print("1")
    imgo=imgg[226:240, 240:257]  
    #cv2.imshow("imga",imga)
    co2=color(imgo)
    print("r1=" +str(co2))
    col2[0]=co2
    print("color2 array="+ str(col2))
    imgp=imgg[226:240, 275:287]    
    co2=color(imgp)
    print("r2=" +str(co2))
    col2[1]=co2
    print("color2 array="+ str(col2))
    imgq=imgg[226:240, 305:320]    
    co2=color(imgq)
    #print("r=" +str(co2))+
    col2[2]=co2
    print("color2 array="+ str(col2))
    imgr=imgg[226:240, 334:345]    
    co2=color(imgr)
    print("r=" +str(co2))
    col2[3]=co2
    print("color2 array="+ str(col2))
    sta=3
    return sta

wordsold=[-1,-1,-1,-1]
newwords=[-1,-1,-1,-1]
colold=[-1,-1,-1,-1]
colold1=[-1,-1,-1,-1]
colnew=[-1,-1,-1,-1]
col2=[-1,-1,-1,-1]
assume=[-1,-1,-1,-1]  
status=0
sta=0
step=1
drawing=0
count=0
count1=0
kcount=0
mcount=0 
p=0
g=0

port_list = list(serial.tools.list_ports.comports())
if len(port_list) == 0:
   print('No serial port located')
else:
    for i in range(0,len(port_list)):
        try:        
            serial_port="COM"+str(port_list[i])[3]
            ser = serial.Serial(serial_port)
            print(serial_port)
            break
        except:
            pass
        try:        
            serial_port="COM"+str(port_list[i])[3]+str(port_list[i])[4]
            ser = serial.Serial(serial_port)
            print(serial_port)
            break
        except:
            pass
            
#speaker      
speaker=win32com.client.Dispatch('SAPI.SpVoice')
element = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3)) 
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
r = sr.Recognizer()
mic = sr.Microphone()
#time.sleep(1)
print("ready")
#speaker.Speak("System Initiated")
#time.sleep(1)
#stc=" " 
sstart=-1
talk("systemi.wav")
PGUI(99)
while True:
    stc=""
    with mic as source:    
        print("Say ready!")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source,duration=5)
        print("finish")
    try:
        stc=r.recognize_google(audio)
        print("You said " + stc) 
    except sr.UnknownValueError:
        xund()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    sstart=findv(str.lower(stc),["ready","ok","begin"])
    print(sstart)
    if sstart==0:
        print("ok")
        break
    else:
        nonrec=nonrec+1
        if nonrec==3:
            PGUI(23)
            sstart=codeready
            codeready=-1
            break

nonrec=0 
while True:
    if step==1:
        PGUI(0)      
        #try:
        if status==0:
            #cv2.waitKey (0)
            #speaker.Speak("Drawing the panels")
            talk("drawpanels.wav")
            print("step 1")
            seri("take")
            status=1
        if status==1:            
            #camera turn to robot and read its panel color
            if sta==0:
                seri("rec")
                turn_to_robot(count)
                sta=read_robot_color(sta)
                print("sta1=" +str(sta))
            #read robot's panel nomber and bubble sort it
            if sta==1:
                sta, newwords=read_robot_number(sta)
                print("sta2=" +str(sta))
                print("newwords=" +str(newwords))
                seri("recf")
                #Read kid's panel color        
            if sta==2:
                seri("reck")
                sta=read_kid_color(count1,sta)
                print("sta3=" +str(sta))
                seri("reckf")
                status=0
                step=2
                

        #except:
            #print("step 1 error")
            #pass        
    if step==2:
        PGUI(0)
        # kid's turn
        if status==0:        
            mcount,kcount=kid_turn(mcount,kcount)
            print("kcount=" +str(kcount))
            print("mcount=" +str(mcount))
            status=1
            if kcount==4:
                PGUI(12)
                #speaker.Speak("Haha, you lose the game, I win")
                talk("youlose.wav")
                print("Haha, you lose the game, I win")
                step=3
                status=3
            elif mcount==4:
                PGUI(13)
                #speaker.Speak("Okay, you win, congrajulations")
                talk("youwin.wav")
                talk("desm.wav")                 
                print("Okay, you win, congrajulations")
                step=3
                status=3
            else:
                print("Mcontinue")
        #machine's turn
        if status==1:
            mcount,kcount=machine_turn(mcount,kcount)
            print("mcount=" +str(mcount))
            print("kcount=" +str(kcount))
            status=0
            if kcount==4:
                PGUI(12)
                #speaker.Speak("Haha, you lose the game, I win")
                talk("youlose.wav")                
                print("Haha, you lose the game, I win")
                step=3
            elif mcount==4:
                PGUI(13)
                #speaker.Speak("Okay, you win, congrajulations")
                talk("youwin.wav")
                talk("desm.wav")                 
                print("Okay, you win, congrajulations")
                step=3
            else:
                print("Kcontinue")

    if step==3:   #cv2.destroyAllWindows()  
        #PGUI(0)
        print("step 3")
        status=0
        #speaker.Speak("Do you want to play another round?")
        talk("anotherround.wav")
        stc=" "
        plist=[r"yes",r"true",r"right",r"no",r"false",r"wrong"]
        with mic as source:
            print("Do you want to play another round?")
            r.adjust_for_ambient_noise(source)
            print("0")
            audio = r.record(source,duration=10)
            #audio = r.listen(source, duration=10)
            print("finish")
        try:
            stc=str.lower(r.recognize_google(audio))
            print("You said " + stc) 
        except sr.UnknownValueError:
            #xund()
            print(xund)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        s3a=findv(stc,plist)
        print(s3a)
        while True:
            if s3a==10:
                xund()
                nonrec=nonrec+1
                print(nonrec)
                if nonrec>=2:
                    PGUI(22)
                    while True:
                        if codea>-1:
                            s3a=codea
                            codea=-1
                            break
                    nonrec=0
                else:
                    s3a=ans()
            else:
                break
        nonrec=0
        if s3a==0 or s3a==1 or s3a==2:
            step=1
            status=0
            sta=0
            wordsold=[-1,-1,-1,-1]
            newwords=[-1,-1,-1,-1]
            colold=[-1,-1,-1,-1]
            colold1=[-1,-1,-1,-1]
            colnew=[-1,-1,-1,-1]
            col2=[-1,-1,-1,-1]
            assume=[-1,-1,-1,-1]                          
            drawing=0
            count=0
            count1=0
            kcount=0
            mcount=0 
            p=0
            g=0
        if s3a==3 or s3a==4 or s3a==5:       
            break
cap.release()
cv2.waitKey (0)
cv2.destroyAllWindows() 
            
            
            
