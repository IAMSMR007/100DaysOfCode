from tkinter import *
from tkinter import messagebox
import random
import json
import string
# Define background color
GREEN = "#9bdeac"

#-----------------------------Search button----------------------
def Search():
    website = input_web.get().strip().lower()  # convert to lowercase to avoid case mismatches
    try:
        with open("Saved_Password.json", "r") as data_file:
            dict_to_search = json.load(data_file)  # Read existing data
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error", message="No saved passwords file found.")
        return
    if website in dict_to_search:
        main_dict = dict_to_search[website]
        emailX = main_dict["email"]
        passwordX = main_dict["password"]
        messagebox.askokcancel(title=website, message=f"Details:\nEmail: {emailX} \nPassword: {passwordX}")
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for '{website}' exist.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Password():
    """Generates a random password and inserts it into the password entry field."""
    
    # Define characters to be used in the password
    letters = string.ascii_letters  # All uppercase & lowercase letters
    digits = string.digits  # Numbers 0-9
    symbols = string.punctuation  # Special characters (!, @, #, etc.)
    
    # Combine all characters and set password length
    characters = letters + digits + symbols
    password_length = 12  # You can change this value
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    # Insert the password into the entry field
    input_pass.delete(0, END)  # Clear previous entry
    input_pass.insert(0, password)  # Insert new password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Saved():
    website = input_web.get().strip().lower()  # use lowercase for consistency
    email = input_email.get().strip()
    password = input_pass.get().strip()

    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please fill in all fields.")
        return

    data_to_add = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("Saved_Password.json", "r") as data_file:
            dict_data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        dict_data = {}

    # If website already exists, ask for confirmation to update
    if website in dict_data:
        is_update = messagebox.askyesno(title="Confirm Update", message=f"An entry for '{website}' already exists. Do you want to update it?")
        if not is_update:
            return

    dict_data.update(data_to_add)

    with open("Saved_Password.json", "w") as data_file:
        json.dump(dict_data, data_file, indent=4)

    input_web.delete(0, END)
    input_pass.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Create main application window
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg=GREEN)  # Add padding and background color

# Create a Canvas widget (used for images, shapes, etc.)
canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)

# Try to load the image; show a warning if the file is missing
try:
    padlock_img = PhotoImage(file="logo.png")  # Load image
    canvas.create_image(100, 100, image=padlock_img)  # Add image to canvas
except TclError:
    messagebox.showwarning("Warning", "Image file 'logo.png' not found!")

canvas.grid(row=0, column=1)  # Place canvas at row 0, column 1

# Labels (for guiding user input)
web_label = Label(text="Website:", bg=GREEN)
web_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", bg=GREEN)
user_label.grid(row=2, column=0)

pass_label = Label(text="Password:", bg=GREEN)
pass_label.grid(row=3, column=0)

# Entry fields (where user inputs data)
input_web = Entry(width=25)  # Website entry
input_web.focus()  # Set cursor to this entry by default
input_web.grid(column=1, row=1)

input_email = Entry(width=25)  # Email entry
input_email.insert(0, "abc@gmail.com")  # Default email
input_email.grid(column=1, row=2)

input_pass = Entry(width=25)  # Password entry
input_pass.grid(column=1, row=3)

# Buttons (for user actions)
search_button=Button(text="Search",command=Search, bg="#e2979c",width=7)
search_button.grid(column=2,row=1)


gen_button = Button(text="Generate", command=Password, bg="#e2979c")  # Generate password button
gen_button.grid(column=2, row=3)

add_button = Button(text="Save Password", command=Saved, bg="#e7305b", width=36)  # Save button
add_button.grid(row=4, column=1, columnspan=2)

# Start the Tkinter main event loop
window.mainloop()


