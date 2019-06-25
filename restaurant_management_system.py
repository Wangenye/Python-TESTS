#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")

root.configure(background='cadet blue')
# adding a frame
Tops = Frame(root, bg='cadet blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)
# HEADING
lblTitle = Label(Tops, font=('arial', 60, 'bold'), text='Restaurant Management System', bd=21, bg='cadet blue',
                 fg='cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

# receipt and calculator frame
ReceiptCal_F = Frame(root, bg='powder blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg='powder blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F = Frame(ReceiptCal_F, bg='powder blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F = Frame(ReceiptCal_F, bg='powder blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

Menuframe = Frame(root, bg='cadet blue', bd=10, relief=RIDGE)
Menuframe.pack(side=LEFT)
# drinks and cake frames
Drinks_F = Frame(Menuframe, bg='cadet blue', bd=10)
Drinks_F.pack(side=TOP)
Cost_F = Frame(Menuframe, bg='powder blue', bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F = Frame(Menuframe, bg='powder blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cakes_F = Frame(Menuframe, bg='powder blue', bd=10, relief=RIDGE)
Cakes_F.pack(side=RIGHT)

# checkboxes

# =======================variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateOfOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_input = StringVar()
operator = ""

E_Latta = StringVar()
E_Expresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_Coffee = StringVar()
E_Cappucino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappucino = StringVar()

E_School_Cake = StringVar()
E_Sunday_O_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_West_African_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Carlton_Hill_Chocolate_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()

E_Latta.set("0")
E_Expresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappucino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappucino.set("0")

E_School_Cake.set("0")
E_Sunday_O_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FUNCTION DECLARATIONS>>>>>>>>>>>>>>>>>>>>>>>>>
# EXIT BUTTON
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Restaurant System", "CONFIRM IF YOU WANT TO EXIT")
    if iExit <= 0:
        root.destroy()
        return


# RESET BUTTON
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Latta.set("0")
    E_Expresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_Coffee.set("0")
    E_Cappucino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappucino.set("0")

    E_School_Cake.set("0")
    E_Sunday_O_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Jonathan_YO_Cake.set("0")
    E_West_African_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatta.configure(state=DISABLED)
    txtExpresso.configure(state=DISABLED)
    txtIced_Latta.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappucino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappucino.configure(state=DISABLED)
    txtSchoolCake.configure(state=DISABLED)
    txtSunday_O_Cake.configure(state=DISABLED)
    txtJonathan_YO_Cake.configure(state=DISABLED)
    txtWest_African_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate_Cake.configure(state=DISABLED)
    txtCarlton_Hill_Cake.configure(state=DISABLED)
    txtQueen_Park_Cake.configure(state=DISABLED)
    
#========================
def CostOfItem():
    Item1 = float(E_Latta.get())
    Item2 = float(E_Expresso.get())
    Item3 = float(E_Iced_Latta.get())
    Item4 = float(E_Vale_Coffee.get())
    Item5 = float(E_Cappucino.get())
    Item6 = float(E_African_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappucino.get())
    
    Item9 = float(E_School_Cake.get())
    Item10 = float(E_Sunday_O_Cake.get())
    Item11 = float(E_Jonathan_YO_Cake.get())
    Item12 = float(E_West_African_Cake.get())
    Item13 = float(E_Lagos_Chocolate_Cake.get())
    Item14 = float(E_Kilburn_Chocolate_Cake.get())
    Item15 = float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16 = float(E_Queen_Park_Chocolate_Cake.get())
    
    PriceOfDrinks = (Item1*1.2)+(Item2*1.99)+ (Item3*2.05)+(Item4*1.89)+(Item5*1.99)                                    +(Item6*2.99)+(Item7*2.39)+(Item8*1.29)
        
    PriceOfCakes = (Item9*1.35)+(Item10*2.2)+ (Item11*1.99)+(Item12*1.49)+(Item13*1.8)                                    +(Item14*1.67)+(Item15*1.6)+(Item16*1.99)
        
    DrinksPrice = "Ksh.",str("%.2sf"%(PriceOfDrinks))
    CakessPrice = "Ksh.",str("%.2sf"%(PriceOfCakes))
    CostofCakes.set(CakessPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "ksh.",str("%.2sf"%(1.59))
    ServiceCharge.set(SC)
        
    SubTotalITEMS = "Ksh.", str('%.2f'%(PriceOfDrinks + PriceOfCakes + 1.59))
    SubTotal.set(SubTotalITEMS)
    
    Tax = "Ksh.", str('%.2f'%((PriceOfDrinks + PriceOfCakes + 1.59)*0.15))
    PaidTax.set(Tax)
    
    TT = ((PriceOfDrinks + PriceOfCakes + 1.59)*0.15)
    
    TC = "Ksh.", str('%.2f'%(PriceOfDrinks + PriceOfCakes + 1.59+TT))
    TotalCost.set(TC)
    
    
def chkLatta():
    if (var1.get() == 1):
        txtLatta.configure(state = NORMAL)
        txtLatta.focus()
        txtLatta.delete('0',END)
        E_Latta.set("")  
    elif(var1.get() == 0):
        txtLatta.configure(state = DISABLED)
        E_Latta.set("0")
        
def chkExpresso():
    if (var2.get() == 1):
        txtExpresso.configure(state = NORMAL)
        txtExpresso.focus()
        txtExpresso.delete('0',END)
        E_Expresso.set("")  
    elif(var2.get() == 0):
        txtExpresso.configure(state = DISABLED)
        E_Expresso.set("0")
        
def chkIcedLatta():
    if (var3.get() == 1):
        txtIced_Latta.configure(state = NORMAL)
        txtIced_Latta.focus()
        txtIced_Latta.delete('0',END)
        E_Iced_Latta.set("")  
    elif(var3.get() == 0):
        txtIced_Latta.configure(state = DISABLED)
        E_Iced_Latta.set("0")
        
def chkVale_Coffee():
    if (var4.get() == 1):
        txtVale_Coffee.configure(state = NORMAL)
        txtVale_Coffee.focus()
        txtVale_Coffee.delete('0',END)
        E_Vale_Coffee.set("")  
    elif(var4.get() == 0):
        txtVale_Coffee.configure(state = DISABLED)
        E_Vale_Coffee.set("0")
        
def chkCappucino():
    if (var5.get() == 1):
        txtCappucino.configure(state = NORMAL)
        txtCappucino.focus()
        txtCappucino.delete('0',END)
        E_Cappucino.set("")  
    elif(var5.get() == 0):
        txtCappucino.configure(state = DISABLED)
        E_Cappucino.set("0")
        
def chkAfrican_Coffee():
    if (var6.get() == 1):
        txtAfrican_Coffee.configure(state = NORMAL)
        txtAfrican_Coffee.focus()
        txtAfrican_Coffee.delete('0',END)
        E_African_Coffee.set("")  
    elif(var6.get() == 0):
        txtAfrican_Coffee.configure(state = DISABLED)
        E_African_Coffee.set("0")
        
def chkAmerican_Coffee():
    if (var7.get() == 1):
        txtAmerican_Coffee.configure(state = NORMAL)
        txtAmerican_Coffee.focus()
        txtAmerican_Coffee.delete('0',END)
        E_American_Coffee.set("")  
    elif(var7.get() == 0):
        txtAmerican_Coffee.configure(state = DISABLED)
        E_American_Coffee.set("0")
        
def chkIced_Cappucino():
    if (var8.get() == 1):
        txtIced_Cappucino.configure(state = NORMAL)
        txtIced_Cappucino.focus()
        txtIced_Cappucino.delete('0',END)
        E_Iced_Cappucino.set("")  
    elif(var8.get() == 0):
        txtIced_Cappucino.configure(state = DISABLED)
        E_Iced_Cappucino.set("0")
            
    
    


# ==============================================DRINKS===================================================
Latta = Checkbutton(Drinks_F, text='Latta', variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg='powder blue',command = chkLatta).grid(row=0, sticky='w')
Expresso = Checkbutton(Drinks_F, text='Expresso', variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                       bg='powder blue',command = chkExpresso).grid(row=1, sticky='w')
Iced_Latta = Checkbutton(Drinks_F, text='Iced Latta', variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                         bg='powder blue',command = chkIcedLatta).grid(row=2, sticky='w')
Vale_Coffee = Checkbutton(Drinks_F, text='Vale Coffee', variable=var4, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'),
                          bg='powder blue',command = chkVale_Coffee).grid(row=3, sticky='w')
Cappucino = Checkbutton(Drinks_F, text='Cappucino', variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                        bg='powder blue',command = chkCappucino).grid(row=4, sticky='w')
African_Coffee = Checkbutton(Drinks_F, text='African Coffee', variable=var6, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'),
                             bg='powder blue',command = chkAfrican_Coffee).grid(row=5, sticky='w')
American_Coffee = Checkbutton(Drinks_F, text='American Coffee', variable=var7, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'),
                              bg='powder blue',command = chkAmerican_Coffee).grid(row=6, sticky='w')
Iced_Cappucino = Checkbutton(Drinks_F, text='Iced Cappucino', variable=var8, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'),
                             bg='powder blue',command = chkIced_Cappucino).grid(row=7, sticky='w')
# ==============================================ENTRY BOX FOR DRINKS===================================================
txtLatta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, textvariable=E_Latta, state=DISABLED )
txtLatta.grid(row=0, column=1)

txtExpresso = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Expresso, state=DISABLED)
txtExpresso.grid(row=1, column=1)

txtIced_Latta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Iced_Latta, state=DISABLED)
txtIced_Latta.grid(row=2, column=1)

txtVale_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Vale_Coffee, state=DISABLED)
txtVale_Coffee.grid(row=3, column=1)

txtCappucino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Cappucino, state=DISABLED)
txtCappucino.grid(row=4, column=1)

txtAfrican_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_African_Coffee, state=DISABLED)
txtAfrican_Coffee.grid(row=5, column=1)

txtAmerican_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_American_Coffee, state=DISABLED)
txtAmerican_Coffee.grid(row=6, column=1)

txtIced_Cappucino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Iced_Cappucino, state=DISABLED)
txtIced_Cappucino.grid(row=7, column=1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def chkSchoolCake():
    if (var9.get() == 1):
        txtSchoolCake.configure(state = NORMAL)
        txtSchoolCake.focus()
        txtSchoolCake.delete('0',END)
        E_School_Cake.set("")  
    elif(var9.get() == 0):
        txtSchoolCake.configure(state = DISABLED)
        E_School_Cake.set("0")
        
def chkSunday_O_Cake():
    if (var10.get() == 1):
        txtSunday_O_Cake.configure(state = NORMAL)
        txtSunday_O_Cake.focus()
        txtSunday_O_Cake.delete('0',END)
        E_Sunday_O_Cake.set("")  
    elif(var10.get() == 0):
        txtSunday_O_Cake.configure(state = DISABLED)
        E_Sunday_O_Cake.set("0")
        
def chkJonathan_YO_Cake():
    if (var11.get() == 1):
        txtJonathan_YO_Cake.configure(state = NORMAL)
        txtJonathan_YO_Cake.focus()
        txtJonathan_YO_Cake.delete('0',END)
        E_Jonathan_YO_Cake.set("")  
    elif(var11.get() == 0):
        txtJonathan_YO_Cake.configure(state = DISABLED)
        E_Jonathan_YO_Cake.set("0")
        
def chkWest_African_Cake():
    if (var12.get() == 1):
        txtWest_African_Cake.configure(state = NORMAL)
        txtWest_African_Cake.focus()
        txtWest_African_Cake.delete('0',END)
        E_West_African_Cake.set("")  
    elif(var12.get() == 0):
        txtWest_African_Cake.configure(state = DISABLED)
        E_West_African_Cake.set("0")
        

        
def chkLagos_Chocolate_Cake():
    if (var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state = NORMAL)
        txtLagos_Chocolate_Cake.focus()
        txtLagos_Chocolate_Cake.delete('0',END)
        E_Lagos_Chocolate_Cake.set("")  
    elif(var13.get() == 0):
        txtLagos_Chocolate_Cake.configure(state = DISABLED)
        E_Lagos_Chocolate_Cake.set("0")
        
def chkKilburn_Chocolate_Cake():
    if (var14.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state = NORMAL)
        txtKilburn_Chocolate_Cake.focus()
        txtKilburn_Chocolate_Cake.delete('0',END)
        E_Kilburn_Chocolate_Cake.set("")  
    elif(var14.get() == 0):
        txtKilburn_Chocolate_Cake.configure(state = DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")
        
def chkCarlton_Hill_Cake():
    if (var15.get() == 1):
        txtCarlton_Hill_Cake.configure(state = NORMAL)
        txtCarlton_Hill_Cake.focus()
        txtCarlton_Hill_Cake.delete('0',END)
        E_Carlton_Hill_Chocolate_Cake.set("")  
    elif(var15.get() == 0):
        txtCarlton_Hill_Cake.configure(state = DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")
        
def chkQueen_Park_Cake():
    if (var16.get() == 1):
        txtQueen_Park_Cake.configure(state = NORMAL)
        txtQueen_Park_Cake.focus()
        txtQueen_Park_Cake.delete('0',END)
        E_Queen_Park_Chocolate_Cake.set("")  
    elif(var16.get() == 0):
        txtQueen_Park_Cake.configure(state = DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")
        
        
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)
    
    txtReceipt.insert(END, "Recipt REF :\t\t\t" + Receipt_Ref.get()+"\t"+ DateOfOrder.get()+"\n")
    txtReceipt.insert(END, "Items :\t\t\t" + "Cost of Item \n")
    txtReceipt.insert(END, "Latta :\t\t\t\t\t" + E_Latta.get()+"\n")
    txtReceipt.insert(END, "Expresso :\t\t\t\t\t" + E_Expresso.get()+"\n")
    txtReceipt.insert(END, "Iced Latta :\t\t\t\t\t" + E_Iced_Latta.get()+"\n")
    txtReceipt.insert(END, "Vale Coffee :\t\t\t\t\t" + E_Vale_Coffee.get()+"\n")
    txtReceipt.insert(END, "Cappucino :\t\t\t\t\t" + E_Cappucino.get()+"\n")
    txtReceipt.insert(END, "African Coffee :\t\t\t\t\t" + E_African_Coffee.get()+"\n")
    txtReceipt.insert(END, "American Coffee :\t\t\t\t\t" + E_American_Coffee.get()+"\n")
    txtReceipt.insert(END, "Iced Cappucino :\t\t\t\t\t" + E_Iced_Cappucino.get()+"\n")
    txtReceipt.insert(END, "School Cake :\t\t\t\t\t" + E_School_Cake.get()+"\n")
    txtReceipt.insert(END, "Sunday O Cake:\t\t\t\t\t" + E_Sunday_O_Cake.get()+"\n")
    txtReceipt.insert(END, "Jonathan YO Cake :\t\t\t\t\t" + E_Jonathan_YO_Cake.get()+"\n")
    txtReceipt.insert(END, "West African Cake :\t\t\t\t\t" + E_West_African_Cake.get()+"\n")
    txtReceipt.insert(END, "Lagos Chocolate Cake :\t\t\t\t\t" + E_Lagos_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END, "Kilburn Chocolate Cake :\t\t\t\t\t" + E_Kilburn_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END, "Carlton Hill Cake :\t\t\t\t\t" + E_Carlton_Hill_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END, "Queen Park Cake :\t\t\t\t\t" + E_Queen_Park_Chocolate_Cake.get()+"\n")

# ==============================================CAKES===================================================

SchoolCake = Checkbutton(Cakes_F, text='School Cake\t\t\t', variable=var9, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'),
                         bg='powder blue',command = chkSchoolCake).grid(row=0, sticky='w')

Sunday_O_Cake = Checkbutton(Cakes_F, text='Sunday O Cake', variable=var10, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold'),
                            bg='powder blue',command = chkSunday_O_Cake).grid(row=1, sticky='w')

Jonathan_YO_Cake = Checkbutton(Cakes_F, text='Jonathan YO Cake', variable=var11, onvalue=1, offvalue=0,
                               font=('arial', 18, 'bold'),
                               bg='black', fg='white',command = chkJonathan_YO_Cake).grid(row=2, sticky='w')

West_African_Cake = Checkbutton(Cakes_F, text='West African Cake', variable=var12, onvalue=1, offvalue=0,
                                font=('arial', 18, 'bold'),
                                bg='powder blue',command = chkWest_African_Cake).grid(row=3, sticky='w')

Lagos_Chocolate_Cake = Checkbutton(Cakes_F, text='Lagos Chocolate Cake', variable =var13, onvalue=1, offvalue=0,
                                   font=('arial', 18, 'bold'),
                                   bg='powder blue',command = chkLagos_Chocolate_Cake).grid(row=4, sticky='w')

Kilburn_Chocolate_Cake = Checkbutton(Cakes_F, text='Kilburn Chocolate Cake', variable=var14, onvalue=1, offvalue=0,
                                     font=('arial', 18, 'bold'),
                                     bg='powder blue',command = chkKilburn_Chocolate_Cake).grid(row=5, sticky='w')

Carlton_Hill_Cake = Checkbutton(Cakes_F, text='Carlton Hill Cake', variable=var15, onvalue=1, offvalue=0,
                                font=('arial', 18, 'bold'),
                                bg='powder blue',command = chkCarlton_Hill_Cake).grid(row=6, sticky='w')

Queen_Park_Cake = Checkbutton(Cakes_F, text='Queen Park Cake', variable=var16, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'),
                              bg='powder blue',command = chkQueen_Park_Cake).grid(row=7, sticky='w')
# ==============================================ENTRY BOX FOR CAKES===================================================
txtSchoolCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_School_Cake, state=DISABLED)
txtSchoolCake.grid(row=0, column=1)

txtSunday_O_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Sunday_O_Cake, state=DISABLED)
txtSunday_O_Cake.grid(row=1, column=1)

txtJonathan_YO_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Jonathan_YO_Cake, state=DISABLED)
txtJonathan_YO_Cake.grid(row=2, column=1)

txtWest_African_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_West_African_Cake, state=DISABLED)
txtWest_African_Cake.grid(row=3, column=1)

txtLagos_Chocolate_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Lagos_Chocolate_Cake, state=DISABLED)
txtLagos_Chocolate_Cake.grid(row=4, column=1)

txtKilburn_Chocolate_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,textvariable=E_Kilburn_Chocolate_Cake,
                                  state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row=5, column=1)

txtCarlton_Hill_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,
                             textvariable=E_Carlton_Hill_Chocolate_Cake, state=DISABLED)
txtCarlton_Hill_Cake.grid(row=6, column=1)

txtQueen_Park_Cake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT,
                           textvariable=E_Queen_Park_Chocolate_Cake, state=DISABLED)
txtQueen_Park_Cake.grid(row=7, column=1)

# =================================================================TOTAL COST=================================
# ==============DRINKS=============
lblCostOfDrinks = Label(Cost_F, font=('arial', 14, 'bold'), text='Cost of Drinks\t', bd=7, bg='powder blue',
                        fg='black')
lblCostOfDrinks.grid(row=0, column=0, sticky='w')
txtCostOfDrinks = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                        textvariable=CostofDrinks , insertwidth=2, justify=RIGHT)
txtCostOfDrinks.grid(row=0, column=1)

# ==============CAKES=============
lblCostOfCakes = Label(Cost_F, font=('arial', 14, 'bold'), text='Cost of Cakes', bd=7, bg='powder blue',
                       fg='black')
lblCostOfCakes.grid(row=1, column=0, sticky='w')
txtCostOfCakes = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                       textvariable=CostofCakes , insertwidth=2, justify=RIGHT)
txtCostOfCakes.grid(row=1, column=1)
# ==============SERVICE CHARGE=============
lblServiceCharge = Label(Cost_F, font=('arial', 14, 'bold'), text='Service Charge', bd=7, bg='powder blue',
                         fg='black')
lblServiceCharge.grid(row=2, column=0, sticky='w')
txtServiceCharge = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                         textvariable=ServiceCharge , insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

# ===========================================PAYMENT INFORMATION==============================================
lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text='\tPaid Tax\t', bd=7, bg='powder blue',
                    fg='black')
lblPaidTax.grid(row=0, column=2, sticky='w')
txtPaidTax = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                   textvariable=PaidTax, insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text='\tSub Total', bd=7, bg='powder blue',
                    fg='black')
lblSubTotal.grid(row=1, column=2, sticky='w')
txtSubTotal = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                    textvariable=SubTotal, insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font=('arial', 14, 'bold'), text='\tSub Total', bd=7, bg='powder blue',
                     fg='black')
lblTotalCost.grid(row=2, column=2, sticky='w')
txtTotalCost = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                     textvariable=TotalCost, insertwidth=2, justify=RIGHT)
txtTotalCost.grid(row=2, column=3)

# =================================================================CREATING RECEIPTS===========================
txtReceipt = Text(Receipt_F, width=46, height=12, bg='white', bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

# =================================================================CREATING RECEIPTS BUTTONS===========================
btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Total',
                  bg='powder blue',command = CostOfItem).grid(row=0, column=0)

btnTReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Receipt',
                     bg='powder blue',command = Receipt).grid(row=0, column=1)

btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Reset',
                  bg='powder blue', command=Reset).grid(row=0, column=2)

btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Exit',
                 bg='powder blue', command=iExit).grid(row=0, column=3)


# ==================================================CALCULATOR DISPLAY===============================================

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CALCULATOR FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


txtDisplay = Entry(Cal_F, width=45, bg='white', bd=4, font=('arial', 12, 'bold'), justify=RIGHT,
                   textvariable=text_input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, '0')

# =================================================================CREATING CALCULATOR BUTTONS===========================
btn7 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='7',
              bg='powder blue', command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='8',
              bg='powder blue', command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='9',
              bg='powder blue', command=lambda: btnClick(9)).grid(row=2, column=2)

btnAdd = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='+',
                bg='powder blue', command=lambda: btnClick('+')).grid(row=2, column=3)

# =================================================================CREATING CALCULATOR BUTTONS===========================
btn4 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='4',
              bg='powder blue', command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='5',
              bg='powder blue', command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='6',
              bg='powder blue', command=lambda: btnClick(6)).grid(row=3, column=2)

btnSub = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='-',
                bg='powder blue', command=lambda: btnClick('-')).grid(row=3, column=3)

# =================================================================CREATING CALCULATOR BUTTONS===========================
btn1 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='1',
              bg='powder blue', command=lambda: btnClick(1)).grid(row=4, column=0)

btn2 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='2',
              bg='powder blue', command=lambda: btnClick(2)).grid(row=4, column=1)

btn3 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='3',
              bg='powder blue', command=lambda: btnClick(3)).grid(row=4, column=2)

btnMulti = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                  width=4, text='x', command=lambda: btnClick('*')).grid(row=4, column=3)

# =================================================================CREATING CALCULATOR BUTTONS===========================
btn0 = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='0',
              bg='powder blue', command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Clear',
                  bg='powder blue', command=btnClear).grid(row=5, column=1)

btnEquals = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='=',
                   bg='powder blue', command=btnEquals).grid(row=5, column=2)

btnDiv = Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='/',
                bg='powder blue', command=lambda: btnClick('/')).grid(row=5, column=3)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




