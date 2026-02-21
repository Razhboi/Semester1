import customtkinter as ctk
from PIL import ImageTk,Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

def show_page_two():
    page_one_frame.place_forget()
    my_label.place_forget()
    labeljudul.pack_forget()
    labelnama1.place_forget()
    labelnama2.place_forget()
    labelnama3.place_forget()
    labelnama4.place_forget()
    labelnama5.place_forget()
    
    #2nd page
    label_two.place(x=0, y=0, relwidth=1, relheight=1)
    #entry
    entry.grid(row=0, column=0, columnspan=5,pady=50)
    #filler
    fillabel1.grid(row=4, column=0)
    fillabel2.grid(row=4, column=4)
    #infobox
    infobox.grid(row=1, column=0, columnspan=5)
    #first row button
    button0.grid(row=2, column=1,pady=5)
    button1.grid(row=2, column=2,pady=5)
    buttonclear.grid(row=2, column=3, pady=5)
    #second row button
    buttonand.grid(row=3, column=1,pady=5)
    buttonor.grid(row=3, column=2,pady=5)
    buttonnot.grid(row=3, column=3,pady=5)
    #third row button
    buttonnand.grid(row=4, column=1, pady=5)
    buttonnor.grid(row=4, column=2, pady=5)
    buttonxor.grid(row=4, column=3, pady=5)
    #fourth row button
    buttonxnor.grid(row=5, column=1, pady=5)
    buttoncal.grid(row=5, column=3, pady=5)

locksym = 'unlock'
lockop = 'lock'
operator = ''
evaluable = ''
checkop = ''
notpresent = ''
lvar = []

def press(symbol):
    global locksym
    global lockop
    global lvar
    global operator
    global evaluable
    global checkop
    
    entry.configure(state='normal')
    if locksym == 'lock':
        infobox.configure(text='*Harap masukkan operator')
    if locksym == 'unlock':

        envar = entry.get() + str(symbol) + ' '
        lvar.append(symbol)
        entry.delete(0, 'end')
        entry.insert(0, envar)
        if operator == 'AND':
            lvar.append((lvar[-2]) and (lvar[-1]))
        if operator == 'OR':
            lvar.append((lvar[-2]) or (lvar[-1]))
        if operator == 'NAND':
            lvar.append(int(not(lvar[-2] and lvar[-1])))
        if operator == 'NOR':
            lvar.append(int(not(lvar[-2] or lvar[-1])))
        if operator == 'XOR':
            lvar.append(lvar[-2] ^ lvar[-1])
        if operator == 'XNOR':
            lvar.append(int(not(lvar[-2] ^ lvar[-1])))
        locksym = 'lock'
        lockop = 'unlock'
        if checkop == 'conf':
            evaluable = 'conf'
        infobox.configure(text='')
    entry.configure(state='disabled')

def clear():
    global locksym
    global lockop
    global lvar
    global operator
    global evaluable
    global checkop
    
    entry.configure(state='normal')
    entry.delete(0, 'end')
    lvar = []
    operator = ''
    lockop = 'lock'
    locksym ='unlock'
    checkop = ''
    evaluable = ''
    infobox.configure(text='')
    entry.configure(state='disabled')

def operate(op):
    global locksym
    global lockop
    global lvar
    global operator
    global evaluable
    global checkop    

    entry.configure(state='normal')
    
    if lockop == 'lock':
        infobox.configure(text='*Harap masukkan nilai')
    if lockop == 'unlock':
        operator = op
        envar = entry.get() + str(op) + ' '
        entry.delete(0, 'end')
        entry.insert(0, envar)
        lockop = 'lock'
        locksym ='unlock'
        checkop = 'conf'
        infobox.configure(text='')
    entry.configure(state='disabled')
    
def notop(op):
    global locksym
    global lockop
    global lvar
    global operator
    global evaluable
    global checkop
    
    entry.configure(state='normal')
    
    if lockop == 'lock':
        infobox.configure(text='*Harap masukkan nilai')
    if lockop == 'unlock':
        operator = op
        lvar[-1] = int(not lvar[-1])
        envar = '(NOT[' + entry.get() +']) '
        entry.delete(0, 'end')
        entry.insert(0, envar)
        checkop = 'confsp'
        infobox.configure(text='')
    entry.configure(state='disabled')
        
def eval():
    global lvar
    global evaluable
    global checkop
    entry.configure(state='normal')
    if checkop == 'confsp' or evaluable == 'conf':
        if (len(lvar) % 2) == 1 :
            enlvar = ' ' + str(lvar[-1]) + ' '
            entry.delete(0, 'end')
            entry.insert(0, enlvar)
            checkop = ''
            evaluable = ''
            infobox.configure(text='')
    else :
        infobox.configure(text='*Operasi tidak valid')
    entry.configure(state='disabled')
    

root = ctk.CTk()
root.geometry("700x500")
root.maxsize(700,500)
root.minsize(700,500)

root.title('Kalkulator Gerbang Logika')

#Main BG
bg = ctk.CTkImage(Image.open(r"C:\Users\Raymond\Desktop\Proyek Logmat\TIF BG.png"),size=(700,500))
my_label= ctk.CTkLabel(root, text='', image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#Main Text
labeljudul = ctk.CTkLabel(root,text="KALKULATOR GERBANG LOGIKA", font=('Exotc350 Bd BT', 24,'bold'), text_color='#30318a', fg_color='#ffffff')
labelnama1 = ctk.CTkLabel(root,text="  |   Adetia Raymond S.\t(2320506036)", font=('roboto', 17,'bold'), text_color='#30318a', fg_color='#ffffff')
labelnama2 = ctk.CTkLabel(root,text="  |   Muhammad Naveed S.\t(2320506040)", font=('roboto', 17,'bold'), text_color='#30318a', fg_color='#ffffff')
labelnama3 = ctk.CTkLabel(root,text="  |   Wahyu Dwi Yulianto.\t(2340506056)", font=('roboto', 17,'bold'), text_color='#30318a', fg_color='#ffffff')
labelnama4 = ctk.CTkLabel(root,text="  |   Noufal Aji Prasetyo.\t(2340506056)", font=('roboto', 17,'bold'), text_color='#30318a', fg_color='#ffffff')
labelnama5 = ctk.CTkLabel(root,text="  |   Achmad Madania H. M.\t(2340506062)", font=('roboto', 17,'bold'), text_color='#30318a', fg_color='#ffffff')

labeljudul.place(relx=0.445, rely=0.16)
labelnama1.place(relx=0.45, rely=0.25)
labelnama2.place(relx=0.45, rely=0.295)
labelnama3.place(relx=0.45, rely=0.34)
labelnama4.place(relx=0.45, rely=0.385)
labelnama5.place(relx=0.45, rely=0.43)

#Start Button
page_one_frame = ctk.CTkFrame(root, fg_color='#FFFFFF')
button_one = ctk.CTkButton(page_one_frame, text="START", font=('Swis721 Hv BT', 24),text_color='#FFFFFF',fg_color='#30318a',width=250,height=65,corner_radius=50
                           ,command=show_page_two)

page_one_frame.place(relx=0.308, rely=0.72)
button_one.pack(pady=10, padx=10)

#PAGE 2nd

bg2 = ctk.CTkImage(Image.open(r"C:\Users\Raymond\Desktop\Proyek Logmat\TIF BG2.png"),size=(700,500))

#Main layout
label_two = ctk.CTkLabel(root, text='', image=bg2)

#Entry box
entry = ctk.CTkEntry(root, width=700, height=70,font=('roboto', 23, 'bold'),text_color='#30318a', state='disabled')

#Filler
fillabel1 = ctk.CTkLabel(root,text='',fg_color='#ffffff',padx=75)
fillabel2 = ctk.CTkLabel(root,text='',fg_color='#ffffff',padx=75)

#Info box
infobox = ctk.CTkLabel(root,text='',font=('roboto', 20, 'bold'),text_color='#FF0000',fg_color='#ffffff')
#First row 
button0 = ctk.CTkButton(root, text='0',font=('Swis721 BlkCn BT', 29, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                        ,command=lambda: press(0))
button1 = ctk.CTkButton(root, text='1',font=('Swis721 BlkCn BT', 29, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                        ,command=lambda: press(1))
buttonclear = ctk.CTkButton(root, text='Clear',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                            ,command= clear)

#Second row
buttonand = ctk.CTkButton(root, text='AND',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                          ,command= lambda: operate('AND'))
buttonor = ctk.CTkButton(root, text='OR',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                         ,command= lambda: operate('OR'))
buttonnot = ctk.CTkButton(root, text='NOT',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                          ,command= lambda: notop('NOT'))


#Third row
buttonnand = ctk.CTkButton(root, text='NAND',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                           ,command= lambda: operate('NAND'))
buttonnor = ctk.CTkButton(root, text='NOR',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                          ,command= lambda: operate('NOR'))
buttonxor = ctk.CTkButton(root, text='XOR',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                          ,command= lambda: operate('XOR'))


#Fourth row
buttonxnor = ctk.CTkButton(root, text='XNOR',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                           ,command= lambda: operate('XNOR'))
buttoncal = ctk.CTkButton(root, text='=>',font=('roboto', 27, 'bold'),text_color='#ffffff' ,width=140, height=50,fg_color='#30318a'
                          ,command=eval)



root.mainloop()
