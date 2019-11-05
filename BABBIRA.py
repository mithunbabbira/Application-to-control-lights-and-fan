import tkinter as tk
import urllib.request


HEIGHT = 400
WIDTH = 400

def control(action):
	if(action==0):
		u=urllib.request.urlopen('http://188.166.206.43/fa045324698e48bb9be8e4887a89973c/update/D0?value=1')
	elif(action==1):
		u=urllib.request.urlopen('http://188.166.206.43/fa045324698e48bb9be8e4887a89973c/update/D0?value=0')
	elif(action==2):
		 u=urllib.request.urlopen('http://188.166.206.43/fa045324698e48bb9be8e4887a89973c/update/D2?value=0')
	elif(action==3):
		u=urllib.request.urlopen('http://188.166.206.43/fa045324698e48bb9be8e4887a89973c/update/D2?value=1')


root = tk.Tk()


root.configure(background='black')

# background = tk.Label(root, bg = 'red')
# background.place(relwidth=1, relheight=1)


# canvas = tk.Canvas(root,height=HEIGHT, width =WIDTH)
# canvas.pack()                                              // for initial size declaration (usefull for my other projects )

frame = tk.Frame(root, bg = '#9999ff', bd =10)
frame.place(relx=0.5 , rely = 0.2, relwidth =0.75, relheight =0.65, anchor='n')


button = tk.Button(frame,text='FAN ON',bg='#ff6666', command=lambda:control(0))
button.place(relx=0.006,rely=0.01,relwidth=0.5,relheight=0.5)


button = tk.Button(frame,text='FAN OFF',bg='#ff6666' ,  command=lambda:control(1))
button.place(relx=0.006,rely=0.5,relwidth=0.5,relheight=0.5)


button = tk.Button(frame,text='LIGHT ON',bg='#ff6666' ,  command=lambda:control(3))
button.place(relx=0.5,rely=0.01,relwidth=0.5,relheight=0.5)


button = tk.Button(frame,text='LIGHT OFF',bg='#ff6666',  command=lambda:control(2))
button.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.5)

root. mainloop()