from cProfile import label

import customtkinter as ctk

ctk.set_appearance_mode("dark")

app=ctk.CTk()
app.geometry("500x400")
app.title("Login Page")

label=ctk.CTkLabel(app,text="Enter your Name:", font=("Times", 20))
label.pack(pady=20)

# entry=ctk.CTkEntry(app,placeholder_text="Enter your Name")
entry=ctk.CTkEntry(app,width=250,font=("Helvetica",16))
entry.pack(pady=10)

label_result=ctk.CTkLabel(app,font=("Arial",20))
label_result.pack(pady=10)

def submit():
    user_input =entry.get()
    label_result.configure(text=user_input)

button=ctk.CTkButton(app,text="Submit", width=100, command=submit)
button.pack(pady=10)

app.mainloop()