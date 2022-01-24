from __future__ import barry_as_FLUFL
from tkinter import *
import time
import sys
from tkinter import font
import pyautogui as pg
import keyboard

root=Tk()
#root.geometry('400x300')
root.title('Bot')

def get_time():
    timeVar=time.strftime("%H:%M:%S ")
    
    clock.config(text=timeVar)
    clock.after(200,get_time)

def pointer():

    while True:
        if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
            
            a=pg.position()
            mouse_position.after(100,pointer)

            if clicked.get() == 'Link':
                
                link_coor1.delete(0,END)
                link_coor1.insert(0,str(a[0])+","+str(a[1]))

                break

            elif clicked.get() == 'Cam':
                
                cam.delete(0,END)
                cam.insert(0,str(a[0])+","+str(a[1]))

                break

            elif clicked.get() == 'Mic':
                
                mic.delete(0,END)
                mic.insert(0,str(a[0])+","+str(a[1]))

                break

            elif clicked.get() == 'Join':
                
                join.delete(0,END)
                join.insert(0,str(a[0])+","+str(a[1]))

                break

            break

        elif keyboard.is_pressed('w') or keyboard.is_pressed('W'):
            mouse_position.config(text='')
            break

        else:
            a=pg.position()
            mouse_position.after(100,pointer)

            mouse_position.config(text=a)
            
            break


    return
    
def start():
    var6=timelater.get()

    timeVar=time.strftime("%H:%M:%S ")
    trueTime=time.strftime("%H:%M")
    
    clock.config(text=timeVar)

    if trueTime == var6:
        start_now()
    else:
        clock.after(1000,start)

    return

def start_now():

    stop=time.sleep(.5)

    var1=link.get()
    var2=link_coor1.get().split(",")
    var3=cam.get().split(",")
    var4=mic.get().split(",")
    var5=join.get().split(",")
    
    
    #print(coor2[0]+' '+coor2[1])
    pg.moveTo(int(var2[0]),int(var2[1]),.5)
    stop
    pg.click()
    pg.typewrite(var1,.02)
    stop
    pg.press('Enter')
    stop
    pg.moveTo(int(var3[0]),int(var3[1]),5)
    stop
    pg.leftClick()
    stop
    pg.moveTo(int(var4[0]),int(var4[1]))
    stop
    pg.leftClick()
    stop
    pg.moveTo(int(var5[0]),int(var5[1]))
    stop
    pg.leftClick()


    return

def default():

    link_coor1.delete(0,END)
    link_coor1.insert(0,'304,50')
    cam.delete(0,END)
    cam.insert(0,'511,565')
    mic.delete(0,END)
    mic.insert(0,'434,564')
    join.delete(0,END)
    join.insert(0,'999,431')

options=[
    'Link',
    'Cam',
    'Mic',
    'Join'
]

clicked=StringVar()
clicked.set(options[0]) 

link=Entry(root,width=30)
Link_text=Label(root,text='Google Meet Link',font=15)

link_coor1=Entry(root,width=30)
Link_coor_text1=Label(root,text='Link  (x,y):',font=15)

cam=Entry(root,width=30)
cam_text=Label(root,text='Cam  (x,y):',font=15)

mic=Entry(root,width=30)
mic_text=Label(root,text='Mic  (x,y):',font=15)

join=Entry(root,width=30)
join_text=Label(root,text='Join  (x,y):',font=15)

timelater=Entry(root,width=30)
timelater_text=Label(root,text='Time  (hh,mm):',font=15)

clock=Label(root, font=("Calibri",20),bg="grey",fg="white")

mouse_position=Label(root,font=("Calibri",10))

btn=OptionMenu(root,clicked,*options)

start_btn=Button(root,text='Start Bot',width=50,command=start)

set_btn=Button(root,text='Set',width=10,command=pointer)

default=Button(root,text='Default',width=10,command=default)




link.grid(column=1,row=0,padx=(10,0),pady=(10,0),columnspan=2)
Link_text.grid(column=0,row=0,pady=(10,0))

link_coor1.grid(column=1,row=1,padx=(10,0),pady=(10,0),columnspan=2)
Link_coor_text1.grid(column=0,row=1,pady=(10,0))

cam.grid(column=1,row=2,padx=(10,0),pady=(10,0),columnspan=2)
cam_text.grid(column=0,row=2,pady=(10,0))

mic.grid(column=1,row=3,padx=(10,0),pady=(10,0),columnspan=2)
mic_text.grid(column=0,row=3,pady=(10,0))

join.grid(column=1,row=4,padx=(10,0),pady=(10,0),columnspan=2)
join_text.grid(column=0,row=4,pady=(10,0))

timelater.grid(column=1,row=5,padx=(10,0),pady=(10,0),columnspan=2)
timelater_text.grid(column=0,row=5,pady=(10,0))

clock.grid(column=2,row=10,pady=(10,0),rowspan=2)

mouse_position.grid(column=0,row=11,pady=(10,0))

btn.grid(column=0,row=10,pady=(10))

default.grid(column=0,row=11,pady=(10,0))

set_btn.grid(column=1,row=10,pady=(10,0))

start_btn.grid(column=0,row=6,columnspan=3,pady=20,padx=10)

get_time()

root.mainloop()