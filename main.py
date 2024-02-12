import customtkinter as tk
from tkinter import messagebox

# Function to save the birthday
def save_birthday():
    name = name_entry.get()
    date = date_entry.get()
    with open('file.txt', 'a') as file:
        file.write(f"\n{date} {name}")
    messagebox.showinfo("Success", "Birthday saved successfully!")

# Create the main window
root = tk.CTk()
root.title("Birthday Reminder")

# Create and place labels
tk.CTkLabel(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
tk.CTkLabel(root, text="Date (MMDD):").grid(row=1, column=0, padx=10, pady=5)

# Create and place entry fields
name_entry = tk.CTkEntry(root)
date_entry = tk.CTkEntry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
date_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place a button to save the birthday
save_button = tk.CTkButton(root, text="Save Birthday", command=save_birthday)
save_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
