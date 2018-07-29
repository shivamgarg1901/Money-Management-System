import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
######
def calctotal():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
    back.pack(side=RIGHT)
    label=Label(frm1,text='Total expense is ',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
    label.pack(side=TOP)
    conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    sum1=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisehealth"): 
            for j in range(len(i)):
                sum1+=i[j]
    except sqlite3.OperationalError:
        sum1=0
    sum2=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisedu"):
            for j in range(len(i)):
                sum2+=i[j]
    except sqlite3.OperationalError:
        sum2=0
    sum3=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisebills"):
            for j in range(len(i)):
                sum3+=i[j]
    except sqlite3.OperationalError:
        sum3=0
    sum4=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisegr"):
            for j in range(len(i)):
                sum4+=i[j]
    except sqlite3.OperationalError:
        sum4=0
    sum5=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisemisc"):
            for j in range(len(i)):
                sum5+=i[j]
    except sqlite3.OperationalError:
        sum5=0
    sum6=0
    try:
        for i in cursor.execute("SELECT Amount FROM categoriseshop"):
            for j in range(len(i)):
                sum6+=i[j]
    except sqlite3.OperationalError:
        sum6=0
    sum7=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisetravel"):
            for j in range(len(i)):
                sum7+=i[j]
    except sqlite3.OperationalError:
        sum7=0
    sum8=0
    try:
        for i in cursor.execute("SELECT Amount FROM categorisefood"):
            for j in range(len(i)):
                sum8+=i[j]
    except sqlite3.OperationalError:
        sum8=0
    conn.commit()
    sumt=sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8
    msg=StringVar()
    label=Label(frm1,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
    msg.set(sumt)
    label.pack(side=TOP)


def total():
    
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm3=Frame(frm,bg='LEMONCHIFFON')   
    frm3.pack(side=TOP,expand=YES,fill=BOTH)
    frm4=Frame(frm,bg='LEMONCHIFFON')   
    frm4.pack(side=TOP,expand=YES,fill=BOTH)
    back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
    back.pack(side=RIGHT)

    def calc():

        
        #global ms,ys
        try:
            mnth=int(ms.get())
            yr=int(ys.get())
        except ValueError:
            messagebox.showinfo("OOPS!!","Enter an integer")
            ms.delete(0,END)
            ys.delete(0,END)
            return
        if(not(mnth>0 and mnth<13 and yr>=1950 and yr<=2099)):
            messagebox.showinfo("OOPS!!","Data out of range")
            ms.delete(0,END)
            ys.delete(0,END)
            return
        label=Label(frm3,text='Total expense is ',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        conn = sqlite3.connect("database11.db") 
        cursor = conn.cursor()
        mnth=ms.get()
        yr=ys.get()
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisehealth WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum1+=(i[j])
        except sqlite3.OperationalError:
            sum1=0
        sum2=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisedu WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum2+=i[j]
        except sqlite3.OperationalError:
            sum2=0
        sum3=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisebills WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum3+=i[j]
        except sqlite3.OperationalError:
            sum3=0
        sum4=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisegr WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum4+=i[j]
        except sqlite3.OperationalError:
            sum4=0
        sum5=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisemisc WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum5+=i[j]
        except sqlite3.OperationalError:
            sum5=0
        sum6=0
        try:
            for i in cursor.execute("SELECT Amount FROM categoriseshop WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum6+=i[j]
        except sqlite3.OperationalError:
            sum6=0
        sum7=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisetravel WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum7+=i[j]
        except sqlite3.OperationalError:
            sum7=0
        sum8=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisefood WHERE Month='%s' AND Year='%s'"%(mnth,yr)):
                for j in range(len(i)):
                    sum8+=i[j]
        except sqlite3.OperationalError:
            sum8=0
        conn.commit()
        sumt=sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sumt)
        label.pack(side=TOP)



    
    msg=StringVar()
    label=Label(frm1,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
    msg.set('Enter month')
    label.pack(side=TOP)
    global ms,ys
    ms=Entry(frm1)
    ms.pack(side=TOP)
    msg=StringVar()
    label=Label(frm1,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
    msg.set('Enter year')
    label.pack(side=TOP)
    ys=Entry(frm1)
    ys.pack(side=TOP)
    button=Button(frm2,text='Calculate total',command=calc)
    button.pack(side=TOP)

    
    
def optionslogin():
    global frm
    frm.forget()
    coptions()

def addexpenseshealth():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisehealth(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisehealth(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisehealth"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisehealth"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()

def addexedu():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisedu(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisedu(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisedu"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisedu"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
    
def addexfood():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisefood(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisefood(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisefood"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisefood"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
    
def addextravel():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisetravel(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisetravel(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisetravel"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisetravel"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
 
def addexshop():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categoriseshop(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categoriseshop(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categoriseshop"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categoriseshop"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
    
def addexgr():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisegr(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisegr(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisegr"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisegr"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
    
def addexbills():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisebills(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisebills(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisebills"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisebills"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
    
def addexmisc():
    global frm
    frm.forget()
    #global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    frmx=Frame(frm,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=YES,fill=BOTH)
    frm0=Frame(frm,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=YES,fill=BOTH)
    frm1=Frame(frm,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=YES,fill=BOTH)
    frm2=Frame(frm,bg='LEMONCHIFFON')   
    frm2.pack(side=TOP,expand=YES,fill=BOTH)
    frm11=Frame(frm1,bg='LEMONCHIFFON')
    frm11.pack(side=LEFT,expand=YES,fill=BOTH)
    frm12=Frame(frm1,bg='LEMONCHIFFON')
    frm12.pack(side=LEFT,expand=YES,fill=BOTH)
    frm13=Frame(frm1,bg='LEMONCHIFFON')
    frm13.pack(side=LEFT,expand=YES,fill=BOTH)
    frm14=Frame(frm1,bg='LEMONCHIFFON')
    frm14.pack(side=LEFT,expand=YES,fill=BOTH)
    def datacat():
        global d,m,y,a,z
        global i
        i=2

        def add():
            global d,m,y,a,z
            d=Entry(frm2)
            global i
            d.grid(row=i,column=0)
            m=Entry(frm2)
            m.grid(row=i,column=1)
            y=Entry(frm2)
            y.grid(row=i,column=2)
            a=Entry(frm2)
            a.grid(row=i,column=3)
            z=Entry(frm2)
            z.grid(row=i,column=4)
   
        def done():
            global q
            global d,m,y,a,z
            if((d.get()=='' or m.get()=='' or y.get()=='' or a.get()=='' or z.get()=='')):
                messagebox.showinfo('Warning','Please enter data')
            else:
                def click():
                    
                    Date=int(d.get())
                    Month=int(m.get())
                    Year=int(y.get())
                    Amount=int(a.get())
                    Details=z.get()
                    if((Date<1 or Date>31) or (Year<=1950 or Year>=2099)or Month<1 or Month>12):
                        messagebox.showinfo("OOPS!!","Invalid data")
                        d.delete(0,END)
                        m.delete(0,END)
                        y.delete(0,END)
                        a.delete(0,END)
                        z.delete(0,END)
                    else:
                        if(Month==2 or Month==4 or Month==6 or Month==9 or Month==11):
                            if(Date==31):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Date==30):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            elif(Month==2 and Year%4!=0 and Date>28):
                                messagebox.showinfo("OOPS!!","Invalid data")
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
                            else:
                                global i
                                q=[]
                        #click()
                                q.append(d.get())
                                q.append(m.get())
                                q.append(y.get())
                                q.append(a.get())
                                q.append(z.get())
                                label1=Label(frm2,text=q[0],fg='BLUE',width=17)
                                label1.grid(row=i,column=0)
                                label2=Label(frm2,text=q[1],fg='BLUE',width=17)
                                label2.grid(row=i,column=1)
                                label3=Label(frm2,text=q[2],fg='BLUE',width=17)
                                label3.grid(row=i,column=2)
                                label3=Label(frm2,text=q[3],fg='BLUE',width=17)
                                label3.grid(row=i,column=3)
                                label3=Label(frm2,text=q[4],fg='BLUE',width=17)
                                label3.grid(row=i,column=4)
                #click()
                                i+=1
                                d.delete(0,END)
                                m.delete(0,END)
                                y.delete(0,END)
                                a.delete(0,END)
                                z.delete(0,END)
        
                                conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
                                cursor = conn.cursor() 
                        # insert some data
                                Amount=int(Amount)
                                sql="INSERT INTO categorisemisc(Date,Month,Year,Amount,Details) VALUES('%s','%s','%s','%d','%s')"%(Date,Month,Year,Amount,Details)
                                cursor.execute(sql)
                        # save data to database
                                conn.commit()
                                
                click()
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=80)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=80)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm1,text='Enter Information!',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.grid(row=0,column=0)
        label1=Label(frm2,text='Date',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=0)
        label1=Label(frm2,text='Month',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=1)
        label1=Label(frm2,text='Year',bg='LEMONCHIFFON',font=15)
        label1.grid(row=0,column=2)
        label2=Label(frm2,text='Amount',bg='LEMONCHIFFON',font=15)
        label2.grid(row=0,column=3)
        label3=Label(frm2,text='Details',bg='LEMONCHIFFON',font=15)
        label3.grid(row=0,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=0)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=1)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=1,column=2)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=1,column=4)
        global d,m,y,a,z
        d=Entry(frm2)
        d.grid(row=i,column=0)
        m=Entry(frm2)
        m.grid(row=i,column=1)
        y=Entry(frm2)
        y.grid(row=i,column=2)
        a=Entry(frm2)
        a.grid(row=i,column=3)
        z=Entry(frm2)
        z.grid(row=i,column=4)
        label1=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label1.grid(row=i+1,column=0)
        label2=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label2.grid(row=i+1,column=1)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=2)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=3)
        label3=Label(frm2,text='',bg='LEMONCHIFFON',font=15)
        label3.grid(row=i+1,column=4)
        button1=Button(frm3,text='Add New',command=add,width=10)
        button1.pack(side=LEFT,expand=YES)
        button2=Button(frm3,text='Done',command=done,width=10)
        button2.pack(side=RIGHT,expand=YES)
        button3=Button(frm3,text='View All',width=10,command=dataview)
        button3.pack(side=LEFT,expand=YES)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall,width=10)
        back.pack(side=RIGHT)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor() 
        cursor.execute("CREATE TABLE categorisemisc(Date,Month,Year,Amount INT(10),Details)")
        conn.commit()


    def dataview():
        global frm
        frm.forget()
        #global frm
        frm=Frame(logs,bg='LEMONCHIFFON')
        frm.pack(expand=YES,fill=BOTH)
        frmx=Frame(frm,bg='LEMONCHIFFON',height=50)
        frmx.pack(side=TOP,expand=YES,fill=BOTH)
        frm0=Frame(frm,bg='LEMONCHIFFON',height=50)
        frm0.pack(side=TOP,expand=YES,fill=BOTH)
        frm1=Frame(frm,bg='LEMONCHIFFON')
        frm1.pack(side=TOP,expand=YES,fill=BOTH)
        frm2=Frame(frm,bg='LEMONCHIFFON')
        frm2.pack(side=TOP,expand=YES,fill=BOTH)
        frm3=Frame(frm,bg='LEMONCHIFFON')
        frm3.pack(side=TOP,expand=YES,fill=BOTH)
        label0=Label(frm0,text='Your Details.',pady=50,bg='LEMONCHIFFON',font='Helvetica 30 bold italic')
        label0.pack(side=TOP)
        conn = sqlite3.connect("database11.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        #print
        i=10
        j=10
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=0,ipadx=150)
        label=Label(frm2,text="",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=1,ipadx=20)
        label=Label(frm2,text="DATE",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=2,ipadx=50)
        label=Label(frm2,text="MONTH",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=3,ipadx=50)
        label=Label(frm2,text="YEAR",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=4,ipadx=50)
        label=Label(frm2,text="AMOUNT",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=5,ipadx=50)
        label=Label(frm2,text="DETAILS",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON')
        label.grid(row=0,column=6,ipadx=50)
        back=Button(frmx,text="BACK",font="Times 20 bold",fg='BLUE',bg='LEMONCHIFFON',command=catcall)
        back.pack(side=RIGHT)

        i=1
        try:
            for row in cursor.execute("SELECT * FROM categorisemisc"):
                j=2
                for elem in row:
                    msg=StringVar()
                    label=Label(frm2,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
                    msg.set(elem)
                    label.grid(row=i,column=j)
                    j+=1
                i+=1
        except sqlite3.OperationalError:
            messagebox.showinfo("OOPS!!","No record in this table")
        label=Label(frm3,text='Total of this category',font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        label.pack(side=TOP)
        sum1=0
        try:
            for i in cursor.execute("SELECT Amount FROM categorisemisc"):
                for j in range(len(i)):
                    sum1+=i[j]
        except sqlite3.OperationalError:
            sum1=0
        msg=StringVar()
        label=Label(frm3,textvariable=msg,font = "Helvetica 15 bold italic",fg='BLACK',bg='LEMONCHIFFON')
        msg.set(sum1)
        label.pack(side=TOP)
        conn.commit()

    
    label=Label(frm0,text='What do you want!!',bg='LEMONCHIFFON',pady=50,font='Helvetica 30 bold italic')
    label.pack()
    button1=Button(frm12,text='Add',width=15,command=datacat)
    button1.pack()
    button2=Button(frm13,text='View',width=15,command=dataview)
    button2.pack()
    



def optionsignup():
    global frm
    frm.forget()
    coptions()

def catcall():
    global frm
    frm.forget()
    categories()

def categories():
    global frm1
    global frm
    
    frm.forget()
    #global frm
    frm=Frame(logs)
    frm.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    frmx=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm0=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm1=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm2=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm2.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm3=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm3.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm4=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm4.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm5=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm5.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm6=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm6.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm7=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm7.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm8=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm8.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm21=Frame(frm2,bg='LEMONCHIFFON')
    frm21.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm22=Frame(frm2,bg='LEMONCHIFFON')
    frm22.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm23=Frame(frm2,bg='LEMONCHIFFON')
    frm23.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm24=Frame(frm2,bg='LEMONCHIFFON')
    frm24.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm25=Frame(frm2,bg='LEMONCHIFFON')
    frm25.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm26=Frame(frm2,bg='LEMONCHIFFON')
    frm26.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm31=Frame(frm3,bg='LEMONCHIFFON')
    frm31.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm32=Frame(frm3,bg='LEMONCHIFFON')
    frm32.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm33=Frame(frm3,bg='LEMONCHIFFON')
    frm33.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm34=Frame(frm3,bg='LEMONCHIFFON')
    frm34.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm35=Frame(frm3,bg='LEMONCHIFFON')
    frm35.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm36=Frame(frm3,bg='LEMONCHIFFON')
    frm36.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm41=Frame(frm4,bg='LEMONCHIFFON')
    frm41.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm42=Frame(frm4,bg='LEMONCHIFFON')
    frm42.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm43=Frame(frm4,bg='LEMONCHIFFON')
    frm43.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm44=Frame(frm4,bg='LEMONCHIFFON')
    frm44.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm45=Frame(frm4,bg='LEMONCHIFFON')
    frm45.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm46=Frame(frm4,bg='LEMONCHIFFON')
    frm46.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)        
    frm51=Frame(frm5,bg='LEMONCHIFFON')
    frm51.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm52=Frame(frm5,bg='LEMONCHIFFON')
    frm52.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm53=Frame(frm5,bg='LEMONCHIFFON')
    frm53.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm54=Frame(frm5,bg='LEMONCHIFFON')
    frm54.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm55=Frame(frm5,bg='LEMONCHIFFON')
    frm55.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm56=Frame(frm5,bg='LEMONCHIFFON')
    frm56.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
   
    #...
    frm61=Frame(frm6,bg='LEMONCHIFFON')
    frm61.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm62=Frame(frm6,bg='LEMONCHIFFON')
    frm62.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm63=Frame(frm6,bg='LEMONCHIFFON')
    frm63.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm64=Frame(frm6,bg='LEMONCHIFFON')
    frm64.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm65=Frame(frm6,bg='LEMONCHIFFON')
    frm65.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm66=Frame(frm6,bg='LEMONCHIFFON')
    frm66.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    #...
    
    label=Label(frm1,text='Manage Your Budget',fg='BLACK',bg='LEMONCHIFFON',font = "Times 30 bold")
    label.pack(side=TOP)
    label1=Label(frm1,text='CATEGORIES',fg='BLACK',bg='LEMONCHIFFON',font = "Times 30 bold")
    label1.pack(side=TOP)
    button1=Button(frm23,text='Health',fg='BLACK',font="15",width=20,command=addexpenseshealth)
    button1.pack(side=TOP)
    button2=Button(frm24,text='Education',fg='BLACK',font="15",width=20,command=addexedu)
    button2.pack(side=TOP)
    button3=Button(frm33,text='Food',fg='BLACK',font="15",width=20,command=addexfood)
    button3.pack(side=TOP)
    button4=Button(frm34,text='Travel',fg='BLACK',font="15",width=20,command=addextravel)
    button4.pack(side=TOP)
    button5=Button(frm43,text='Shopping',fg='BLACK',font="15",width=20,command=addexshop)
    button5.pack(side=TOP)
    button6=Button(frm44,text='Groceries',fg='BLACK',font="15",width=20,command=addexgr)
    button6.pack(side=TOP)
    button7=Button(frm53,text='Bills',fg='BLACK',font="15",width=20,command=addexbills)
    button7.pack(side=TOP)
    button8=Button(frm54,text='Miscellaneous',fg='BLACK',font="15",width=20,command=addexmisc)
    button8.pack(side=TOP)
    button9=Button(frm63,text='TOTAL OF A MONTH',fg='BLACK',font="15",width=20,command=total)
    button9.pack(side=TOP)
    button10=Button(frm64,text='TOTAL',fg='BLACK',font="15",width=20,command=calctotal)
    button10.pack(side=TOP)
    back=Button(frmx,fg='BLACK',text='Back',font="Times 15 bold",padx=30,pady=5,command=optionsignup)
    back.pack(side=RIGHT)
    


def coptions():
    global frm
    frm=Frame(logs,bg='LEMONCHIFFON')
    frm.pack(expand=YES,fill=BOTH)
    fx=Frame(frm,bg='LEMONCHIFFON')
    fx.pack(side=TOP,expand=YES,fill=BOTH)
    f1=Frame(frm,bg='LEMONCHIFFON')
    f1.pack(side=TOP,expand=YES,fill=BOTH)
    f2=Frame(frm,bg='LEMONCHIFFON')
    f2.pack(side=TOP,expand=YES,fill=BOTH)
    f3=Frame(frm,bg='LEMONCHIFFON')
    f3.pack(side=TOP,expand=YES,fill=BOTH)
    f4=Frame(frm,bg='LEMONCHIFFON')
    f4.pack(side=TOP,expand=YES,fill=BOTH)
    f21=Frame(f2,bg='LEMONCHIFFON')
    f21.pack(side=LEFT,expand=YES,fill=BOTH)
    f22=Frame(f2,bg='LEMONCHIFFON')
    f22.pack(side=LEFT,expand=YES,fill=BOTH)
    f23=Frame(f2,bg='LEMONCHIFFON')
    f23.pack(side=LEFT,expand=YES,fill=BOTH)
    f31=Frame(f3,bg='LEMONCHIFFON')
    f31.pack(side=LEFT,expand=YES,fill=BOTH)
    f32=Frame(f3,bg='LEMONCHIFFON')
    f32.pack(side=LEFT,expand=YES,fill=BOTH)
    f33=Frame(f3,bg='LEMONCHIFFON')
    f33.pack(side=LEFT,expand=YES,fill=BOTH)
    label=Label(f22,text="MONEY MATTERS!!",font="Helvetica 30 bold",fg='BLUE',bg='LEMONCHIFFON')
    label.pack(side=TOP)
    b3=Button(f32,text='MANAGE YOUR BUDGET',font='Times 15 bold',fg='BLACK',bg='LIGHTGREEN',width=25,command=catcall)
    b3.pack(side=TOP,padx=65)

    
    
######

    ###########################################################
    
 
    #...
    
        
    
######

logs=Tk()
logs.configure(bg='LEMONCHIFFON')


def login():
    global frm
    frm=Frame(logs)
    def check():
        conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
        cursor = conn.cursor()
        cursor.execute("SELECT Username FROM signup")
        if(x1==f.get()):
            cursor.execute("SELECT Password FROM signup")
            conn.commit()
            if(x2==u.get()):
                messagebox.showinfo("Login","logged in successfully")
                optionsignup()
        else:
            conn.commit()
            messagebox.showinfo("Login","user does not exist")
            f.set("")
            u.set("")
            
    
    frm.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    frmx=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frmx.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm0=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm0.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm1=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm1.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm2=Frame(frm,pady=20,bg='LEMONCHIFFON')
    frm2.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm3=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm3.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm4=Frame(frm,bg='LEMONCHIFFON',pady=20)
    frm4.pack(side=TOP,expand=tkinter.YES, fill=tkinter.BOTH)
    frm21=Frame(frm2,bg='LEMONCHIFFON')
    frm21.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm22=Frame(frm2,bg='LEMONCHIFFON')
    frm22.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm23=Frame(frm2,bg='LEMONCHIFFON')
    frm23.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm24=Frame(frm2,bg='LEMONCHIFFON')
    frm24.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm25=Frame(frm2,bg='LEMONCHIFFON')
    frm25.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    frm26=Frame(frm2,bg='LEMONCHIFFON')
    frm26.pack(side=LEFT,expand=tkinter.YES, fill=tkinter.BOTH)
    #...

    def verify():
        user=f.get()
        passw=u.get()
        if(user=='abc' and passw=='123'):
            messagebox.showinfo("LOGIN","Logged in successfully")
            optionsignup()
        else:
            u.delete(0,END)
            f.delete(0,END)
            messagebox.showinfo("OOPS!!!","Entered data mismatched!!")
        

    label=Label(frm1,text='LOGIN..',fg='BLACK',bg='LEMONCHIFFON',font = "Times 40 bold")
    label.pack(side=TOP)
    label1=Label(frm23,text='Username',fg='BLACK',bg='LEMONCHIFFON',font="20")
    label1.pack(side=TOP)
    f=Entry(frm24,font="25")
    f.pack(side=TOP)
    labelaa=Label(frm23,text='',fg='BLACK',bg='LEMONCHIFFON')
    labelaa.pack(side=TOP)
    labelaaa=Label(frm24,text='',fg='BLACK',bg='LEMONCHIFFON')
    labelaaa.pack(side=TOP)
    label1=Label(frm23,text='Password',fg='BLACK',bg='LEMONCHIFFON',font="20")
    label1.pack(side=TOP)
    u=Entry(frm24,font="25",show='$')
    u.pack(side=TOP)
    submit=Button(frm3,fg='BLACK',text='Login',font="Times 12 bold",padx=32,pady=5,command=verify,cursor='hand2')
    submit.pack(side=TOP)
   
login()
    
if __name__=="__main__":
    main()
logs.mainloop()


##################################################
