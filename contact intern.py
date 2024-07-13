import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
import os

# Load contacts from file
def load_contacts():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.configure(bg='#f0f0f0')
        self.contacts = load_contacts()

        # Frames
        self.frame_top = tk.Frame(root, bg='#f0f0f0')
        self.frame_top.pack(pady=10, padx=10, fill='x')

        self.frame_middle = tk.Frame(root, bg='#f0f0f0')
        self.frame_middle.pack(pady=10, padx=10, fill='x')

        self.frame_bottom = tk.Frame(root, bg='#f0f0f0')
        self.frame_bottom.pack(pady=10, padx=10, fill='x')

        # Add Contact Form
        tk.Label(self.frame_top, text="Name:", bg='#f0f0f0').grid(row=0, column=0, sticky='e')
        self.entry_name = tk.Entry(self.frame_top)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_top, text="Phone Number:", bg='#f0f0f0').grid(row=1, column=0, sticky='e')
        self.entry_phone = tk.Entry(self.frame_top)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_top, text="Email:", bg='#f0f0f0').grid(row=2, column=0, sticky='e')
        self.entry_email = tk.Entry(self.frame_top)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.frame_top, text="Address:", bg='#f0f0f0').grid(row=3, column=0, sticky='e')
        self.entry_address = tk.Entry(self.frame_top)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame_top, text="Add Contact", command=self.add_contact, bg='#4CAF50', fg='white')
        self.add_button.grid(row=4, columnspan=2, pady=10)

        # Contact List
        self.contact_listbox = tk.Listbox(self.frame_middle, width=50, height=10)
        self.contact_listbox.pack(padx=10, pady=10)
        self.contact_listbox.bind('<<ListboxSelect>>', self.show_contact_details)

        # Contact Details
        self.contact_details = tk.StringVar()
        tk.Label(self.frame_middle, textvariable=self.contact_details, bg='#f0f0f0').pack(pady=5)

        # Buttons for updating and deleting contacts
        self.update_button = tk.Button(self.frame_bottom, text="Update Contact", command=self.update_contact, bg='#FFC107', fg='white')
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.frame_bottom, text="Delete Contact", command=self.delete_contact, bg='#F44336', fg='white')
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.load_contact_list()

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            save_contacts(self.contacts)
            self.load_contact_list()
            self.clear_form()
        else:
            messagebox.showwarning("Input Error", "Name and Phone Number are required")

    def load_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact['name'])

    def show_contact_details(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            self.contact_details.set(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            name = simpledialog.askstring("Update Contact", "Name:", initialvalue=contact['name'])
            phone = simpledialog.askstring("Update Contact", "Phone:", initialvalue=contact['phone'])
            email = simpledialog.askstring("Update Contact", "Email:", initialvalue=contact['email'])
            address = simpledialog.askstring("Update Contact", "Address:", initialvalue=contact['address'])

            if name and phone:
                updated_contact = {"name": name, "phone": phone, "email": email, "address": address}
                self.contacts[selected_index[0]] = updated_contact
                save_contacts(self.contacts)
                self.load_contact_list()
                self.contact_details.set("")
            else:
                messagebox.showwarning("Input Error", "Name and Phone Number are required")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
            if confirm:
                self.contacts.pop(selected_index[0])
                save_contacts(self.contacts)
                self.load_contact_list()
                self.contact_details.set("")

    def clear_form(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
