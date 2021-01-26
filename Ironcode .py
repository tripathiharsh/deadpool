import tkinter as tk
Window=tk.Tk()
lable=tk.Lable(text="hello",
                width=12,hight=2,
)
lable.pack()
button=tk.Button(text="quit",
                 width=8,hight=2,
                 command=quit
)
button.pack()
window.mainloop()
