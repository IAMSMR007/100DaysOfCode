from tkinter import *
GREEN = "#9bdeac"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Saved():
    website=input_web.get()
    email=input_email.get()
    password=input_pass.get()
    with open("Saved_Password.txt","a") as data:
        data.write(f"{website} | {email} | {password}\n")
        print("Saving.......")
        input_web.delete(0,END)
        input_pass.delete(0,END)


    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20,bg=GREEN)

#Canvas
canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0,column=1)

#Labels
web_lebel=Label(text="Website:", highlightthickness=0,bg=GREEN)
web_lebel.grid(row=1,column=0)
user_lebel=Label(text="Email/Username:", highlightthickness=0,bg=GREEN)
user_lebel.grid(row=2,column=0)
pass_lebel=Label(text="Password:", highlightthickness=0,bg=GREEN)
pass_lebel.grid(row=3,column=0)


#Entries
input_web=Entry(width=42) 
input_web.focus()
input_web.grid(column=1,row=1,columnspan=2)
input_email=Entry(width=42)
input_email.insert(0,"abc@gmail.com")
input_email.grid(column=1,row=2,columnspan=2)
input_pass=Entry(width=32)
input_pass.grid(column=1,row=3)


#Button
gen_button=Button(text="Generate",command=Password,bg="#e2979c")
gen_button.grid(column=2,row=3)

add_button=Button(text="Save Password",command=Saved,bg="#e7305b")
add_button.grid(row=4,column=1)






window.mainloop()