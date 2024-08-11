import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox

# Path to the JSON file that will store the contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the JSON file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save contacts to the JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")

    if name and phone and email:
        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)
        save_contacts(contacts)
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# View all contacts
def update_contact_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

# Edit an existing contact
def edit_contact():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]

        name = simpledialog.askstring("Input", f"Enter new name (current: {contact['name']}):", initialvalue=contact['name'])
        phone = simpledialog.askstring("Input", f"Enter new phone number (current: {contact['phone']}):", initialvalue=contact['phone'])
        email = simpledialog.askstring("Input", f"Enter new email (current: {contact['email']}):", initialvalue=contact['email'])

        if name and phone and email:
            contacts[index] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            update_contact_list()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to edit.")

# Delete a contact
def delete_contact():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contacts.pop(index)
        save_contacts(contacts)
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Animation for button hover
def on_enter(e, color):
    e.widget['background'] = color

def on_leave(e, color):
    e.widget['background'] = color

# Main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.configure(bg="#E8F9FD")

# Load contacts
contacts = load_contacts()

# UI Elements
frame = tk.Frame(root, bg="#007ACC", padx=10, pady=10)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = tk.Label(frame, text="Contact Book", font=("Helvetica", 24, "bold"), fg="#FFFFFF", bg="#007ACC")
label.pack(pady=10)

listbox = Listbox(frame, font=("Helvetica", 14), bg="#FFFFFF", fg="#007ACC", selectbackground="#FFDD57", selectforeground="#007ACC")
listbox.pack(fill="both", expand=True, pady=10)
update_contact_list()

button_frame = tk.Frame(frame, bg="#007ACC")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", font=("Helvetica", 14), bg="#28A745", fg="#FFFFFF", command=add_contact)
add_button.grid(row=0, column=0, padx=5)

edit_button = tk.Button(button_frame, text="Edit Contact", font=("Helvetica", 14), bg="#FFC107", fg="#FFFFFF", command=edit_contact)
edit_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", font=("Helvetica", 14), bg="#DC3545", fg="#FFFFFF", command=delete_contact)
delete_button.grid(row=0, column=2, padx=5)

# Add animations on button hover
add_button.bind("<Enter>", lambda e: on_enter(e, "#218838"))
add_button.bind("<Leave>", lambda e: on_leave(e, "#28A745"))
edit_button.bind("<Enter>", lambda e: on_enter(e, "#E0A800"))
edit_button.bind("<Leave>", lambda e: on_leave(e, "#FFC107"))
delete_button.bind("<Enter>", lambda e: on_enter(e, "#C82333"))
delete_button.bind("<Leave>", lambda e: on_leave(e, "#DC3545"))

# Start the Tkinter main loop
root.mainloop()
