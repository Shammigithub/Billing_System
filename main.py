from tkinter import *


#GUI part
root = Tk()
root.title("Billing System")
root.geometry("1190x758")
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
billFrame.grid(row=0,column=3,padx=55)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X,padx=40)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=18,width=40,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


root.mainloop()