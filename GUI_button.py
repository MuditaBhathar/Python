#9.create option button using tkinter GUI in python.
import tkinter as tk
r=tk.Tk()
r.title('The GUI in python')
button=tk.Button(r,text='Option',width=25,command=r.destroy)
button.pack()
r.mainloop()
