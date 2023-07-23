from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

if not os.path.exists('bills'):
    os.mkdir('bills')

billnumber=random.randint(500,1000)

def total():
    global pprice,bprice, aprice,oprice,avprice,gprice
    global dprice,tprice,puprice,mprice,muprice,sprice
    global vcprice,ccprice,fcprice,lcprice,icprice,cfcprice
    global totalbill

    pprice=int(papawEntry.get())*150
    bprice=int(bananaEntry.get())*100
    aprice=int(appleEntry.get())*50
    oprice=int(orangeEntry.get())*60
    avprice=int(avacadoEntry.get())*60
    gprice=int(grapesEntry.get())*80

    totalfruitprice=pprice+bprice+aprice+oprice+avprice+gprice
    fruitEntry.delete(0,END)
    fruitEntry.insert(0,'Rs.'+str(totalfruitprice))
    fruittax=totalfruitprice * 0
    fruittaxEntry.delete(0, END)
    fruittaxEntry.insert(0,fruittax)


    dprice = int(dodolEntry.get()) * 200
    tprice = int(thalaEntry.get()) * 160
    puprice = int(phuEntry.get()) * 70
    mprice = int(masEntry.get()) * 80
    muprice = int(musEntry.get()) * 170
    sprice = int(swEntry.get()) * 100

    totalsweetsprice = dprice + tprice + puprice + mprice + muprice + sprice
    sweetsEntry.delete(0, END)
    sweetsEntry.insert(0, 'Rs.' + str(totalsweetsprice))
    sweetstax = totalsweetsprice * 0
    sweetstaxEntry.delete(0, END)
    sweetstaxEntry.insert(0, sweetstax)


    vcprice = int(vcakeEntry.get()) * 250
    ccprice = int(ccakeEntry.get()) * 350
    fcprice = int(fcakeEntry.get()) * 300
    lcprice = int(lcakeEntry.get()) * 600
    icprice = int(icakeEntry.get()) * 1000
    cfcprice = int(cfcakeEntry.get()) * 800

    totalcakeprice = vcprice + ccprice + fcprice +lcprice + icprice + cfcprice
    cakeEntry.delete(0, END)
    cakeEntry.insert(0, 'Rs.' + str(totalcakeprice))
    caketax = totalcakeprice * 0.10
    caketaxEntry.delete(0, END)
    caketaxEntry.insert(0, caketax)

    totalbill=totalfruitprice+totalsweetsprice+totalcakeprice+fruittax+sweetstax+caketax

def bill():

    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif fruitEntry.get()=='' and sweetsEntry.get()=='' and cakeEntry.get()=='':
        messagebox.showerror('Error', ' No Products are selected')
    elif fruitEntry.get()=='Rs.0.0' and sweetsEntry.get()=='Rs.0.0' and cakeEntry.get()=='Rs.0.0':
        messagebox.showerror('Error', ' No Products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**_welcome_**\n ')
        textarea.insert(END,f'\nBilll Number:{billnumber}\n')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer phone Number:{phoneEntry.get()}\n')
        textarea.insert(END, '\n======================================')
        textarea.insert(END, '\nProduct\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n======================================')
        if papawEntry.get()!='0':
            textarea.insert(END,f'\nPapaw\t\t{papawEntry.get()}\t\tRs. {pprice}')
        if bananaEntry.get()!='0':
            textarea.insert(END,f'\nBanana\t\t{bananaEntry.get()}\t\tRs. {bprice}')
        if appleEntry.get()!='0':
            textarea.insert(END,f'\nApple\t\t{appleEntry.get()}\t\tRs. {aprice}')
        if orangeEntry.get()!='0':
            textarea.insert(END,f'\nOrange\t\t{orangeEntry.get()}\t\tRs. {oprice}')
        if avacadoEntry.get()!='0':
            textarea.insert(END,f'\nAvacado\t\t{avacadoEntry.get()}\t\tRs. {avprice}')
        if grapesEntry.get()!='0':
            textarea.insert(END,f'\nGrapes\t\t{grapesEntry.get()}\t\tRs. {gprice}')

        if dodolEntry.get() != '0':
            textarea.insert(END, f'\nDodol\t\t{dodolEntry.get()}\t\tRs. {dprice}')
        if thalaEntry.get() != '0':
            textarea.insert(END, f'\nThalaKerali\t\t{thalaEntry.get()}\t\tRs. {tprice}')
        if phuEntry.get() != '0':
            textarea.insert(END, f'\nPhulDosi\t\t{phuEntry.get()}\t\tRs. {puprice}')
        if masEntry.get() != '0':
            textarea.insert(END, f'\nMarshmallows\t\t{masEntry.get()}\t\tRs. {mprice}')
        if musEntry.get() != '0':
            textarea.insert(END, f'\nMuscat\t\t{musEntry.get()}\t\tRs. {muprice}')
        if swEntry.get() != '0':
            textarea.insert(END, f'\nSweet Cashew\t\t{swEntry.get()}\t\tRs. {sprice}')

        if vcakeEntry.get() != '0':
            textarea.insert(END, f'\nVanilla Cake\t\t{vcakeEntry.get()}\t\tRs. {vcprice}')
        if ccakeEntry.get() != '0':
            textarea.insert(END, f'\nChocolate Cake\t\t{ccakeEntry.get()}\t\tRs. {ccprice}')
        if fcakeEntry.get() != '0':
            textarea.insert(END, f'\nFruit Cake\t\t{fcakeEntry.get()}\t\tRs. {fcprice}')
        if lcakeEntry.get() != '0':
            textarea.insert(END, f'\nLayer Cake\t\t{lcakeEntry.get()}\t\tRs. {lcprice}')
        if icakeEntry.get() != '0':
            textarea.insert(END, f'\nIcing Cake\t\t{icakeEntry.get()}\t\tRs. {icprice}')
        if cfcakeEntry.get() != '0':
            textarea.insert(END, f'\nCoffee Cake\t\t{cfcakeEntry.get()}\t\tRs. {cfcprice}')

        textarea.insert(END, '\n--------------------------------------')

        if fruittaxEntry.get()!='Rs.0.0':
            textarea.insert(END,f'\n Fruit Tax\t\t\t\tRs.{fruittaxEntry.get()}')
        if sweetstaxEntry.get()!='Rs.0.0':
            textarea.insert(END,f'\n Sweet Tax\t\t\t\tRs.{sweetstaxEntry.get()}')
        if caketaxEntry.get()!='Rs.0.0':
            textarea.insert(END,f'\n Cake Tax\t\t\t\tRs.{caketaxEntry.get()}')

        textarea.insert(END,f'\n\nTotal Bill\t\t\t\tRs.{totalbill}\n')
        textarea.insert(END, '\n--------------------------------------')
        textarea.insert(END, '\n ')
        textarea.insert(END, '\tThank You Come Again\n ')
        save_bill()

def save_bill():
    global billnumber

    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'billnumber {billnumber}is saved successfuly')
        billnumber=random.randint(500,1000)

def search():
    for i in os.listdir('bills/'):
        if i.split('.')[0]== billEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Billnumber')

def print():
    if textarea.get(1.0,END)== '\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def email():
    def send():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recipientEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Somthing went wrong, Please try again!',parent=root1)



    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send email')
        root1.resizable(0,0)
        root1.config(bg='gray24')

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray24',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray24',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray24', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        RecipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray24', fg='white')
        RecipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recipientLabel = Label(RecipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray24', fg='white')
        recipientLabel.grid(row=0, column=0, padx=10, pady=8)

        recipientEntry = Entry(RecipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recipientEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(RecipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray24',
                               fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(RecipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()

def clear():
    papawEntry.delete(0, END)
    bananaEntry.delete(0, END)
    appleEntry.delete(0,END)
    orangeEntry.delete(0, END)
    avacadoEntry.delete(0, END)
    grapesEntry.delete(0, END)

    dodolEntry.delete(0, END)
    thalaEntry.delete(0, END)
    phuEntry.delete(0, END)
    masEntry.delete(0, END)
    musEntry.delete(0, END)
    swEntry.delete(0, END)

    vcakeEntry.delete(0, END)
    ccakeEntry.delete(0, END)
    fcakeEntry.delete(0, END)
    lcakeEntry.delete(0, END)
    icakeEntry.delete(0, END)
    cfcakeEntry.delete(0, END)

    papawEntry.insert(0,0)
    bananaEntry.insert(0,0)
    appleEntry.insert(0, 0)
    orangeEntry.insert(0, 0)
    avacadoEntry.insert(0, 0)
    grapesEntry.insert(0, 0)

    dodolEntry.insert(0, 0)
    thalaEntry.insert(0, 0)
    phuEntry.insert(0, 0)
    masEntry.insert(0, 0)
    musEntry.insert(0, 0)
    swEntry.insert(0, 0)

    vcakeEntry.insert(0, 0)
    ccakeEntry.insert(0, 0)
    fcakeEntry.insert(0, 0)
    lcakeEntry.insert(0, 0)
    icakeEntry.insert(0, 0)
    cfcakeEntry.insert(0, 0)

    fruitEntry.delete(0,END)
    sweetsEntry.delete(0,END)
    cakeEntry.delete(0,END)

    fruittaxEntry.delete(0,END)
    sweetstaxEntry.delete(0,END)
    caketaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)

    textarea.delete(1.0,END)


#GUI part
root = Tk()
root.title("Billing System")
root.geometry("1200x758")
root.iconbitmap("icon.ico")

headingLabel = Label(root, text="Billing System",font=('times new roman',30, 'bold'), bg='pink3',fg='maroon4',bd=12,relief=GROOVE )
headingLabel.pack(fill=X,pady=10)

customer_details_frame=LabelFrame(root, text='Customer Details',font=('times new roman',15,'bold'),fg='pink3',bd=8,relief=GROOVE,bg='gray24')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray24',fg='white')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=15)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray24',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,widt=15)
phoneEntry.grid(row=0,column=3,padx=8)

billLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray24',fg='white')
billLabel.grid(row=0,column=4,padx=20,pady=2)
billEntry=Entry(customer_details_frame,font=('arial',15),bd=7,widt=15)
billEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=10,fill=X)

FruitsFrame=LabelFrame(productsFrame,text='Fruits',font=('times new roman',15,'bold'),fg='pink3',bd=8,relief=GROOVE,bg='gray24')
FruitsFrame.grid(row=0,column=0)

papawLabel=Label(FruitsFrame,text='Papaw',font=('times new roman',15,'bold'),bg='gray24',fg='white')
papawLabel.grid(row=0,column=0,pady=9,padx=10)
papawEntry=Entry(FruitsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
papawEntry.grid(row=0,column=1,pady=9,padx=10)
papawEntry.insert(0,0)

bananaLabel=Label(FruitsFrame,text='Banana',font=('times new roman',15,'bold'),bg='gray24',fg='white')
bananaLabel.grid(row=1,column=0,pady=9,padx=10)
bananaEntry=Entry(FruitsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bananaEntry.grid(row=1,column=1,pady=9,padx=10)
bananaEntry.insert(0,0)

appleLabel=Label(FruitsFrame,text='Apple',font=('times new roman',15,'bold'),bg='gray24',fg='white')
appleLabel.grid(row=2,column=0,pady=9,padx=10)
appleEntry=Entry(FruitsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
appleEntry.grid(row=2,column=1,pady=9,padx=10)
appleEntry.insert(0,0)

orangeLabel=Label(FruitsFrame,text='Orange',font=('times new roman',15,'bold'),bg='gray24',fg='white')
orangeLabel.grid(row=3,column=0,pady=9,padx=10)
orangeEntry=Entry(FruitsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
orangeEntry.grid(row=3,column=1,pady=9,padx=10)
orangeEntry.insert(0,0)

avacadoLabel=Label(FruitsFrame,text='Avacado',font=('times new roman',15,'bold'),bg='gray24',fg='white')
avacadoLabel.grid(row=4,column=0,pady=9,padx=10)
avacadoEntry=Entry(FruitsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
avacadoEntry.grid(row=4,column=1,pady=9,padx=10)
avacadoEntry.insert(0,0)

grapesLabel=Label(FruitsFrame,text='Grapes',font=('times new roman',15,'bold'),bg='gray24',fg='white')
grapesLabel.grid(row=5,column=0,pady=9,padx=10)
grapesEntry=Entry(FruitsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grapesEntry.grid(row=5,column=1,pady=9,padx=10)
grapesEntry.insert(0,0)

SweetsFrame=LabelFrame(productsFrame,text="Sweets",font=('times new roman',15,'bold'),fg='pink3',bd=8,relief=GROOVE,bg='gray24')
SweetsFrame.grid(row=0,column=1)

dodolLabel=Label(SweetsFrame,text='Dodol',font=('times new roman',15,'bold'),bg='gray24',fg='white')
dodolLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
dodolEntry=Entry(SweetsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dodolEntry.grid(row=0,column=1,pady=9,padx=10)
dodolEntry.insert(0,0)

thalaLabel=Label(SweetsFrame,text='Thalakerali',font=('times new roman',15,'bold'),bg='gray24',fg='white')
thalaLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
thalaEntry=Entry(SweetsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
thalaEntry.grid(row=1,column=1,pady=9,padx=10)
thalaEntry.insert(0,0)

phuLabel=Label(SweetsFrame,text='Puhul Dosi',font=('times new roman',15,'bold'),bg='gray24',fg='white')
phuLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
phuEntry=Entry(SweetsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
phuEntry.grid(row=2,column=1,pady=9,padx=10)
phuEntry.insert(0,0)

masLabel=Label(SweetsFrame,text='Marshmallows',font=('times new roman',15,'bold'),bg='gray24',fg='white')
masLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
masEntry=Entry(SweetsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
masEntry.grid(row=3,column=1,pady=9,padx=10)
masEntry.insert(0,0)

musLabel=Label(SweetsFrame,text='Muscat',font=('times new roman',15,'bold'),bg='gray24',fg='white')
musLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
musEntry=Entry(SweetsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
musEntry.grid(row=4,column=1,pady=9,padx=10)
musEntry.insert(0,0)

swLabel=Label(SweetsFrame,text='Sweet Cashew',font=('times new roman',15,'bold'),bg='gray24',fg='white')
swLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
swEntry=Entry(SweetsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
swEntry.grid(row=5,column=1,pady=9,padx=10)
swEntry.insert(0,0)

cakeFrame=LabelFrame(productsFrame,text="Cakes",font=('times new roman',15,'bold'),fg='pink3',bd=8,relief=GROOVE,bg='gray24')
cakeFrame.grid(row=0,column=2)

vcakeLabel=Label(cakeFrame,text='Vanilla Cake',font=('times new roman',15,'bold'),bg='gray24',fg='white')
vcakeLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
vcakeEntry=Entry(cakeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
vcakeEntry.grid(row=0,column=1,pady=9,padx=10)
vcakeEntry.insert(0,0)

ccakeLabel=Label(cakeFrame,text='Chocolate Cake',font=('times new roman',15,'bold'),bg='gray24',fg='white')
ccakeLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
ccakeEntry=Entry(cakeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ccakeEntry.grid(row=1,column=1,pady=9,padx=10)
ccakeEntry.insert(0,0)

fcakeLabel=Label(cakeFrame,text='Fruit Cake',font=('times new roman',15,'bold'),bg='gray24',fg='white')
fcakeLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
fcakeEntry=Entry(cakeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fcakeEntry.grid(row=2,column=1,pady=9,padx=10)
fcakeEntry.insert(0,0)

lcakeLabel=Label(cakeFrame,text='Layer Cake ',font=('times new roman',15,'bold'),bg='gray24',fg='white')
lcakeLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
lcakeEntry=Entry(cakeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
lcakeEntry.grid(row=3,column=1,pady=9,padx=10)
lcakeEntry.insert(0,0)

icakeLabel=Label(cakeFrame,text='Icing Cake',font=('times new roman',15,'bold'),bg='gray24',fg='white')
icakeLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
icakeEntry=Entry(cakeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
icakeEntry.grid(row=4,column=1,pady=9,padx=10)
icakeEntry.insert(0,0)

cfcakeLabel=Label(cakeFrame,text='Coffee Cake',font=('times new roman',15,'bold'),bg='gray24',fg='white')
cfcakeLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cfcakeEntry=Entry(cakeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cfcakeEntry.grid(row=5,column=1,pady=9,padx=10)
cfcakeEntry.insert(0,0)

billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X,)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=18,width=40,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='pink3',bd=8,relief=GROOVE,bg='gray24')
billmenuFrame.pack(fill=X)

fruitLabel=Label(billmenuFrame,text='Fruits Total',font=('times new roman',15,'bold'),bg='gray24',fg='white')
fruitLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
fruitEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fruitEntry.grid(row=0,column=1,pady=9,padx=10)

sweetsLabel=Label(billmenuFrame,text='Sweets Total',font=('times new roman',15,'bold'),bg='gray24',fg='white')
sweetsLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
sweetsEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sweetsEntry.grid(row=1,column=1,pady=9,padx=10)

cakeLabel=Label(billmenuFrame,text='Cakes Total',font=('times new roman',15,'bold'),bg='gray24',fg='white')
cakeLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
cakeEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cakeEntry.grid(row=2,column=1,pady=9,padx=10)

fruittaxLabel=Label(billmenuFrame,text='Fruit Tax',font=('times new roman',15,'bold'),bg='gray24',fg='white')
fruittaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')
fruittaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fruittaxEntry.grid(row=0,column=3,pady=9,padx=10)

sweetstaxLabel=Label(billmenuFrame,text='Sweets Tax',font=('times new roman',15,'bold'),bg='gray24',fg='white')
sweetstaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')
sweetstaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sweetstaxEntry.grid(row=1,column=3,pady=9,padx=10)

caketaxLabel=Label(billmenuFrame,text='Cake Tax',font=('times new roman',15,'bold'),bg='gray24',fg='white')
caketaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')
caketaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
caketaxEntry.grid(row=2,column=3,pady=9,padx=10)

buttonFrame =Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=15)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),fg='white',bg='maroon4',bd=5,width=7,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),fg='white',bg='maroon4',bd=5,width=7,pady=10,command=bill)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),fg='white',bg='maroon4',bd=5,width=7,pady=10,command=email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),fg='white',bg='maroon4',bd=5,width=7,pady=10,command=print)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),fg='white',bg='maroon4',bd=5,width=7,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()