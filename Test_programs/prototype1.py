import tkinter as tk
from tkinter import ttk, messagebox


def convert_length(value, from_unit, to_unit):
    factors = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
    }
    value_in_meters = value * factors[from_unit]
    return value_in_meters / factors[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return (celsius * 9 / 5) + 32
    return celsius + 273.15


class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("560x380")
        self.root.resizable(False, False)

        self.category_var = tk.StringVar(value="Length")
        self.input_var = tk.StringVar()
        self.from_unit_var = tk.StringVar(value="km")
        self.to_unit_var = tk.StringVar(value="m")
        self.result_var = tk.StringVar(value="Result will appear here")

        self.length_units = ["km", "m", "cm", "mm"]
        self.temperature_units = ["C", "F", "K"]

        self.create_widgets()
        self.update_units()

    def create_widgets(self):
        main = ttk.Frame(self.root, padding=20)
        main.pack(fill="both", expand=True)

        title = ttk.Label(main, text="Unit Converter", font=("Segoe UI", 20, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=(0, 16))

        ttk.Label(main, text="Category", font=("Segoe UI", 11)).grid(
            row=1, column=0, sticky="w", pady=8
        )
        category_menu = ttk.Combobox(
            main,
            textvariable=self.category_var,
            values=["Length", "Temperature"],
            state="readonly",
            width=20,
        )
        category_menu.grid(row=1, column=1, sticky="ew", pady=8)
        category_menu.bind("<<ComboboxSelected>>", lambda _event: self.update_units())

        ttk.Label(main, text="Value", font=("Segoe UI", 11)).grid(
            row=2, column=0, sticky="w", pady=8
        )
        self.value_entry = ttk.Entry(main, textvariable=self.input_var, width=24)
        self.value_entry.grid(row=2, column=1, sticky="ew", pady=8)

        ttk.Label(main, text="From", font=("Segoe UI", 11)).grid(
            row=3, column=0, sticky="w", pady=8
        )
        self.from_menu = ttk.Combobox(main, textvariable=self.from_unit_var, state="readonly", width=20)
        self.from_menu.grid(row=3, column=1, sticky="ew", pady=8)

        ttk.Label(main, text="To", font=("Segoe UI", 11)).grid(
            row=4, column=0, sticky="w", pady=8
        )
        self.to_menu = ttk.Combobox(main, textvariable=self.to_unit_var, state="readonly", width=20)
        self.to_menu.grid(row=4, column=1, sticky="ew", pady=8)

        button_frame = ttk.Frame(main)
        button_frame.grid(row=5, column=0, columnspan=3, pady=(16, 12), sticky="ew")

        convert_btn = ttk.Button(button_frame, text="Convert", command=self.handle_convert)
        convert_btn.pack(side="left", padx=(0, 10))

        swap_btn = ttk.Button(button_frame, text="Swap Units", command=self.swap_units)
        swap_btn.pack(side="left")

        clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_fields)
        clear_btn.pack(side="left", padx=(10, 0))

        result_box = ttk.Label(
            main,
            textvariable=self.result_var,
            font=("Segoe UI", 12, "bold"),
            anchor="center",
            relief="groove",
            padding=12,
        )
        result_box.grid(row=6, column=0, columnspan=3, sticky="ew", pady=(10, 0))

        for col in range(3):
            main.columnconfigure(col, weight=1)

    def update_units(self):
        units = self.length_units if self.category_var.get() == "Length" else self.temperature_units

        self.from_menu["values"] = units
        self.to_menu["values"] = units

        self.from_unit_var.set(units[0])
        self.to_unit_var.set(units[1])
        self.result_var.set("Result will appear here")

    def swap_units(self):
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        self.from_unit_var.set(to_unit)
        self.to_unit_var.set(from_unit)

    def clear_fields(self):
        self.input_var.set("")
        self.result_var.set("Result will appear here")
        self.value_entry.focus()

    def handle_convert(self):
        raw_value = self.input_var.get().strip()
        if not raw_value:
            messagebox.showwarning("Missing value", "Please enter a number first.")
            return

        try:
            value = float(raw_value)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid numeric value.")
            return

        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        category = self.category_var.get()

        if category == "Length":
            result = convert_length(value, from_unit, to_unit)
        else:
            result = convert_temperature(value, from_unit, to_unit)

        self.result_var.set(f"{value:.4f} {from_unit} = {result:.4f} {to_unit}")


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()

