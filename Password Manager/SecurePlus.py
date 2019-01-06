from tkinter import *
from password_generator import *

    
def info_popup():
    win = Toplevel()
    win.wm_title("More Info")

    l = Label(win, text="In order to generate a unique and secure password, unique parameters are required.\n The first 3 parameters are self explanatory, the 4th one however, isn't.\n The purpose of version number is so that you can have a different password generated,\n with the other parameters unchanged. As a side note, it is recommended to \nuse the max length for password, as it will be harder to crack.",bg='#66ccff')
    l.grid(row=0, column=0)

    close = Button(win, text="Close", command=win.destroy,bg="Black",fg="White")
    close.grid(row=1, column=0)

    win.configure(background='#66ccff')

def set_text(entry,text):
    entry.config(state=NORMAL)
    entry.delete(1.0,END)
    entry.insert("end", text)
    entry.config(state=DISABLED)
    entry.update()
        
def display_passowrd(event):

    alphabet = ""
    if lower_state.get():
        alphabet+="abcdefghijklmnopqrstuvwxyz"
    if upper_state.get():
        alphabet+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if nums_state.get():
        alphabet+="0123456789"
    if special_char_state.get():
        alphabet+="!@#$%^&*()-_"

    website=entry_website.get()
    user_name=entry_user.get()
    master_password=entry_master_pass.get()
    version=entry_version.get()
    length=entry_passwrd_len.get()
    if not (website and user_name and master_password and version and alphabet and length):
        #put a pop up dialog here
        return
    length=int(length)
    password = generate_password(website, user_name, master_password, version,length, alphabet)
    set_text(psswrd_generated,password)
    print(alphabet)
    

root = Tk()

alphabet = []

lower_state, upper_state, nums_state, special_char_state = IntVar(value=1),IntVar(value=1),IntVar(value=1),IntVar(value=1)

lower = Checkbutton(root, text="lowercase",bg="#66ccff",variable=lower_state)
upper = Checkbutton(root, text="UPPERCASE",bg="#66ccff",variable=upper_state)
nums = Checkbutton(root, text="Numbers",bg="#66ccff",variable=nums_state)
special_char = Checkbutton(root, text="Special Characters",bg="#66ccff",variable=special_char_state)



lower.grid(row=6,column=0)
upper.grid(row=6,column=1)
nums.grid(row=7,column=0)
special_char.grid(row=7,column=1)

label_website = Label(root, text="Domain name: ",bg='#66ccff')
entry_website = Entry(root)
label_website.grid(row=0, column = 0)
entry_website.grid(row=0, column = 1)

label_user = Label(root, text="Username: ",bg='#66ccff')
entry_user = Entry(root)
label_user.grid(row=1, column = 0)
entry_user.grid(row=1, column = 1)

label_master_pass = Label(root, text="Master password: ",bg='#66ccff')
entry_master_pass = Entry(root,show="*")
label_master_pass.grid(row=2, column = 0)
entry_master_pass.grid(row=2, column = 1)

label_version = Label(root, text="Version number: ",bg='#66ccff')
entry_version = Entry(root)
label_version.grid(row=3, column = 0)
entry_version.grid(row=3, column = 1)

label_passwrd_len = Label(root, text="Password length desired: ",bg='#66ccff')
entry_passwrd_len = Entry(root)
label_passwrd_len.grid(row=4, column = 0)
entry_passwrd_len.grid(row=4, column = 1)

button_generate = Button(root,text="Generate",height=3,width=15,bg="#000000",fg="white")
psswrd_generated = Text(root, state=DISABLED,height=5, width=16)

button_generate.bind("<Button-1>",display_passowrd)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="More Info",command=info_popup)
menubar.add_cascade(label="Help", menu=filemenu)
root.config(menu=menubar)


button_generate.grid(row=5,column=0)
psswrd_generated.grid(row=5,column=1)

root.title("SecurePlus")
root.configure(background='#66ccff')

root.mainloop()
