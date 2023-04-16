from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

FILE_NAME = "data.json"


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '@', '_']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)
    password_entry.delete(0, END)
    password = "".join(password_list)
    password_entry.insert(0, password)


def save_password():
    """
    Retrieve the data that the user inserted in the text fields, and saves it to a json file.
    """
    update_file = True
    website_name = website_entry.get()
    email_uname = email_username.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email_uname,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details that you entered: "
                                                                   f"\nEmail: {email_uname}"
                                                                   f"\nPassword: {password} \nIs this okay to save?")

        if is_ok:
            data = None
            try:
                with open(FILE_NAME, mode="r") as data_file:
                    # Read the old data
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
            else:
                if website_name in data:
                    is_yes = messagebox.askyesno("Warning",
                                                 message=f"There is already a password for {website_name}.\n"
                                                         f"Would you like to overwrite it?")

                    if is_yes:
                        # Update the password
                        data[website_name]["password"] = password
                    else:
                        update_file = False
                else:
                    # Update the old data with the new data
                    data.update(new_data)
            finally:
                if update_file is True:
                    # Save the new/updated data to the file
                    with open(FILE_NAME, mode="w") as data_file:
                        json.dump(data, data_file, indent=4)

                # Clear the fields after saving the data
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search_data():
    """
    Searches the data from the json file based on the website name the user entered. If the name exists,
    it returns the data associated with the website, i.e. the username and password.
    """
    website = website_entry.get()
    try:
        with open(FILE_NAME, mode="r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"The file: {FILE_NAME} does not exist.")
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="Error",
                             message="There is no data to decode.")
    else:
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]

            messagebox.showinfo(title=website_entry.get(),
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for the website: '{website}' exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, borderwidth=2)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="EW")

email_username = Entry()
email_username.insert(0, "example@gmail.com")
email_username.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

search_btn = Button(text="Search", command=search_data)
search_btn.grid(row=1, column=2, sticky="EW")

window.mainloop()
