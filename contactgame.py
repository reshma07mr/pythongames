#contact book is used to save name, phone number.

#without a database,storing using list
'''name=[]
phone_num=[]
#how many entries are needed to add
x=int(input("Enter the number of contacts needed to save: "))

for i in range(x):
    nam_e=input("Enter the name : ")
    name.append(nam_e)

    pho_num=int(input("Enter the phone number : "))
    phone_num.append(pho_num)
    
#displaying
for i in range(len(name)):
    name[i]=name[i].upper()

for i in range(x):
    print("{}\t\t{}".format(name[i], phone_num[i]))

#for searching by name
search_name=input("Enter the name to be searched :")
search_name=search_name.upper()

if search_name in name:
    x=name.index(search_name)
    y=phone_num[x]
    print("Searched name :{}\nPhone number :{}".format(search_name,y))

else:
    print("User not found")'''

#importing necessary modules

import sqlite3

# Connecting and Initializing the Database where we will store all the data
connector = sqlite3.connect('contacts.db')
#using sqlite3.connect() func a database is created.connected to script by assigning a variable connector.
cursor = connector.cursor()
#for this conncetor varible a function is created known as cursor.
cursor.execute(
"CREATE TABLE IF NOT EXISTS CONTACT_BOOK (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NUMBER TEXT, ADDRESS TEXT)"
)

#using the cursor function a database is created

#Initializing GUI
'''Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively.To create a new StringVar object, you use the StringVar constructor like this:
string_var = tk.StringVar(container, value, name)'''

from tkinter import *
import tkinter.messagebox as mb

root = tkinter.Tk()
root.title("My Contact Book")
root.geometry('700x550')
root.resizable(0, 0)
# Creating the color and font variables
lf_bg = 'Gray85'  # Lightest Shade
cf_bg = 'Gray57'
rf_bg = 'Gray35'  # Darkest Shade
frame_font = ("Garamond", 14)


# Creating the StringVar variables
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()
#1
search_strvar=StringVar()

# Creating and placing the components in the window
Label(root, text='CONTACT BOOK', font=("Noto Sans CJK TC", 15, "bold"), bg='Black', fg='White').pack(side=TOP, fill=X)
# Frame on the left
left_frame = Frame(root, bg=lf_bg) 
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)
# Frame in the center
center_frame = Frame(root, bg=cf_bg)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)
# Frame on the right
right_frame = Frame(root, bg=rf_bg)
right_frame.place(relx=0.6, relwidth=0.4, relheight=1, y=30)


# Placing components in the left frame
Label(left_frame, text='Name', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.05)
name_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=name_strvar)
name_entry.place(relx=0.1, rely=0.1)
Label(left_frame, text='Phone no.', bg=lf_bg, font=frame_font).place(relx=0.23, rely=0.2)
phone_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=phone_strvar)
phone_entry.place(relx=0.1, rely=0.25)
Label(left_frame, text='Email', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.35)
email_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=email_strvar)
email_entry.place(relx=0.1, rely=0.4)


Label(left_frame, text='Address', bg=lf_bg, font=frame_font).place(relx=0.28, rely=0.5)
address_entry = Text(left_frame, width=15, font=("Verdana", 11), height=5)
address_entry.place(relx=0.1, rely=0.55)

# Placing components in the Middle Frame
search_entry = Entry(center_frame, width=18, font=("Verdana", 12), textvariable=search_strvar).place(relx=0.08, rely=0.04)

# Placing components in the Right Frame
Label(right_frame, text='Saved Contacts', font=("Noto Sans CJK TC", 14), bg=rf_bg).place(relx=0.25, rely=0.05)
listbox = Listbox(right_frame, selectbackground='SkyBlue', bg='Gainsboro', font=('Helvetica', 12), height=20, width=25)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.1, rely=0.15)
#2list_contacts()

# Defining the functions
def submit_record():
    global name_strvar, email_strvar, phone_strvar, address_entry
    global cursor
    name, email, phone, address = name_strvar.get(), email_strvar.get(), phone_strvar.get(), address_entry.get(1.0, END)
    if name=='' or email=='' or phone=='' or address=='':
        mb.showerror('Error!', "Please fill all the fields!")
    else:
        cursor.execute(
        "INSERT INTO CONTACT_BOOK (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (?,?,?,?)", (name, email, phone, address))
        connector.commit()
        mb.showinfo('Contact added', 'We have stored the contact successfully!')



def view_record():
    global name_strvar, phone_strvar, email_strvar, address_entry, listbox
    curr = cursor.execute('SELECT * FROM CONTACT_BOOK WHERE NAME=?', listbox.get(ACTIVE))
    values = curr.fetchall()[0]
    name_strvar.set(values[1]); phone_strvar.set(values[3]); email_strvar.set(values[2])
    address_entry.delete(1.0, END)
    address_entry.insert(END, values[4])
       