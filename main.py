import os
import random
import time
import shutil
import sys
import tkinter as tk
import tkinter.ttk as ttk
import secrets
from tkinter import messagebox



def main():
    root = tk.Tk()
    root.title("Disk Space Filler")
    #root.geometry("400x200")
    root.resizable(0, 0)

    selected = tk.StringVar()
    filetype_select = tk.StringVar()

    
    tk.Label(root, text="Disk Space Filler", font=("Helvetica", 20)).pack()


    tk.Label(root, text="Megabytes:").pack()


    entry = tk.Entry(root)
    entry.pack()

   

    tk.Label(root, text="Mode:").pack()

    r1 = ttk.Radiobutton(root, text="Secure Mode", variable=selected, value="secure")
    r1.pack()

    r2 = ttk.Radiobutton(root, text="Normal Mode", variable=selected, value="normal")
    r2.pack()


    tk.Label(root, text="Filetype:").pack()


    r3 = ttk.Radiobutton(root, text="txt", variable=filetype_select, value="txt")
    r3.pack()

    r4 = ttk.Radiobutton(root, text="py", variable=filetype_select, value="py")
    r4.pack()  

    r5 = ttk.Radiobutton(root, text="pdf", variable=filetype_select, value="pdf")
    r5.pack()

    r6 = ttk.Radiobutton(root, text="jpg", variable=filetype_select, value="jpg")
    r6.pack()

    r7 = ttk.Radiobutton(root, text="png", variable=filetype_select, value="png")
    r7.pack()
    


    
    tk.Button(root, text="Fill", command=lambda: fill_disk_space(entry.get(), selected.get(), root)).pack()


    root.mainloop()

def fill_disk_space(megabytes, is_secure, master, filetype):
    try:
        megabytes = int(megabytes)
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return
        
        


    indicator = tk.Toplevel(master)
    indicator.title("Please wait...")
    indicator.resizable(0, 0)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(indicator, orient="horizontal", mode="determinate", maximum=megabytes, variable=progress_var)
    progress_bar.pack(pady=20)


    try:
        filetype = str(filetype)
    except ValueError:
        filetype = "txt"
    

    for i in range(0, megabytes):
        file = open(f"{i * random.randint(0, 245)}.{filetype}", "wb")

        if is_secure:
            data = secrets.token_bytes(1024 * 1024)
        else:
            data = os.urandom(1024 * 1024)

        file.write(data)
        file.close()

        progress_var.set(i / megabytes * 100)
        master.update_idletasks()

    indicator.destroy()

    messagebox.showinfo("", "Operation Complete")

if __name__ == "__main__":
    main()