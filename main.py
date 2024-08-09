import os
import random
import sys
import tkinter as tk
import tkinter.ttk as ttk
import secrets
from tkinter import messagebox


checks = {
    "debugCheck": False
}


def debugCheck():
    if len(sys.argv) > 1 and sys.argv[1] == "safe":
        print("Function debugCheck() says: Debug mode is activated")
        return True
    return False


def main():
    root = tk.Tk()
    root.title("Disk Space Filler")
    # root.geometry("400x200")
    root.resizable(False, False)

    selected = tk.StringVar()
    filetype_select = tk.StringVar()

    ttk.Label(root, text="Disk Space Filler", font=("Helvetica", 20)).pack()

    ttk.Label(root, text="Megabytes:").pack()

    entry = tk.Entry(root)
    entry.pack()

    ttk.Label(root, text="Mode:").pack()

    r1 = ttk.Radiobutton(root, text="Secure Mode", variable=selected, value="secure")
    r1.pack()

    r2 = ttk.Radiobutton(root, text="Normal Mode", variable=selected, value="normal")
    r2.pack()

    ttk.Label(root, text="Filetype:").pack()

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

    tk.Button(root, text="Fill",
              command=lambda: fill_disk_space(entry.get(), selected.get(), root, filetype_select.get())).pack()

    root.mainloop()


# noinspection PyTypeChecker
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
    progress_bar = ttk.Progressbar(indicator, orient="horizontal", mode="determinate", maximum=100,
                                   variable=progress_var)
    progress_bar.pack(pady=1)

    try:
        filetype = str(filetype)
    except ValueError:
        filetype = "txt"

    for i in range(0, int(megabytes)):
        if is_secure:
            data = secrets.token_bytes(1024 * 1024)
        else:
            data = os.urandom(1024 * 1024)

        if not checks["debugCheck"]:
            file = open(f"{i * i}.{filetype}", "wb")

            file.write(data)
            file.close()

        progress_var.set(i / megabytes * 101)
        master.update_idletasks()

    indicator.destroy()

    messagebox.showinfo("", "Operation Complete")


if __name__ == "__main__":

    checks["debugCheck"] = debugCheck()
    main()
