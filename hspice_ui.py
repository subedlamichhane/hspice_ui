#GUI to run Hspice in linux

from Tkinter import *
import subprocess


global flag
flag=1

def button1_push():
    global tBox1
    global destbox
    txt1=tBox1.get()

    if (flag==0):
        out=txt1
    else:
        destext = destbox.get()
        out=destext
    print("the file is "+txt1)
    command="hspice "+"-i "+ txt1+" -o "+out+".lis"
    print(command)
    subprocess.call(command,shell=True)

def create_tbox(parent):
    global tBox1
    tBox1= Entry(parent)
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

    root=Tk()

    w = Label(root, text="Welcome to Hspice gui for Centos")
    w.pack()

    topframe=Frame(root)
    topframe.pack(side=TOP)

    buttomframe=Frame(root)
    buttomframe.pack(side=TOP)

    thirdframe=Frame(root)
    thirdframe.pack(side=TOP)

    fourthframe=Frame(root)
    fourthframe.pack()


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


    root.mainloop()

main()