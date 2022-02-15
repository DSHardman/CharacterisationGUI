import tkinter as tk

window = tk.Tk()

positions = tk.StringVar(value=["Random", "Fixed", "x Line", "y Line", "From File"])
position_list = tk.Listbox(listvariable=positions, selectmode="browse")

depths = tk.StringVar(value=["Random", "Fixed", "From File"])
depth_list = tk.Listbox(listvariable=depths, selectmode="browse")

temps = tk.StringVar(value=["Uncontrolled", "Fixed", "From File"])
temp_list = tk.Listbox(listvariable=temps, selectmode="browse")

def my_function(listbox):
    print(listbox.get(listbox.curselection()))

# this is a test change for git

position_list.bind('<<ListboxSelect>>', lambda event, a=position_list: my_function(a))

# frame
# label
# button
# checkbutton
# radiobutton
# entry
# combobox or listbox

position_list.pack()


window.mainloop()
