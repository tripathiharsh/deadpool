from tkinter import*
import webbrowser


root = Tk()

root.geometry="790 x 434"
root.minsize(900,900)
root.maxsize(234,234)
root.title("I am Deadpool")
root.config(bg='orange')

label=Label(text="hello!!",font=("Snap ITC",19,"underline"))
label.pack(side='top')

new = 1
url = "https://www.google.com"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(root, text = "This opens Google",command=openweb,bg='red',activebackground='brown',)
Btn.pack(side='right')
def openweb():
    webbrowser.open(url2,new=new)
new = 1
url2 = "https://www.youtube.com"

Btn = Button(root, text = "This opens youtube",command=openweb,bg='red',activebackground='brown')
Btn.pack(side='left',)

root.mainloop()
