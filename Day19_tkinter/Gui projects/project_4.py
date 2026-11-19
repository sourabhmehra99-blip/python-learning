import tkinter as tk
from tkinter import messagebox


def handle_login() -> None:
	"""Validate inputs and simulate a login check."""
	username = username_entry.get().strip()
	password = password_entry.get()

	if not username or not password:
		messagebox.showwarning("Missing Input", "Please enter both username and password.")
		return

	# Demo credentials for learning purposes.
	if username == "admin" and password == "1234":
		messagebox.showinfo("Login Success", f"Welcome, {username}!")
		status_label.config(text="Login successful", fg="green")
	else:
		messagebox.showerror("Login Failed", "Invalid username or password.")
		status_label.config(text="Login failed", fg="red")


def toggle_password() -> None:
	"""Show or hide password text based on checkbox state."""
	password_entry.config(show="" if show_password_var.get() else "*")


window = tk.Tk()
window.title("Login Form")
window.geometry("360x250")
window.resizable(False, False)

title_label = tk.Label(window, text="Login", font=("Segoe UI", 18, "bold"))
title_label.pack(pady=(15, 10))

form_frame = tk.Frame(window)
form_frame.pack(padx=20, pady=5, fill="x")

username_label = tk.Label(form_frame, text="Username:", anchor="w")
username_label.grid(row=0, column=0, sticky="w", pady=5)

username_entry = tk.Entry(form_frame, width=30)
username_entry.grid(row=0, column=1, pady=5)

password_label = tk.Label(form_frame, text="Password:", anchor="w")
password_label.grid(row=1, column=0, sticky="w", pady=5)

password_entry = tk.Entry(form_frame, width=30, show="*")
password_entry.grid(row=1, column=1, pady=5)

show_password_var = tk.BooleanVar(value=False)
show_password_check = tk.Checkbutton(
	form_frame,
	text="Show password",
	variable=show_password_var,
	command=toggle_password,
)
show_password_check.grid(row=2, column=1, sticky="w", pady=(2, 8))

login_button = tk.Button(window, text="Login", width=15, command=handle_login)
login_button.pack(pady=8)

status_label = tk.Label(window, text="", font=("Segoe UI", 10))
status_label.pack(pady=5)

window.bind("<Return>", lambda event: handle_login())
username_entry.focus_set()

window.mainloop()
