#GUI to run Hspice in linux

from Tkinter import *
import subprocess
from subprocess import *


global flag
flag=1
out=None



def button1_push():
    global tBox1
    global destbox
    global fifthframe
    global sixthframe
    txt1=tBox1.get()

    if (flag==0):
        out=txt1
    else:
        destext = destbox.get()
        out=destext
    print("the file is "+txt1)
    command="hspice "+"-i "+ txt1+" -o "+out+".lis"
    #print(command)
    #str=subprocess.call(command,shell=True)
    #print (str)
    p=Popen(command,shell=True,stderr=PIPE,stdout=PIPE)
    out = p.stdout.read()
    err = p.stderr.read()
    print(out + "\n" + err + "\n" )
    status = Label(fifthframe,text=out,width=100, justify=CENTER, fg='Brown')
    status.pack()
    if err=="":
        errout="Simulation Succesfull!!!!"
    else:
        errout=err
    error = Label(sixthframe,text=errout, width=100, justify=CENTER, fg='Red')
    error.pack()






def create_tbox(parent):
    global tBox1
    tBox1= Entry(parent,width=50)
    tBox1.pack(side=LEFT)

def yesradio():
    global flag
    print("yes")
    flag=0

def noradio():
    global thirdframe
    global destbox
    print("no")
    desttext=Label(thirdframe,text="Output File(Full Path): ")
    desttext.pack(side=LEFT)

    destbox=Entry(thirdframe)
    destbox.pack(side=LEFT)

def main():
    global tBox1
    global thirdframe
    global destbox
    global out
    global fifthframe
    global sixthframe

    root=Tk()
    root.title("UI_HSPICE_LINUX")

    w = Label(root, text="Welcome to Hspice UI")
    w.pack()

    topframe=Frame(root)
    topframe.pack(side=TOP)

    buttomframe=Frame(root)
    buttomframe.pack(side=TOP)

    thirdframe=Frame(root)
    thirdframe.pack(side=TOP)

    fourthframe=Frame(root)
    fourthframe.pack(side=TOP)

    fifthframe=Frame(root)
    fifthframe.pack(side=TOP)

    sixthframe = Frame(root)
    sixthframe.pack(side=TOP)


    fileText=Label(topframe,text="Input File(Full Path): ")
    fileText.pack(side=LEFT)

    create_tbox(topframe)


    selection=Label(buttomframe,text="Do you want to store output file in same folder?")
    selection.pack(side=LEFT)

    rb1=Button(buttomframe,text="Yes",command=yesradio)
    rb1.pack(side=LEFT,anchor=W)

    rb2 = Button(buttomframe, text="No",command=noradio)
    rb2.pack(side=LEFT,anchor=W)

    button1=Button(fourthframe,text="simulate",command=button1_push)
    button1.pack(side=TOP)






    cright=Label(root,text="developed by : Subed Lamichhane",fg='Blue',justify=CENTER)
    cright.pack()





    root.mainloop()

main()
