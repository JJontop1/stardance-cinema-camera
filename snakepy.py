import tkinter as tk
from tkinter import *
#makes window
root = tk.Tk()


is_recording = False
framecount = 0


#def = defining a new action
def toggle_record():
    global is_recording
    is_recording = not is_recording

    if is_recording:
        statuslabel.config(text="REC", fg="red")
        shutterbutt.config(text="STOP", bg="red", fg="white")
    else:
        statuslabel.config(text="READY", fg="green")
        shutterbutt.config(text="RECORD", bg="red", fg="white")
#remove close&minus
root.overrideredirect(True)

root.title("Kinda Cinema Cam")
root.geometry("800x480+0+0")
root.configure(bg= "black")

topbar = tk.Frame(root, bg="#1c1c1c", height=40)
topbar.pack(fill="x", side="top")

bottombar = tk.Frame(root, bg="#1c1c1c", height=40)
bottombar.pack(fill="x", side="bottom")

statuslabel = tk.Label(topbar, text="READY", fg="green", bg="#1c1c1c", font=("Arial", 12, "bold"))
statuslabel.pack(side="left", padx=15, pady=10)

storage = tk.Label(topbar, text="0.0/256 GB", fg="blue", bg="#1c1c1c", font=("Arial", 12, "bold"))
storage.pack(side="right", padx=15, pady=10)

#esc to close
root.bind("<Escape>", lambda e: root.destroy())

shutterbutt = tk.Button(bottombar,text="RECORD", bg="red", fg="white", command=toggle_record)
shutterbutt.pack()

root.mainloop()