import tkinter as tk
from tkinter import ttk

# Configures window and styles
window = tk.Tk()
window.title('Registration Form')
window.configure(bg="lightblue")
ttk.Style().configure("TButton", padding=6, relief="raised")

# Title 
title_lbl = tk.Label(window, text="Registration Form", font=("Arial", 18, "bold"), bg="lightblue", fg="blue")
title_lbl.grid(columnspan=2)

# Logo
# logo = tk.PhotoImage(file="logo.png")
# tk.Label(window, image=logo, bg="lightblue").grid(row=1, columnspan=2)

# Name section
frame1 = tk.Frame(window, bg="yellow", bd=5)
name_lbl = tk.Label(frame1, text="Name", font=("Arial", 12, "bold"), bg="yellow")
name_entry = tk.Entry(frame1, font=("Arial", 12))
name_lbl.pack()
name_entry.pack()
frame1.grid(row=2, column=0)

# Gender section
frame2 = tk.Frame(window, bg="#ffb3fe") 
gender_var = tk.StringVar()
male_rb = tk.Radiobutton(frame2, text="Male", variable=gender_var, value='M', font=("Arial", 12), bg="#ffb3fe")
female_rb = tk.Radiobutton(frame2, text="Female", variable=gender_var, value='F', font=("Arial", 12), bg="#ffb3fe")
other_rb = tk.Radiobutton(frame2, text="Other", variable=gender_var, value='O', font=("Arial", 12), bg="#ffb3fe")
male_rb.pack()
female_rb.pack()
other_rb.pack()
frame2.grid(row=2, column=1)

# Languages
lang_frame = tk.Frame(window)
lang_var1 = tk.IntVar()
lang_var2 = tk.IntVar()
lang_var3 = tk.IntVar()
c_cb = tk.Checkbutton(lang_frame, text="C", variable=lang_var1, font=("Arial", 12), bg="#ace0f9")
cpp_cb = tk.Checkbutton(lang_frame, text="C++", variable=lang_var2, font=("Arial", 12), bg="#ace0f9") 
java_cb = tk.Checkbutton(lang_frame, text="Java", variable=lang_var3, font=("Arial", 12), bg="#ace0f9")
c_cb.grid(row=0, column=0)
cpp_cb.grid(row=0, column=1)
java_cb.grid(row=0, column=2)
lang_frame.grid(row=3, columnspan=2)

# Degree  
degree_var = tk.StringVar()
degree_cb = ttk.Combobox(window, textvariable=degree_var, font=("Arial", 12))
degree_cb['values'] = ("Undergraduate", "Graduate", "Post Graduate")
degree_cb.grid(row=4, column=0)

# States
states_lb = tk.Listbox(window, height=5, font=("Arial", 12), bg="#ffcf9c")
states_lb.insert(1, "Madhya Pradesh")
states_lb.insert(2, "Maharashtra")
states_lb.grid(row=4, column=1)

# Submit function
def register():
    # Print registration details
    print("Registration successful!")
    print("Name:", name_entry.get())
    print("Gender:", gender_var.get())
    
    if lang_var1.get():
        print("Languages: C", end=" ")
    if lang_var2.get():
        print("C++", end=" ") 
    if lang_var3.get():
        print("Java")
        
    # Print selected state
    selected_state = states_lb.get(states_lb.curselection()) 
    print("State:", selected_state)
        
    print("Degree:", degree_var.get())

# Submit button
submit_btn = ttk.Button(window, text="Submit", style="Accent.TButton", command=register)
submit_btn.grid(row=5, columnspan=2)



window.mainloop()
 