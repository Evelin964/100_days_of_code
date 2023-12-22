import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import string
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui_setup()
        
    
  
    

    def check_website_length(self):
        website = self.website_entry.get()
        if len(website) == 0:
            tk.messagebox.showinfo(title="Error!", message="Website is mandatory.")
            return True
        return False


    def check_email_match(self):
        website = self.website_entry.get()
        self.matching_entries = self.read_entries_from_file(website)

        if self.matching_entries:
            if len(self.matching_entries) > 1:
                self.open_selection_window()
            else:
                self.insert_matching_entry(self.matching_entries[0])
                tk.messagebox.showinfo(title="Match Found", message="Match found for the website.")
        else:
            tk.messagebox.showinfo(title="No Match Found", message="No entries found for the website.")

    def open_selection_window(self):
        self.selection_window = tk.Toplevel(self)
        self.selection_window.title("Select an Email")
        self.selection_window.resizable(False, False)
        self.selection_window.geometry("200x200")

        self.position_selection_window(200, 200)  # Pass the width and height of the window

        listbox = tk.Listbox(self.selection_window)
        self.configure_listbox(listbox)
        self.populate_listbox(listbox)

        listbox.bind('<<ListboxSelect>>', self.on_select)

        # Make the window modal and transient
        self.selection_window.grab_set()
        self.selection_window.attributes("-topmost", True)
        self.selection_window.transient(self)

    def position_selection_window(self, width, height):
        # Center the selection window over the parent window
        parent_x = self.winfo_rootx()
        parent_y = self.winfo_rooty()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()
        x = parent_x + (parent_width - width) // 2
        y = parent_y + (parent_height - height) // 2
        self.selection_window.geometry(f"+{x}+{y}")

    def configure_listbox(self, listbox):
        # Configure the Listbox appearance and behavior
        listbox.grid(column=0, row=0, sticky="nsew")
        self.selection_window.grid_columnconfigure(0, weight=1)
        self.selection_window.grid_rowconfigure(0, weight=1)
        listbox.focus()
        listbox.configure(border=0, highlightthickness=0, justify=tk.CENTER)

    def populate_listbox(self, listbox):
        # Populate the Listbox with email entries
        for entry in self.matching_entries:
            email = entry.split("|")[1].strip()
            listbox.insert(tk.END, email)



    def on_select(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        selected_entry = self.matching_entries[index]
        self.insert_matching_entry(selected_entry)
        self.selection_window.destroy()
        tk.messagebox.showinfo(title="Match Found", message="Match found for the website.")


    def read_entries_from_file(self, website):
        with open("29.Day_29/data.txt", mode="r") as file:
            data = file.readlines()
            matching_entries = []
            for line in data:
                entry = line.split("|")
                if website.lower() == entry[0].strip().lower():
                    matching_entries.append(line)
                    
        return matching_entries

    def insert_matching_entry(self, entry):
        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.website_entry.insert(0, entry.split("|")[0].strip())
        self.email_entry.insert(0, entry.split("|")[1].strip())
        self.password_entry.insert(0, entry.split("|")[2].strip())


    def lookup_entry(self):
        if self.check_website_length():
            return
        self.check_email_match()

    
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(15))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        
    def add_entry(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            tk.messagebox.showinfo(title="Error!", message="Please don't leave any fields empty!")
        else:
            is_duplicate = self.check_duplicate_entry(website, email)
            if is_duplicate:
                tk.messagebox.showinfo(title="Duplicate Entry", message="This entry already exists!")
            else:
                is_ok = tk.messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
                if is_ok:
                    with open("29.Day_29/data.txt", mode="a") as file:
                        file.write(f"{website} | {email} | {password}\n")
                        self.website_entry.delete(0, tk.END)
                        self.password_entry.delete(0, tk.END)
                        self.website_entry.focus()

    def check_duplicate_entry(self, website, email):
        with open("29.Day_29/data.txt", mode="r") as file:
            data = file.readlines()
            for line in data:
                entry = line.split("|")
                if website.lower() == entry[0].strip().lower() and email.lower() == entry[1].strip().lower():
                    return True
        return False
    
      
    def ui_setup(self):
        self.title("Password Manager")
        self.resizable(False, False)
        
        lock_img = Image.open("29.Day_29/logo.png")
        lock_img = lock_img.resize((200, 200))
        logo_img = ImageTk.PhotoImage(lock_img)
        
        self.canvas = tk.Canvas(width=600, height=600, bg="black", highlightthickness=0)
        self.canvas.create_image(300, 200, image=logo_img)
        self.canvas.image = logo_img
        self.canvas.grid(column=1, row=0)
        
        self.website_entry = tk.Entry()
        self.website_entry.grid(column=1, row=0)
        self.website_entry.config(width=35)
        self.website_entry.focus()
        
        self.email_entry = tk.Entry()  
        self.email_entry.grid(column=1, row=1)
        self.email_entry.config(width=35)
        self.email_entry.insert(0,"oferteevelin1996.com")
        
        self.password_entry = tk.Entry()
        self.password_entry.grid(column=1, row=2)
        self.password_entry.config(width=21)
        
        
        self.generate_password_button = tk.Button(text="Generate Password", width=15, command=self.generate_password,font=("arial", 12, 'bold'), bg="black", fg="white", highlightthickness=0,activebackground="black", activeforeground="black",border=0, highlightbackground='black', highlightcolor='black')
        self.generate_password_button.grid(column=1, row=3)

        self.add_entry_button = tk.Button(text="Add Entry", width=36, font=("arial", 12, 'bold'), bg="black", fg="white", highlightthickness=0,activebackground="black", activeforeground="black",border=0, highlightbackground='black', highlightcolor='black',command=self.add_entry)
        self.add_entry_button.grid(column=1, row=4)
        
        self.lookup_entry_button = tk.Button(text="Lookup Entry", width=15, command=self.lookup_entry,font=("arial", 12, 'bold'), bg="black", fg="white", highlightthickness=0,activebackground="black", activeforeground="black",border=0, highlightbackground='black', highlightcolor='black')
        
        
        
        self.website_text_label = self.canvas.create_text(200, 350, text="Website:", font=("Arial", 12, "bold"), fill="white")
        self.email_text_label = self.canvas.create_text(210, 400, text="Email:", font=("Arial", 12, "bold"), fill="white")
        self.password_text_label = self.canvas.create_text(190, 450, text="Password:", font=("Arial", 12, "bold"), fill="white")
        
        
        
        
        
        self.canvas.create_window(350, 350, window=self.website_entry)
        self.canvas.create_window(350, 400, window=self.email_entry)
        self.canvas.create_window(310, 450, window=self.password_entry)
        self.canvas.create_window(470, 450, window=self.generate_password_button)
        self.canvas.create_window(300, 500, window=self.add_entry_button)
        self.canvas.create_window(470, 350, window=self.lookup_entry_button)
 


if __name__ == "__main__":
    app = PasswordManager()
    app.mainloop()

