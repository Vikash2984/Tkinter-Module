
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Student Registration')

# Label
reg_label = tk.Label(window, text="Student's Registration Form")  
reg_label.grid(row=0, column=0, columnspan=2)

# Name
name_label = tk.Label(window, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)

# Gender
gender_var = tk.StringVar()
male_rb = tk.Radiobutton(window, text="Male", variable=gender_var, value='M')
female_rb = tk.Radiobutton(window, text="Female", variable=gender_var, value='F')
other_rb = tk.Radiobutton(window, text="Other", variable=gender_var, value='O')
male_rb.grid(row=2, column=0)
female_rb.grid(row=2, column=1)
other_rb.grid(row=2, column=2)

# Languages 
lang_var1 = tk.IntVar()
lang_var2 = tk.IntVar()
lang_var3 = tk.IntVar()
c_cb = tk.Checkbutton(window, text="C", variable=lang_var1)
cpp_cb = tk.Checkbutton(window, text="C++", variable=lang_var2)
java_cb = tk.Checkbutton(window, text="Java", variable=lang_var3)
c_cb.grid(row=3, column=0) 
cpp_cb.grid(row=3, column=1)
java_cb.grid(row=3, column=2)

# Degree
degree_var = tk.StringVar()
degree_cb = ttk.Combobox(window, textvariable=degree_var) 
degree_cb['values'] = ("Undergraduate", "Graduate", "Post Graduate")  
degree_cb.grid(row=4, column=0, columnspan=2)

# States  
states_lb = tk.Listbox(window)
states_lb.insert(1, "Madhya Pradesh")
states_lb.insert(2, "Maharashtra")
states_lb.grid(row=5, column=0, columnspan=2)

# Submit
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
        
    print("Degree:", degree_var.get())
    
    # Print selected state
    selected_state = states_lb.get(states_lb.curselection()) 
    print("State:", selected_state)
    
submit_btn = tk.Button(window, text="Submit", command=register) 
submit_btn.grid(row=6, column=0, columnspan=2)

window.mainloop()