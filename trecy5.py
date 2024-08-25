from tkinter import*
import keyboard

root=Tk()
root.title("Trecy 4")
root.geometry("600x600")
graph=Canvas(root,bg="cyan")
graph.pack(fill="both",expand=True)


T=[]
S=[]
u=[]
x=[]
vel=[]
exx=[]
oldexx=[]

n=100

for i in range(n):
    x.append(i)
    T.append(0)
    u.append(0)
    vel.append(0)
    S.append(0)
    exx.append(0)
    oldexx.append(0)

#T[0]=50
#u[0]=50


dt=.08
ds=1
alp=.1
E=1
k=5

scalex=5
scaley=5
offx=50
offy=300
speed=3
scalespeed=.1

cont1=1
while cont1==1:
    for i in range(n-1):
        graph.create_line(scalex*x[i]+offx,scaley*T[i]+offy,scalex*x[i+1]+offx,scaley*T[i+1]+offy,fill="red",width=2)
        graph.create_line(scalex*x[i]+offx,scaley*10*S[i]+offy,scalex*x[i+1]+offx,scaley*10*S[i+1]+offy,fill="dark blue",width=3)
        graph.create_line(scalex*x[i]+offx,scaley*u[i]+offy+200,scalex*x[i+1]+offx,scaley*u[i+1]+offy+200,fill="yellow",width=3)
        graph.create_line(scalex*(x[i]+u[i])+offx,100,scalex*(x[i]+u[i])+offx,150,fill="dark green",width=3)

    for i in range(1,n-1):
        exx[i]=(u[i+1]-u[i-1])/(2*ds)
        S[i]=E*exx[i]-alp*T[i]
        
    for i in range(1,n-1):
        T[i]+=k*(T[i-1]+T[i+1]-2*T[i])*dt/(ds**2)-10*alp*(exx[i]-oldexx[i])/(ds*dt)
        a=E*(u[i+1]+u[i-1]-2*u[i])/(ds**2)-alp*(T[i+1]-T[i-1])/(2*ds)-.1*vel[i]
        vel[i]+=a*dt
        u[i]+=vel[i]*dt

    for i in range(len(exx)):
        oldexx[i]=exx[i]

    if keyboard.is_pressed("up arrow"):
        offy-=speed
    if keyboard.is_pressed("down arrow"):
        offy+=speed
    if keyboard.is_pressed("left arrow"):
        offx+=speed
    if keyboard.is_pressed("right arrow"):
        offx-=speed
    if keyboard.is_pressed("w"):
        scaley+=scalespeed
    if keyboard.is_pressed("s"):
        scaley-=scalespeed
    if keyboard.is_pressed("a"):
        scalex+=scalespeed
    if keyboard.is_pressed("d"):
        scalex-=scalespeed
    if keyboard.is_pressed("i"):
        u[0]-=.2
    if keyboard.is_pressed("k"):
        u[0]+=.2
    if keyboard.is_pressed("u"):
        T[n-1]-=2
    if keyboard.is_pressed("j"):
        T[n-1]+=2

    graph.create_text(300,20,text="Thermoelasticity 1-D",fill="dark red", font=("Helvetica 20 bold"))
    graph.create_text(300,50,text="by Bryce",fill="dark red", font=("Helvetica 15 bold"))
    graph.create_text(500,475,text="Displacement",fill="yellow", font=("Helvetica 15 bold underline"))
    graph.create_text(500,275,text="Temperature",fill="red", font=("Helvetica 15 bold underline"))
    graph.create_text(75,275,text="Stress",fill="dark blue", font=("Helvetica 15 bold underline"))
    graph.create_text(100,75,text="Nodal locations",fill="dark green", font=("Helvetica 15 bold underline"))
    graph.create_text(25,475,text="i",fill="yellow", font=("Helvetica 20 bold"))
    graph.create_text(25,450,text="^",fill="yellow", font=("Helvetica 25 bold"))
    graph.create_text(25,525,text="k",fill="yellow", font=("Helvetica 20 bold"))
    graph.create_text(25,550,text="v",fill="yellow", font=("Helvetica 25 bold"))


    #graph.pack()

    root.update()
    graph.delete("all")












