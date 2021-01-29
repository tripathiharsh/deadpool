from tkinter import *
import webbrowser
root=Tk()
root.geometry =" 345 x 650"
root.minsize(900,900)
root.title("Food")
root.config(bg='grey')
#label
label=Label(text="Are you hungry!!😋🍟",font=(" French Fries",19,"underline"),bg='yellow',height=4,width=20)
label.pack()
#trvlabel
trv=Label(text="Want to book your meal online!",font=(" French Fries",19,"underline"),bg='orange')
trv.pack()
#radio


rtu=1
url3='https://www.pizzahut.co.in/'
def openweb():
    webbrowser.open(url3,new=rtu1)
R1 = Radiobutton(root, text="pizza hut", value=1,
                  command=openweb,bg='red',activebackground='green')
R1.pack( )

rtu1=1
url4='https://www.zomato.com'
def openweb():
    webbrowser.open(url4,new=rtu1)
R1 = Radiobutton(root, text="zomato", value=1,
                  command=openweb,bg='green',activebackground='green')
R1.pack( )


rtu2=1

url5='https://www.justeattakeaway.com'

def openweb():
    webbrowser.open(url5,new=rtu2)
R1 = Radiobutton(root, text="justeattakeaway", value=1,
                  command=openweb,bg='orange',activebackground='green')
R1.pack()



rtu4=1
url7='https://www.grubhub.com'
def openweb():
    webbrowser.open(url7,new=rtu4)
R1 = Radiobutton(root, text="grubhub", value=1,
                  command=openweb,bg='blue',activebackground='green')
R1.pack( )






#google
new=1
url='https://www.google.com'
def openweb():
    webbrowser.open(url,new=new)
bnt=Button(root,text='Google',command=openweb,bg='red',activebackground='green')
bnt.pack(fill=X)

#label1
label1=Label(text="Want to make your meal!!🍜  ",font=("times new roman",19,"underline"),bg='yellow',height=4,width=22)
label1.pack()
#label2
label2=Label(text="pizza!!🍕  ",font=("times new roman",19,"underline"),bg='yellow',height=4,width=22)
label2.pack(side='left')
#butto
new1=1
url2='https://youtu.be/PWB7vZy8Zp4'
def openweb():
    webbrowser.open(url2,new=new1)
bnt=Button(root,text='Play',command=openweb,bg='red',activebackground='green')
bnt.pack(side='left')














root.mainloop()
