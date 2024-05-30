import tkinter as tk
import math

def main():
	global frequency,time,phase,zoom
	global can
	global wd,ht
	global pause

	if pause==0:

		
		can.delete("all")

		try:
			v=int(frequency)



			ar=[]

			for r in range(750):

				x=r*zoom*math.sin(math.radians((2*math.pi*int(frequency)*time)+phase))+wd/2
				y=r*zoom*math.cos(math.radians((2*math.pi*int(frequency)*time)+phase))+ht/2

				if r*zoom>750:
					break

				ar.append(x)
				ar.append(y)

				time+=1



			can.create_line(ar,fill="#32fca7")


			phase+=1
		except:
			pass


		def format_e(n):
			a = '%E' % n
			return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

		ff=frequency

		if len(str(frequency))>10:
			ff=format_e(int(frequency))


		can.create_text(20,ht-20,text="Frequency  ",fill="#ffffff",font=("FreeMono",13),anchor="w")
		can.create_text(120-10,ht-20,text=str(ff),fill="gold",font=("FreeMono",13),anchor="w")

		can.create_text(wd-20,ht-20,text="x "+str(zoom),fill="gold",font=("FreeMono",13),anchor="e")

	root.after(10,main)


def can_e(e):
	global frequency,time,phase,zoom

	ava="0123456789"

	if not ava.find(e.char)==-1:

		if frequency=="0":
			frequency=""

		frequency+=e.char

		time=0
		phase=0	
		zoom=1

def bs(e):

	global frequency,time,phase,zoom

	frequency=frequency[:-1]

	if frequency=="":
		frequency="0"

	time=0
	phase=0	
	zoom=1

def zoomin(e):
	global zoom

	zoom+=1



def zoomout(e):
	global zoom

	zoom-=1
	if zoom<1:
		zoom=1

def dn(e):
	pass

def pause_(e):
	global pause

	if pause==0:
		pause=1
	elif pause==1:
		pause=0

frequency="1"
time=0
phase=0
zoom=1

pause=0


root=tk.Tk()


wd=root.winfo_screenwidth()-10
ht=root.winfo_screenheight()-65

root.geometry(str(wd)+"x"+str(ht)+"+0+0")
#root.wm_attributes("-fullscreen",1)

root.title("frequency generator circular")


can=tk.Canvas(width=wd,height=ht,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)


can.bind("<space>",pause_)
can.bind("<BackSpace>",bs)
can.bind("<KeyPress>",can_e)
can.bind("<Right>",zoomin)
can.bind("<Left>",zoomout)
can.bind("<Up>",dn)
can.bind("<Down>",dn)

main()

can.focus_set()
root.mainloop()