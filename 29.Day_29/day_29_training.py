import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import string
import random
import json
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui_setup()
        
    

        
  
    def clear_entries(self):
        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.website_entry.focus()

    def check_website_length(self):
        website = self.website_entry.get()
        if len(website) == 0:
            tk.messagebox.showinfo(title="Error!", message="Website is mandatory.")
            return True
        return False


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
        for entry in self.matching_entries:
            listbox.insert(tk.END, entry['email'])


    def on_select(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        selected_entry = self.matching_entries[index]
        self.insert_matching_entry(selected_entry)
        
        self.selection_window.destroy()
        



    def insert_matching_entry(self, entry):
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)      
        self.email_entry.insert(0, entry["email"])
        self.password_entry.insert(0, entry["password"])
       







    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(15))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
    
    def lookup_entry(self):
        if self.check_website_length():
            
            return
        self.check_email_match()
    
    def check_email_match(self):
        website = self.website_entry.get().strip()
        data = self.read_entries_from_file()

        if website in data:
            self.matching_entries = data[website]
            self.process_matching_entries()
        else:
            tk.messagebox.showinfo(title="No Match Found", message="No entries found for the website.")


     
    def process_matching_entries(self):
        if len(self.matching_entries) == 1:
            self.insert_matching_entry(self.matching_entries[0])
            tk.messagebox.showinfo(title="Match Found", message="Match found for the website.")
        elif len(self.matching_entries) > 1:
            self.open_selection_window()



   
        

    def add_entry(self):
        website = self.website_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not website or not email or not password:
            tk.messagebox.showinfo(title="Error!", message="Please don't leave any fields empty!")
            return

        data = self.read_entries_from_file()

        # Check if the website already exists in data
        if website not in data:
            data[website] = []

        # Check for duplicate email under the same website
        if any(entry["email"] == email for entry in data[website]):
            tk.messagebox.showinfo(title="Duplicate Entry", message="This email for the website already exists!")
            return

        # Add the new email and password to the website's list
        data[website].append({"email": email, "password": password})
        self.write_entries_to_file(data)

        # Clear the input fields
        self.website_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, "oferteevelin1996.com")
        self.website_entry.focus()

    
    def read_entries_from_file(self):
        try:
            with open("29.Day_29/data.json", mode="r") as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            
            return {}  # Return an empty dictionary if file doesn't exist or is empty

    def write_entries_to_file(self, data):
        with open("29.Day_29/data.json", mode="w") as file:
            json.dump(data, file,indent=4)

       
    
    
  
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
        self.clear_entries_button = tk.Button(text="Clear Entry", width=15, command=self.clear_entries,font=("arial", 12, 'bold'), bg="black", fg="white", highlightthickness=0,activebackground="black", activeforeground="black",border=0, highlightbackground='black', highlightcolor='black')
        
        
        self.website_text_label = self.canvas.create_text(200, 350, text="Website:", font=("Arial", 12, "bold"), fill="white")
        self.email_text_label = self.canvas.create_text(210, 400, text="Email:", font=("Arial", 12, "bold"), fill="white")
        self.password_text_label = self.canvas.create_text(190, 450, text="Password:", font=("Arial", 12, "bold"), fill="white")
        
        
        
        
        self.canvas.create_window(370, 500, window=self.clear_entries_button)
        self.canvas.create_window(250, 500, window=self.add_entry_button)
        self.canvas.create_window(350, 350, window=self.website_entry)
        self.canvas.create_window(350, 400, window=self.email_entry)
        self.canvas.create_window(310, 450, window=self.password_entry)
        self.canvas.create_window(470, 450, window=self.generate_password_button)
        self.canvas.create_window(470, 350, window=self.lookup_entry_button)
 



if __name__ == "__main__":
    app = PasswordManager()
    app.mainloop()

