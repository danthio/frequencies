import tkinter as tk

import math


def run():
	global can,amp,sig,zoom,speed

	v=int(round(float((700)/zoom),0))

	can.delete(sig)


	ar=[]
	x=40
	for y in amp:

		ar.append(x)
		ar.append(y)

		x+=700/v

	try:

		sig=can.create_line(ar,fill="#57f76d")
	except:
		pass

	draw_vals()

	root.after(speed,run)


def main():

	global can
	global amplitude,frequency,time,state,zoom
	global amp
	global speed

	global sig,freq,amp_,speed_,zoom_,sine1,sine2,cos1,cos2,p,st

	def update(z):

		global can
		global amplitude,frequency,time,state,zoom
		global amp
		global freq,amp_,speed_,zoom_,sine1,sine2,cos1,cos2,p
		global positive

		ar=[freq,amp_,speed_,zoom_,sine1,sine2,cos1,cos2]

		for _ in ar:

			can.delete(_)
	

		try:
			xv=int(frequency)


			v=int(round(float((700)/zoom),0))

			

			#for _ in range(v):

			if z==0:
				y=-amplitude*math.sin(math.radians(2*math.pi*int(frequency)*time))


				if positive==1:
					if y>0:
						y=-y

			elif z==1:
				y=-amplitude*math.cos(math.radians(2*math.pi*int(frequency)*time))

				if positive==1:
					if y>0:
						y=-y

			if y<=0:
				p=-y
			else:
				p=y

			

			


			if len(amp)<=v:
				amp.append(y+20+560/2)
			else:
				amp.pop(0)
				amp.append(y+20+560/2)


			time+=1



			




		except:
			pass

		
		amp_=can.create_text(1111-15-300+70,273,text=str(amplitude),fill="#57f76d",anchor="w",font=("FreeMono",13))

		
		def format_e(n):
			a = '%E' % n
			return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]


		f=str(frequency)

		if len(str(frequency))>10:

			try:
				f=str(format_e(int(frequency)))

			except:
				f=str(frequency)[:10]+"..."




		freq=can.create_text(1111-15-300+70,273+40+10-10,text=f,fill="#57f76d",anchor="w",font=("FreeMono",13))



		sine1=can.create_oval(1009+40-300+70,388-10-20, 1009+40+20-300+70,388+10-20,fill="#111111",outline="#57f76d")
		cos1=can.create_oval(1089+40-300+70,388-10-20, 1089+40+20-300+70,388+10-20,fill="#111111",outline="#57f76d")
		




		if state=="sine":
			sine2=can.create_oval(1009+40+4-300+70,388-10+4-20, 1009+40+20-4-300+70,388+10-4-20,fill="#57f76d",outline="#57f76d")
		elif state=="cos":
			cos2=can.create_oval(1089+40+4-300+70,388-10+4-20, 1089+40+20-4-300+70,388+10-4-20,fill="#57f76d",outline="#57f76d")




		draw_speed()


		zoom_=can.create_text(740,590,text="x "+str(zoom),fill="#57f76d",anchor="e",font=("FreeMono",11))



	if state=="sine":

		if st==0:
			update(0)
	elif state=="cos":
		if st==0:
			update(1)



	

	
	root.after(speed,main)

def draw_pointer():

	global can,pointer1,pointer2,pointer3,pointer4,p,amplitude

	

	can.delete(pointer1)
	can.delete(pointer2)
	can.delete(pointer3)
	can.delete(pointer4)

	angle=p*270/amplitude

	if angle>270:
		print(angle)

	start_angle=315+270-angle




	cx,cy=1025-10+100-300+70,20+100
	pointer3=can.create_text(cx,cy+80,text=str(round(p,3)),font=("FreeMono",13),fill="#57f76d")


	pointer4=can.create_arc(1025-10-5-300+70,20-5, 1025+200-10+5-300+70,20+200+5, start=315,extent=260,
		style="arc",outline="#222222",width=7)



	pointer1=can.create_arc(1025-10-5-300+70,20-5, 1025+200-10+5-300+70,20+200+5, start=start_angle,extent=angle,
		style="arc",outline="#57f76d",width=7)

	


	x=70*math.sin(math.radians(315-angle))+cx
	y=70*math.cos(math.radians(315-angle))+cy

	x2=11*math.sin(math.radians(315-angle+90-40))+cx
	y2=11*math.cos(math.radians(315-angle+90-40))+cy


	ax=30

	ar=[x,y,x2,y2]	

	a_=315-angle+90-40
	for a in range(180-80):

		x_=11*math.sin(math.radians(a_))+cx
		y_=11*math.cos(math.radians(a_))+cy

		a_-=1

		ar.append(x_)
		ar.append(y_)


	ar.append(x)
	ar.append(y)



	pointer2=can.create_polygon(ar,fill="#57f76d",outline="#57f76d")
	root.after(1,draw_pointer)


def draw_speed():
	global can,speed,speed_1,speed_2,speed_3

	can.delete(speed_1)
	can.delete(speed_2)
	can.delete(speed_3)

	x=(1250-40-300+70)-(speed*190/200)



	speed_1=can.create_oval(x-7,480-7+50, x+7,480+7+50,outline="#57f76d")
	speed_2=can.create_oval(x-3,480-3+50, x+3,480+3+50,outline="#57f76d",fill="#57f76d")


	speed_3=can.create_text(1250-40-300+70,480+30+50,text=str(round(speed/1000,3))+" s",fill="#57f76d",font=("FreeMono",13),anchor="e" )





def can_but(e):
	global speed,state
	global amplitude,amp,zoom,time,positive,_positive


	if 1020-15-300+70<=e.x<=1250-40+15-300+70:
		if 480-15+50<=e.y<=480+15+50:

			if 1020-300+70<=e.x<=1250-300+70:
				speed=int(((1250-300+70-40)-e.x)*200/190)

			if e.x<1020-300+70:
				speed=200

			if e.x>1250-300+70:
				speed=1

			if speed<=0:
				speed=1

			if speed>200:
				speed=200

			draw_speed()

			return


	cx,cy=1009+40+10-300+70,388-10+10-20

	r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

	if r<=10:
		state="sine"
		amp=[]
		time=0
		return

	cx,cy=1089+40+10-300+70,388-10+10-20
	r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

	if r<=10:
		state="cos"
		amp=[]
		time=0
		return

	cx,cy=1009+20+20+10-300+70+20,388+30-10+10
	r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

	if r<=10:

		if positive==0:
			positive=1
		elif positive==1:
			positive=0


		can.delete(_positive)


		if positive==0:
			_positive=can.create_oval(1009+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")

		elif positive==1:
			_positive=can.create_oval(1009+20+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")


		time=0
		amp=[]
		zoom=1


		return

	cx,cy=1009+20+20+20+10-300+70+20,388+30-10+10
	r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

	if r<=10:

		if positive==0:
			positive=1
		elif positive==1:
			positive=0

		can.delete(_positive)


		if positive==0:
			_positive=can.create_oval(1009+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")

		elif positive==1:
			_positive=can.create_oval(1009+20+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")


		time=0
		amp=[]
		zoom=1

		return

	if 1009+20+20+10-300+70+20<=e.x<=1009+20+20+20+20-10-300+70+20:
		if 388+30-10<=e.y<=388+30+10:



			if positive==0:
				positive=1
			elif positive==1:
				positive=0

			can.delete(_positive)


			if positive==0:
				_positive=can.create_oval(1009+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")

			elif positive==1:
				_positive=can.create_oval(1009+20+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")



			time=0
			amp=[]
			zoom=1


			return			



def kp(e):
	global amplitude,frequency,time,zoom
	global amp,st

	ava="0123456789."


	if not ava.find(e.char)==-1:

		if len(str(frequency))==0:
			frequency+=e.char

		if len(str(frequency))==1 and str(frequency)=="0":		
			frequency=""

		frequency+=e.char

		time=0
		amp=[]
		zoom=1

		st=0

def bs(e):
	global amplitude,frequency,time,zoom
	global amp,st



	frequency=frequency[:-1]
	time=0
	amp=[]
	zoom=1

	if frequency=="":
		frequency="0"
	st=0



def amp_up(e):

	global amplitude,time,amp,st


	amp=[]
	amplitude+=10

	if amplitude>280:
		amplitude=280
		st=0

def amp_down(e):

	global amplitude,time,amp,st


	amp=[]
	amplitude-=10

	if amplitude<10:
		amplitude=10
		st=0


def zoomin(e):

	global zoom,time,amp,st

	zoom+=2

	amp=[]
	time=0
	st=0

def zoomout(e):

	global zoom,time,amp,st

	if not zoom==1:

		zoom-=2

		if zoom<1:
			zoom=1

		amp=[]
		time=0
		st=0

def space(e):
 
	global st

	if st==0:
		st=1
	elif st==1:
		st=0



def draw_vals():
	global amplitude,can
	global dv_1,dv_2,dv_3,dv_4,dv_5,dv_6,dv_7,dv_8,dv_9,dv_10,dv_11
	
	cx,cy=1025-10+100-300+70,20+100



	a_=315
	a2=0

	can.delete(dv_1)
	can.delete(dv_2)
	can.delete(dv_3)	
	can.delete(dv_4)
	can.delete(dv_5)
	can.delete(dv_6)
	can.delete(dv_7)
	can.delete(dv_8)	
	can.delete(dv_9)
	can.delete(dv_10)
	can.delete(dv_11)

	a_=315
	a2=0

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_1=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")



	a_-=27
	a2=str(int(round(amplitude/10*1,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_2=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")


	a_-=27
	a2=str(int(round(amplitude/10*2,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_3=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")


	a_-=27
	a2=str(int(round(amplitude/10*3,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_4=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")



	a_-=27
	a2=str(int(round(amplitude/10*4,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_5=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")



	a_-=27
	a2=str(int(round(amplitude/10*5,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_6=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")


	a_-=27
	a2=str(int(round(amplitude/10*6,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_7=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")


	a_-=27
	a2=str(int(round(amplitude/10*7,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_8=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")

	a_-=27
	a2=str(int(round(amplitude/10*8,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_9=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")


	a_-=27
	a2=str(int(round(amplitude/10*9,0)))

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_10=can.create_text(x,y,text=str(a2),font=("FreeMono",8),fill="#57f76d")


	a_-=27
	a2=amplitude

	x=65*math.sin(math.radians(a_))+cx
	y=65*math.cos(math.radians(a_))+cy

	dv_11=can.create_text(x,y,text="   "+str(a2),font=("FreeMono",8),fill="#57f76d")


amplitude=200
frequency="1"
time=1
zoom=1
p=0

state="sine"

speed=2

amp=[]



sig=()
freq=()
amp_=()
speed_=()
zoom_=()

sine1=()
sine2=()

cos1=()
cos2=()

speed_1=()
speed_2=()
speed_3=()

pointer1=()
pointer2=()
pointer3=()
pointer4=()

positive=0
_positive=()


dv_1=()
dv_2=()
dv_3=()
dv_4=()
dv_5=()
dv_6=()
dv_7=()
dv_8=()
dv_9=()
dv_10=()
dv_11=()

st=0
root=tk.Tk()

root.title("HSCOPE")
root.geometry("1020x600+0+0")





can=tk.Canvas(width=1000+250-300+70,height=600,bg="#000000",relief="flat",highlightthickness=0,border=0)

can.create_rectangle(20+20,20,720+20,600-20,fill="#090909",outline="#555555")

can.create_line(20+20,20+140-70,720+20,20+140-70,fill="#323232")

can.create_line(20+20,20+140,720+20,20+140,fill="#323232")

can.create_line(20+20,20+140+70,720+20,20+140+70,fill="#323232")



can.create_line(20+20,20+140-70+280,720+20,20+140-70+280,fill="#323232")

can.create_line(20+20,20+140+280,720+20,20+140+280,fill="#323232")

can.create_line(20+20,20+140+70+280,720+20,20+140+70+280,fill="#323232")


can.create_line(20+20,20+(600-40)/2, 720+20,20+(600-40)/2,fill="#777777")

text=280

yy=20
for l in range(9):

	can.create_text(35,yy,text=str(text),fill="#777777", anchor="e")

	yy+=70

	text-=70





xx=40+70
while 1:
	can.create_line(xx,20,xx,600-20,fill="#323232")
	xx+=70

	if xx> 1000-20-300:
		break


can.create_oval(760,250, 760+40,250+40,fill="#111111",outline="#111111")
can.create_oval(998-40,250, 998,250+40,fill="#111111",outline="#111111")
can.create_oval(760,580-40, 760+40,580,fill="#111111",outline="#111111")
can.create_oval(998-40,580-40, 998,580,fill="#111111",outline="#111111")

can.create_polygon(760+20,250,998-20,250, 998,250+20, 998,580-20, 998-20,580,
	760+20,580, 760,580-20,760,250+20,fill="#111111",outline="#111111")



can.create_text(1009-300+70-5,273,text="Amplitude",fill="#888888",anchor="w",font=("FreeMono",13))
can.create_text(1009-300+70-5,273+40+10-10,text="Frequency",fill="#888888",anchor="w",font=("FreeMono",13))	
can.create_text(1009-300+70-5,388-20,text="sine ",fill="#888888",anchor="w",font=("FreeMono",13))
can.create_text(1089-300+70-5,388-20,text="cos ",fill="#888888",anchor="w",font=("FreeMono",13))	
can.create_text(1009-300+70-5,388+30,text="Positive",fill="#888888",anchor="w",font=("FreeMono",13))


can.create_arc(1009+20+20-300+70+20,388+30-10, 1009+20+20+20-300+70+20,388+30+10,outline="#57f76d",style="arc",
	start=90,extent=180)
can.create_arc(1009+20+20+20-300+70+20,388+30-10, 1009+20+20+20+20-300+70+20,388+30+10,outline="#57f76d",style="arc",
	start=270,extent=180)

can.create_line(1009+20+20+10-300+70+20,388+30-10,1009+20+20+20+20-10-300+70+20,388+30-10,fill="#57f76d")
can.create_line(1009+20+20+10-1-300+70+20,388+30+10,1009+20+20+20+20-10-300+70+20,388+30+10,fill="#57f76d")

can.create_text(1009-300+70-5,451+50,text="Speed",fill="#888888",font=("FreeMono",13),anchor="w" )
can.create_line(1020-300+70,480+50, 1250-40-300+70,480+50, fill="#57f76d",width=2)

if positive==0:
	_positive=can.create_oval(1009+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")

elif positive==1:
	_positive=can.create_oval(1009+20+20+20+3-300+70+20,388+30-10+3, 1009+20+20+20+20-3-300+70+20,388+30+10-3,outline="#57f76d",fill="#57f76d")

#meter








can.create_oval(1000+250/2-8-10-300+70,20+200/2-8, 1000+250/2+8-10-300+70,20+200/2+8,fill="#045d10",outline="#57f76d")
#can.create_oval(1000+250/2-5-10-300,20+200/2-5, 1000+250/2+5-10-300,20+200/2+5,fill="darkred",outline="red")


r=95

cx,cy=1025-10+100-300+70,20+100
v=3
v2=int(round(270/v,0))

sx=315
for a in range(v2):

	x1=r*math.sin(math.radians(sx))+cx
	y1=r*math.cos(math.radians(sx))+cy

	x2=(r-7)*math.sin(math.radians(sx))+cx
	y2=(r-7)*math.cos(math.radians(sx))+cy

	can.create_line(x1,y1, x2,y2,fill="#57f76d")

	sx-=v


v=27
v2=int(round(270/v,0))

sx=315
for a in range(v2+1):

	x1=r*math.sin(math.radians(sx))+cx
	y1=r*math.cos(math.radians(sx))+cy

	x2=(r-20-3+5)*math.sin(math.radians(sx))+cx
	y2=(r-20-3+5)*math.cos(math.radians(sx))+cy

	can.create_line(x1,y1, x2,y2,fill="#57f76d")

	sx-=v




can.bind("<KeyPress>",kp)
can.bind("<BackSpace>",bs)
can.bind("<Up>",amp_up)
can.bind("<Down>",amp_down)
can.bind("<Left>",zoomout)
can.bind("<Right>",zoomin)
can.bind("<Button-1>",can_but)
can.bind("<space>",space)


can.place(in_=root,x=0,y=0)

can.focus_set()
#draw_vals()

main()
run()
draw_pointer()
root.mainloop()
