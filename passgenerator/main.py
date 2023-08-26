import customtkinter as ctk

from generator import generate_password

number_of_symbols = 12

ctk.set_appearance_mode("light")

root = ctk.CTk()

root.title("Pass Generator")

root.geometry("200x150")

root.resizable(0, 0)

text_output = ctk.CTkEntry(root, placeholder_text='PASSWORD', justify="center", width=180, fg_color="#5727A3", text_color="#D6C5F0")

text_output.grid(row=0, column=0, padx=1, pady=(0, 60))

def slider_event(value):
    global number_of_symbols
    number_of_symbols = int(value)
    print(number_of_symbols)

slider = ctk.CTkSlider(root, from_=6, to=18, command=slider_event, fg_color="#D6C5F0", button_hover_color="#1B0044", button_color="#5727A3")

slider.grid(row=0, column=0, padx=1, pady=(130, 0))

def radiobutton_event():
    ctk.set_appearance_mode("light")

def radiobutton_event1():
    ctk.set_appearance_mode("dark")

radio_var = ctk.IntVar(value=0)
radiobutton_1 = ctk.CTkRadioButton(root, text="light", fg_color="#D6C5F0",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = ctk.CTkRadioButton(root, text="dark", fg_color="#D6C5F0",
                                             command=radiobutton_event1, variable= radio_var, value=2)

radiobutton_1.grid(row=0, column=0, padx=(0, 80), pady=(0, 115))
radiobutton_2.grid(row=0, column=0, padx=(40, 0), pady=(0, 115))

def button_callback():
    text_output.delete(0, 24)
    button1 = generate_password(number_of_symbols)
    text_output.insert(0, button1)


button = ctk.CTkButton(root, text="Сгенерировать пароль", width=180, fg_color="#5727A3", hover_color="#1B0044", text_color="#D6C5F0", command=button_callback)

button.grid(row=0, column=0, padx=1, pady=(20, 0))

root.mainloop()