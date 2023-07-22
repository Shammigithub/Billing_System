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




root.mainloop()