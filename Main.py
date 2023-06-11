from tkinter import *
import smtplib

#main Screen
master = Tk()
master.title("Email Application")

#functions
def send_email():
    username = temp_username.get()
    password = temp_password.get()
    receiver = temp_receiver.get()
    subject = temp_subject.get()
    body = temp_body.get()

    if username or password or receiver or subject or body == "":
        notif.config("All fields are required",fg="red")
        return
    else:
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username,password)
            message = 'Subject: {}\n\n{}'.format(subject,body)
            server.sendmail(username,receiver,message)
            server.quit()
            notif.config(fg="green",text="Email has been sent successfully")
        except:
            notif.config(fg="red",text="Error sending email")

def reset_email():
    username = temp_username.get()
    password = temp_password.get()
    receiver = temp_receiver.get()
    subject = temp_subject.get()
    body = temp_body.get()

    temp_username.set("")
    temp_password.set("")
    temp_receiver.set("")
    temp_subject.set("")
    temp_body.set("")


#Graphics window
Label(master, text="Custom Email Application", font=('poppins', 15)).grid(row=0,columnspan=2, sticky=N)
Label(master, text="Use The Form Below To Send A Mail",font=('poppins',11)).grid(row=1,columnspan=2, sticky=W,padx=5)


Label(master, text="Email :",font=('poppins',11)).grid(row=2,column=0, sticky=W,padx=25)
Label(master, text="Password :",font=('poppins',11)).grid(row=3,column=0, sticky=W,padx=25)
Label(master, text="To :",font=('poppins',11)).grid(row=4,column=0, sticky=W,padx=25)
Label(master, text="Subject :",font=('poppins',11)).grid(row=5,column=0, sticky=W,padx=25)
Label(master, text="Body :",font=('poppins',11)).grid(row=6,column=0, sticky=W,padx=25)

notif = Label(master, text="",font=('poppins',11))
notif.grid(row=7, sticky=S,padx=5)

#storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#Entries
Entry(master, textvariable=temp_username).grid(row=2, column=1,padx=25)
Entry(master, textvariable=temp_password,show="#").grid(row=3, column=1,padx=25)
Entry(master, textvariable=temp_receiver).grid(row=4, column=1,padx=25)
Entry(master, textvariable=temp_subject).grid(row=5, column=1,padx=25)
Entry(master, textvariable=temp_body).grid(row=6, column=1,padx=25)

#Buttons

Button(master, text="Send", command=send_email).grid(row=7, sticky=W,padx=5,pady=15)
Button(master, text="Reset", command=reset_email).grid(row=7, sticky=W,padx=45,pady=45)

master.mainloop()