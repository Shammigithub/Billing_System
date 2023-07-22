from tkinter import *


#GUI part
root = Tk()
root.title("Billing System")
root.geometry("1190x758")
root.iconbitmap("icon.ico")

headingLabel = Label(root, text="Billing System",font=('times new roman',30, 'bold'), bg='pink3',fg='maroon4',bd=12,relief=GROOVE )
headingLabel.pack(fill=X,pady=10)




root.mainloop()