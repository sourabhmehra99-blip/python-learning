import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root  # Stores the main window inside the class
        self.root.title("My App")

    def login(self):
        # Create a new window for login
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        # Create labels and entry fields for username and password
        tk.Label(login_window, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(login_window)
        self.username_entry.grid(row=0, column=1)

        tk.Label(login_window, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(login_window, show="*")
        self.password_entry.grid(row=1, column=1)

        # Create a submit button
        submit_button = tk.Button(login_window, text="Submit", command=self.submit_login)
        submit_button.grid(row=2, columnspan=2)

main_window = tk.Tk()
app = App(main_window)
app.login()
main_window.mainloop()
