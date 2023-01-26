from tkinter import *
import time

#parameters
sigma = 10
beta = 8 / 3
rho = 28
dt = 0.01
tend = 100

#initial conditions
x = [1]
y = [1]
z = [1]

x2 = [1]
y2 = [1.01]
z2 = [1]
t = 0

while t < tend:
	dx = dt * sigma * (y[-1] - x[-1])
	dy = dt * ((rho - z[-1]) * x[-1] - y[-1])
	dz = dt * (x[-1] * y[-1] - beta * z[-1])
	x.append(x[-1]+dx)
	y.append(y[-1]+dy)
	z.append(z[-1]+dz)
	dx2 = dt * sigma * (y2[-1] - x2[-1])
	dy2 = dt * ((rho - z2[-1]) * x2[-1] - y2[-1])
	dz2 = dt * (x2[-1] * y2[-1] - beta * z2[-1])
	x2.append(x2[-1]+dx2)
	y2.append(y2[-1]+dy2)
	z2.append(z2[-1]+dz2)
	t += dt

class lorenz:
	def __init__(self, master):
		self.master=master
		self.master.geometry("1100x1200")
		frame1 = Frame(self.master)
		frame1.pack()
		Button(frame1, text="Draw Overlap", command = self.overlap).pack(side=LEFT)
		Button(frame1, text="Draw separately", command = self.separate).pack(side=LEFT)
		self.label = Label(frame1, text="Time: 0s")
		self.label.pack(side=LEFT)

	def overlap(self):
		self.canvas = Canvas(self.master)
		self.canvas.pack(fill=BOTH, expand=1)

		#draw axis
		self.canvas.create_line(50,550,1050,550)
		self.canvas.create_line(550, 50, 550, 1050)

		#draw line segments
		num = len(x)

		pointer1 = self.canvas.create_oval(550+x[0]*10, 550-y[0]*10, 540+x[0]*10, 540-y[0]*10, fill="red")
		pointer2 = self.canvas.create_oval(550+x2[0]*10, 550-y2[0]*10, 540+x2[0]*10, 540-y2[0]*10, fill="blue")

		for i in range(0, num-1):
			self.canvas.delete(pointer1)
			self.canvas.delete(pointer2)
			self.canvas.create_line(550+x[i]*10, 550-y[i]*10, 550+x[i+1]*10, 550-y[i+1]*10, fill="red")
			self.canvas.create_line(550+x2[i]*10, 550-y2[i]*10, 550+x2[i+1]*10, 550-y2[i+1]*10, fill="blue")
			pointer1 = self.canvas.create_oval(550+x[i]*10, 550-y[i]*10, 540+x[i]*10, 540-y[i]*10, fill="red")
			pointer2 = self.canvas.create_oval(550+x2[i]*10, 550-y2[i]*10, 540+x2[i]*10, 540-y2[i]*10, fill="blue")
			self.label.configure(text = "Time: " + str(round(i * dt, 4)) + "s")

			time.sleep(0.005)
			self.master.update()

	def separate(self):
		self.win1 = Tk()
		self.win1.title("System1")
		self.win1.geometry("2200x1100")
		frame1 = Frame(self.win1, width=1100, height=1100, background="blue")
		frame1.pack(side=LEFT, expand=1, fill=BOTH)
		frame2 = Frame(self.win1, width=1100, height=1100, background="red")
		frame2.pack(side=LEFT, expand=1, fill=BOTH)
		self.canvas1 = Canvas(frame1)
		self.canvas1.pack(fill=BOTH, expand=1)
		self.canvas2 = Canvas(frame2)
		self.canvas2.pack(fill=BOTH, expand=1)

		#draw axis
		self.canvas1.create_line(50,550,1050,550)
		self.canvas1.create_line(550, 50, 550, 1050)
		self.canvas2.create_line(50,550,1050,550)
		self.canvas2.create_line(550, 50, 550, 1050)


		#draw line segments
		num = len(x)

		for i in range(0, num-1):
			self.canvas2.create_line(550+x2[i]*10, 550-y2[i]*10, 550+x2[i+1]*10, 550-y2[i+1]*10, fill="blue")
			self.canvas1.create_line(550+x[i]*10, 550-y[i]*10, 550+x[i+1]*10, 550-y[i+1]*10, fill="red")
			self.label.configure(text = "Time: " + str(i * dt) + "s")
			time.sleep(0.001)
			self.win1.update()

		self.win1.mainloop()

root=  Tk()
root.title("Lorenz system")
lorenz(root)
root.mainloop()



