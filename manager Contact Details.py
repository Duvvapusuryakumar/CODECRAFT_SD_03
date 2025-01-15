import tkinter as tk
from tkinter import messagebox

# In-memory contact storage
contacts = {}

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required.")
        return

    if name in contacts:
        messagebox.showerror("Error", "A contact with this name already exists.")
        return

    contacts[name] = {"phone": phone, "email": email}
    update_contact_list()
    clear_entries()
    messagebox.showinfo("Success", f"Contact {name} added successfully.")

def view_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "No contact selected.")
        return

    name = listbox_contacts.get(selected)
    contact = contacts[name]
    messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")

def edit_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "No contact selected.")
        return

    name = listbox_contacts.get(selected)
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    update_contact_list()
    clear_entries()
    messagebox.showinfo("Success", f"Contact {name} updated successfully.")

def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "No contact selected.")
        return

    name = listbox_contacts.get(selected)
    del contacts[name]
    update_contact_list()
    messagebox.showinfo("Success", f"Contact {name} deleted successfully.")

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name in contacts:
        listbox_contacts.insert(tk.END, name)

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Create GUI
root = tk.Tk()
root.title("Contact Manager")

# Input frame
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_inputs, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_inputs, width=30)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_inputs, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Buttons frame
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Contact", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="View Contact", command=view_contact).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Edit Contact", command=edit_contact).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Delete Contact", command=delete_contact).grid(row=0, column=3, padx=5)

# Contact list
frame_list = tk.Frame(root)
frame_list.pack(pady=10)

listbox_contacts = tk.Listbox(frame_list, width=50, height=15)
listbox_contacts.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_contacts.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_contacts.yview)

# Populate contact list
update_contact_list()

root.mainloop()
